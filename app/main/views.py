from flask import render_template
from . import main
from flask_login import login_required


@main.route('/')
def index():

    '''
    This function  returns the index page and its data
    '''
    message = 'PRIMEPITCH'
    return render_template('index.html',message= message)
 
@main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):                          
       