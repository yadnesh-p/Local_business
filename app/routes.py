from flask import Blueprint, render_template
from .models import get_db

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')