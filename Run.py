from jinja2 import Template
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('GUI.html', my_list=[0,1,2,3,4,5])


if __name__ == 'GUI.html':
    #app.run(debug=True)

    t = Template("Hello {{ something }}!")
    t.render(something="World")
    t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
    t.render()

template_test()
