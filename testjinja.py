from jinja2 import Template
t = Template("Hello {{ something }}!")
print(t.render(something="world"))
