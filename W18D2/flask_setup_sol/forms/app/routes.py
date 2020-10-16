from app.forms.login import LoginForm
from app import app
from flask import render_template, redirect


@app.route('/')
def index():
    return render_template('page.html', title='Welcome')


@app.route('/login', methods=['GET', 'POST']) # we need to tell our route what methods will be used (we have GET by default)
def login():
    form = LoginForm()
    # Our form is an instance of LoginForm
    if form.validate_on_submit(): # A built in validator built in to flask-wtf.FlaskForm
        return redirect('/')
    return render_template('login.html', form=form)
    # We pass the form to our template under the name form


@app.route('/help')
def help():
    return render_template('page.html', title='Help')


@app.route('/item/<int:id>')
def item(id):
    if (id > 0 and id < 100):
        item = {
            "id": id,
            "name": f"Fancy Item {id}",
            "description": "Coming soon!",
        }
        return render_template('item.html', item=item)
    else:
        return '<h1>Sample App</h1><h2>Item Not Found</h2>'
