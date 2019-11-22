from flask import render_template
from . import Main


@main.route('/')
def index():

    '''
    A function that returns the index page and its data
    '''
    message = 'PRIMEPITCH'
    return render_template('index.html',message= message)
                           
@app.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    This function  returns the movie details page and its data
    '''
    return render_template('pitch.html',id = pitch_id)                           
                           
                           