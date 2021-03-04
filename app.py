from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import story_dict

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """ Return Dropdown with story options """

    return render_template("dropdown.html", story_options=story_dict.keys())


@app.route('/results')
def story_form():
    """Return MadLibs Homepage"""

    story_name = request.args["story"]
    return render_template("questions.html", words=story_dict[story_name].prompts, story_name=story_name)


# @app.route('/results', methods=["POST"])
# def results():
#     """Return MadLibs results"""

#     return render_template("story.html", story=silly_story.generate(request.form))
