from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import length,DataRequired
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add some information about You')
    submit = SubmitField('Submit')
    
