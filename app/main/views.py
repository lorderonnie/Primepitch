from flask import render_template
from . import main


@main.route('/')
def index():

    '''
    A function that returns the index page and its data
    '''
    message = 'PRIMEPITCH'
    return render_template('index.html',message= message)
                           
       