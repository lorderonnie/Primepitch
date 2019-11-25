from flask import render_template
from . import main
from flask_login import login_required


@main.route('/')
def index():

    '''
    This function  returns the index page and its data
    '''
    title = 'PRIMEPITCH the best pitching site in the country!!!'
    return render_template('index.html',title= title)
 
                          
       