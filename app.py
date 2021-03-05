from flask import Flask, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """ Return Dropdown with story options """

    return render_template("dropdown.html", story_options=stories.keys())


@app.route('/results')
def story_form():
    """Return MadLibs Questions"""

    session["story"] = request.args["story"]
    print(session["story"])
    return render_template("questions.html", words=stories[session["story"]].prompts, story_name=session["story"])


@app.route('/results', methods=["POST"])
def results():
    """Return MadLibs Results"""

    story_for_generation = stories[session["story"]]
    return render_template("story.html", story=story_for_generation.generate(request.form))
