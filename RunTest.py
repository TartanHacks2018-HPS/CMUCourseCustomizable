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

@app.route('/',methods=["Course"])
def create_index_html():
    inputfile = open("master_data.txt","r")
    master = ast.literal_eval(inputfile.readline())
    course = master.get("21-222")


    #num = str(76101)
    #name = str(course[1])
    #prereqs = str(course[6])
    #desc = str(course[2])
    #postreqs = str(course[5])
    #department = str(course[4])
    #units = str(course[0])
    #coreqs = str(course[3])



    context = {"info":[course]}
    #
    #fname = "render_template.html"


    return render_template('template.html', context)

########################################
