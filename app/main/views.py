from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,NewPitch,CommentForm
from .. import db,photos

@main.route('/')
def index():

    '''
    This function  returns the index page and its data
    '''
    title = 'PRIMEPITCH'
    pitches = Pitch.get_all_pitches()
    games = Pitch.get_pitch_by_category("games")
    business = Pitch.get_pitch_by_category("business")
    music = Pitch.get_pitch_by_category("music")
    tech = Pitch.get_pitch_by_category("tech")
    
    return render_template('index.html',title= title,games = games,business = business,music = music,tech = tech)
 
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    pitch = Pitch.get_user_pitch(user.username)
    return render_template('profile/profile.html',pitch = pitch, user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/new/<uname>' ,methods=["GET",'POST'])
def new_pitch(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = NewPitch()
    if form.validate_on_submit():
        title =form.title.data
        pitch = form.body.data
        category = form.category.data
        
        new_pitch = Pitch(title = title,body = pitch,category = category, user =uname)

        new_pitch.saves_pitch()
        
        return redirect(url_for('main.new_pitch',uname = current_user.username))
    title = "New pitch"
    return render_template('newpitch.html',title = title, new_pitch_form = form, user = user)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    pitch = Pitch.query.filter_by(id = id ).first()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(pitch_id = pitch.id, comment = comment, user = current_user.username)
        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id))

    title = f'{pitch.pitch_title} comment'
    return render_template('comment.html',title = title, comment_form = form,pitch = pitch)
   
# @main.route('/pitch/<id>')
# def pitch(id):
    # pitch = Pitch.query.filter_by(id = id).first()
    
    # comment = Comment.get_pitch_comment(pitch.id)
    # return render_template('pitch.html',pitch = pitch,comment = comment )
    
@main.route('/categories/<category>', methods=['GET',"POST"])    
def categories(category):
    pitches=Pitch.get_pitch_by_category(category)
    
    return render_template('categories.html',pitches=pitches)
