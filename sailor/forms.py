from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, IntegerField
from wtforms.validators import DataRequired, Length,EqualTo,ValidationError
from sailor.models import  Entry
from sailor import db

class SearchForm(FlaskForm):
	searchTerm=StringField('Search',validators=[Length(max=21)])
	submit=SubmitField('Add Entry')

class DeleteForm(FlaskForm):	
	ID=IntegerField('ID to be deleted',validators=[DataRequired()])
	submit=SubmitField('Delete Entry')
	def validate_id(self,ID):
		entry=db.session.query(Entry.ID).filter_by(ID=ID.data)
		if(not entry):
			raise ValidationError("That ID does not exists in the database")

class NewEntryForm(FlaskForm):
	ID=IntegerField("ID")
	name=StringField("Name",validators=[DataRequired(),Length(min=2,max=50)])
	rating=IntegerField("Rating",validators=[DataRequired()])
	age=IntegerField("Age",validators=[DataRequired()])
	moreThanOneEntry=BooleanField('More Than One New Entry')
	submit=SubmitField('Add Entry')

	def validate_rating(self,rating):
		if not rating.data:
			raise ValidationError()
		if not(0<rating.data<10):
			raise ValidationError("Rating can only be between 0 and 10")

	def validate_age(self,age):
		if not age:
			raise ValidationError()
		if not(18<age.data<85):
			raise ValidationError("Sailors can only be between 18 and 85 years old")

class EditEntryForm(FlaskForm):
	ID=IntegerField("ID of Entry to be edited",validators=[DataRequired()])
	name=StringField("Name",validators=[DataRequired(),Length(min=2,max=50)])
	rating=IntegerField("Rating",validators=[DataRequired()])
	age=IntegerField("Age",validators=[DataRequired()])
	submit=SubmitField('Write Changes')
	def validate_ID(self,ID):
		entry=db.session.query(Entry.ID).filter_by(ID=ID.data).first()
		if(not entry):
			raise ValidationError("No such ID exists in directory")
	def validate_rating(self,rating):
		if not rating.data:
			raise ValidationError()
		if not(0<rating.data<10):
			raise ValidationError("Rating can only be between 0 and 10")

	def validate_age(self,age):
		if not age:
			raise ValidationError()
		if not(18<age.data<85):
			raise ValidationError("Sailors can only be between 18 and 85 years old")
