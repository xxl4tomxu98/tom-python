from app import app


@app.route('/')
def index():
    return '<h1>Sample App</h1><h2>Welcome</h2>'
 

@app.route('/help')
def help():
    return '<h1>Sample App</h1><h2>Help</h2>'


@app.route('/item/<int:id>') # we set a wildcard of id onto our route and limit it to int values
def item(id): # our function passed to the app.routes decorator can take the wildcard as a parameter
    if (id > 0 and id < 100):
        return f'<h1>Sample App</h1><h2>Item {id}</h2>' # we use string interpolation for the id
    else:
        return '<h1>Sample App</h1><h2>Item Not Found</h2>'
