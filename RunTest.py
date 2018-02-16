import os
from flask import Flask,g
import ast
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

app = Flask("flaskr")
app.config.update(dict(DEBUG=True))

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

#@app.route('/')
#def homepage():
#    return"""<h1>Hello world!</h1>"""

@app.route('/<class_page>')
def some_class_page(class_page):
    inputfile = open("master_data.txt","r")
    master = ast.literal_eval(inputfile.readline())
    course_temp = master.get(class_page)

    Name = course_temp.get("name")
    Units = course_temp.get("units")
    Description = course_temp.get("desc")
    if(course_temp.get("prereqs")!=None):
        Prereqs = ast.literal_eval(course_temp.get("prereqs"))
    else:
        Prereqs = course_temp.get("prereqs")
    if(course_temp.get("coreqs")!=None):
        Coreqs = ast.literal_eval(course_temp.get("coreqs"))
    else:
        Coreqs = course_temp.get("coreqs")
    Postreqs = course_temp.get("postreqs")

    course = {"Name":Name,"Units":Units,"Description":Description,"Prereqs":Prereqs,"Coreqs":Coreqs,"Postreqs":Postreqs}

    context = {"info":[course]}

    return render_template('GUI.html', context)

if(__name__=="__main__"):
    app.run()

########################################
