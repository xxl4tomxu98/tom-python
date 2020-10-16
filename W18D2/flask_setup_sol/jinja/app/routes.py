from flask import render_template # we import render template from flask
from app import app


@app.route('/')
def index():
    return render_template('page.html', title='Welcome')


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
        # rather than returning a value, we render an html file from our templates directory
        # we can pass variables to our template by setting a variable name equal to some value
    else:
        return '<h1>Sample App</h1><h2>Item Not Found</h2>'
