from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

STORY_TYPE = silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Return MadLibs Homepage"""

    return render_template("questions.html", words = STORY_TYPE.prompts)

@app.route('/results')
def results():
    """Return MadLibs results"""
    story = STORY_TYPE.generate(request.args)

    return render_template("story.html", story = story)    
