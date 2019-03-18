import os
from flask import render_template, redirect, request
from app import app, db
from app.models import Entry
from werkzeug import secure_filename

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods = [ 'GET', 'POST' ])
def uploader_file():
    if request.method == 'POST':
        file = request.files['file']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
        return render_template('upload.html')


@app.route('/content')
def content():
    entries = Entry.query.all()
    return render_template('content.html', title='Collection', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        asset_name = form.get('asset_name')
        format = form.get('format')
        source = form.get('source')
        full_description = form.get('full_description')
        if not asset_name or format or source or full_description:
            entry = Entry(asset_name = asset_name, format = format, source = source, full_description = full_description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

@app.route('/update/<int:id_no>')
def updateRoute(id_no):
    if not id_no or id_no != 0:
        entry = Entry.query.get(id_no)
        if entry:
            return render_template('update.html', entry=entry)

#CHECK FUNCTION
@app.route('/update', methods=['POST'])
def update():
    if not id_no or id_no != 0:
        entry = Entry.query.get(id_no)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

@app.route('/delete/<int:id_no>')
def delete(id_no):
    if not id_no or id_no != 0:
        entry = Entry.query.get(id_no)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')


#CHECK FUNCTION - NOT USED
@app.route('/turn/<int:id_no>')
def turn(id_no):
    if not id_no or id_no != 0:
        entry = Entry.query.get(id_no)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')



# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"
