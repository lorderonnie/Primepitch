from flask_wtf import  FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators =[Required()])
    submit = SubmitField('Submit')   
    
class NewPitch(FlaskForm):
    title = StringField('pitch title', validators = [Required()])
    category = SelectField(u'input category', choices = [('business','business'),('games','games'),('music','music'),('tech','tech')])
    body = TextAreaField('write your pitch', validators = [Required()]) 
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    comment = TextAreaField('write a comment',validators=[Required()])
    submit = SubmitField('Submit')   
    