import os
import ast
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    inputfile = open("master_data.txt","r")
    master = ast.literal_eval(inputfile.readline())
    course = master.get("21-228")


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
    fname = "render_template.html"
    with open(fname, 'w') as f:
        html = render_template('GUI.html', context)
        f.write(html)


def main():
    create_index_html()

########################################

if __name__ == "__main__":
    main()
