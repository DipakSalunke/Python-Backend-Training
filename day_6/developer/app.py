''''
Implement a small Flask App with HTML
Create a new project
Create and activate venv
Install Flask
Use HTML templates to display a developers name in a color of your choice
'''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/developer/<string:name>')
def dev(name):
    return render_template('index.html', name=name)


app.run(port=5001)
