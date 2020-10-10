from flask import Flask, redirect, url_for, flash, request, render_template,session
from sailor.forms import  NewEntryForm, SearchForm, EditEntryForm, DeleteForm
from sailor.models import Entry
from sailor import app, db,bcrypt

@app.route('/',methods=['POST','GET'])
def home():
	rows=Entry.query.all()
	form=SearchForm()
	if form.validate_on_submit():
		if form.searchTerm.data=="":
			return render_template('home.html',title='Welcome',rows=rows,form=form)
		rows=[]
		NameRows=Entry.query.filter_by(name=form.searchTerm.data.strip())
		AddressRows=Entry.query.filter_by(address=form.searchTerm.data.strip())
		PhoneRows=[]
		try:
			PhoneRows=Entry.query.filter_by(phone_num=int(form.searchTerm.data.strip()))
		except:
			pass
		for field in (NameRows,AddressRows, PhoneRows):
			for data in field:
				rows.append(data)
	return render_template('home.html',title='Welcome',rows=rows,form=form)




@app.route('/admin/newentry',methods=['GET','POST'])
def newEntry():
	form=NewEntryForm()
	if form.validate_on_submit():
		entry=Entry(name=form.name.data.lower(),rating=form.rating.data,age=form.age.data)
		db.session.add(entry)
		db.session.commit()
		flash("Entry has been added","success")
		if(not form.moreThanOneEntry.data):
			return redirect(url_for('home'))
		else:
			return redirect(url_for('newEntry'))
	rows=Entry.query.all()
	# flash(form.ID.data)
	return render_template('newEntry.html',title="new",form=form,rows=rows)

@app.route('/admin/editentry',methods=['POST','GET'])
def editEntry():
	form=EditEntryForm()
	if form.validate_on_submit():
		entry=Entry.query.filter_by(ID=form.ID.data).first()
		entry.name=form.name.data.lower()
		entry.age=form.age.data
		entry.rating=form.rating.data
		db.session.commit()
		flash("The entry has been updated","success")
		return redirect(url_for('home'))
	rows=Entry.query.all()
	return render_template('update.html',title="Update entry",form=form,rows=rows)

@app.route('/admin/delete',methods=['POST','GET'])
def deleteEntry():
	form=DeleteForm()
	if form.validate_on_submit():
		entry=Entry.query.filter_by(ID=form.ID.data).first()
		db.session.delete(entry)
		db.session.commit()
		flash("The entry has been deleted","success")
		return redirect(url_for('deleteEntry'))
	rows=Entry.query.all()
	return render_template('deleteEntry.html',title="Delete entry",form=form,rows=rows)

