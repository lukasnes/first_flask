"""Greeting Flask app."""

from random import choice

from flask import Flask, request, url_for

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return f"""<!doctype html><html>Hi! This is the home page.<a href="{ url_for('hello') }">Hello!</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <label for="compliments">Choose a compliment:</label>
                               <select id="compliments" name="compliments">
                                  <option value="awesome">awesome</option>
                                  <option value="terrific">terrific</option>
                                  <option value="fantastic">fantastic</option>
                                  <option value="neato">neato</option>
                                  <option value="fantabulous">fantabulous</option>
                                  <option value="wowza">wowza</option>
                                  <option value="oh-so-not-meh">oh-so-not-meh</option>
                                  <option value="brilliant">brilliant</option>
                                  <option value="ducky">ducky</option>
                                  <option value="coolio">coolio</option>
                                  <option value="incredible">incredible</option>
                                  <option value="wonderful">wonderful</option>
                                  <option value="smashing">smashing</option>
                                  <option value="lovely">lovely</option>
                              </select>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          What's your name? <input type="text" name="person2">
          <label for"disses">Choose a diss:</label>
              <select id="diss" name="diss">
                  <option value="monkey">monkey</option>
                  <option value="pig">pig</option>
                  <option value="skunk">skunk</option>
                  <option value="garbage truck">garbage truck</option>
                  <option value="landfill">landfill</option>
              </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get('compliments')

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
  """Get user by name."""
  
  player = request.args.get("person2")
  
  diss = request.args.get("diss")
  
  return f"""
  <!doctype html>
  <html>
    <head>
      <title>A diss</title>
    </head>
    <body>
      Man, {player}, you smell like a {diss}..
    </body>
  </html>
  """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
