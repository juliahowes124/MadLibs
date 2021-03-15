from flask import Flask, render_template, request, session, redirect
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories, Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """ Render Dropdown with story options """

    return render_template("dropdown.html", story_options=stories.keys())


@app.route('/results')
def story_form():
    """ Render MadLibs Questions """

    session["story"] = request.args["story"]
    return render_template("questions.html", words=stories[session["story"]].prompts, story_name=session["story"])


@app.route('/results', methods=["POST"])
def results():
    """ Render MadLibs Generated Story """

    story_for_generation = stories[session["story"]]
    return render_template("story.html", story=story_for_generation.generate(request.form))


@app.route('/create')
def show_template_form():
    """ Displays form for creating a new story template """
    
    return render_template("create_story_template.html")


@app.route('/create', methods=["POST"])
def create_template():
    """ Creates a new story template and adds to dictionary of stories """

    story_name = request.form["story_name"]
    word1 = request.form["word_type_1"]
    word2 = request.form["word_type_2"]
    text1 = request.form["text_1"]
    text2 = request.form["text_2"]

    prompts = [word1, word2]
    template = text1 + " {" + word1 + '} ' + text2 + " {" + word2 + "} "

    stories[f"{story_name}"] = Story(prompts, template)
    return redirect("/")
