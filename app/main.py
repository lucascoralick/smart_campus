from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
@login_required
def home():
    return render_template('home.html')

@main.route('/events')
@login_required
def events():
    return render_template('events.html')

@main.route('/map')
@login_required
def map():
    return render_template('map.html')
