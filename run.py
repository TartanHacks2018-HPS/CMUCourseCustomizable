from jinja2 import Environment, PackageLoader, select_autoescape
evn = Environment(loader=PackageLoader('application','templates'),autoescape=select_autoescape(['html','xml'])))
