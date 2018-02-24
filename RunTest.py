import os
from flask import Flask,g,request
import ast
from jinja2 import Environment, FileSystemLoader
import collections

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

app = Flask("flaskr")
app.config.update(dict(DEBUG=True))

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

@app.route('/',methods=['POST','GET'])
def homepage():
    context = {'info':[{'':"Welcome to the CMU Course Network. Enter courses without \'-\' after the prefix. Enjoy."}]}


    if request.method=='POST':
        return some_class_page(request.form['text'])

    return render_template('GUI.html',context)

@app.route('/<class_page>',methods=['POST','GET'])
def some_class_page(class_page):


    inputfile = open("master_data.txt","r")
    master = ast.literal_eval(inputfile.readline())
    course_temp = master.get(class_page)

    Name = course_temp.get("name")
    Units = course_temp.get("units")
    Description = course_temp.get("desc")
    if(course_temp.get("prereqs")!=None):
        Prereqs = ast.literal_eval(course_temp.get("prereqs"))[0:6]
    else:
        Prereqs = course_temp.get("prereqs")
    if(course_temp.get("coreqs")!=None):
        Coreqs = ast.literal_eval(course_temp.get("coreqs"))[0:6]
    else:
        Coreqs = course_temp.get("coreqs")
    Postreqs = course_temp.get("postreqs")[0:6]

    course = collections.OrderedDict()
    #{"Name":Name,"Units":Units,"Description":Description,"Prereqs":Prereqs,"Coreqs":Coreqs,"Postreqs":Postreqs}
    course['Name'] = Name
    course['Units'] = Units
    course['Description'] = Description
    course['Prereqs'] = Prereqs
    course['Coreqs'] = Coreqs
    course['Postreqs'] = Postreqs

    context = {"info":[course]}

    return render_template('GUI.html', context)

if(__name__=="__main__"):
    app.run()

########################################
