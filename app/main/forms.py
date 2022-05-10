from wtforms import TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add some information about You')
    submit = SubmitField('Submit')
    
class UploadPitch(FlaskForm):
    category=SelectField('Select Category',validators=[DataRequired()],
                         choices=[
                            ('Interview Pitch','Interview Pitch'),
                            ('Products Pitch','Products Pitch'),
                            ('Tech Pitch','Tech Pitch'),
                            ('Political Pitch','Political Pitch'),
                            ('Religious Pitch','Religious Pitch'),
                            ('Pickup Lines','Pickup Lines'),
                            ('Others','None of the above')
                            ])
    pitch=TextAreaField('Write Pitch:',validators=[DataRequired()])
    submit=SubmitField('Post Pitch')
    
class CommentsForm(FlaskForm):
    comment=TextAreaField('Add a comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')