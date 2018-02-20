#! /usr/bin/env python3

from jinja2 import Environment, PackageLoader, select_autoescape

TEMPLATE_DIR = "templates"

env = Environment(
    loader=PackageLoader('test', TEMPLATE_DIR),
    autoescape=select_autoescape(['html', 'xml'])
)


def render(name):
    template = env.get_template(name)
    return template.render()
