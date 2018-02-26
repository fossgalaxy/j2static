#! /usr/bin/env python3

import json
import os

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE_DIR = "templates"
DATA_DIR = "data"
SITE_DIR = "site"
ESCAPE = ('html', 'xml')

class TemplateEngine(object):
    
    def __init__(self):
        loader = FileSystemLoader(TEMPLATE_DIR)

        self.env = Environment(
            loader=loader,
            autoescape=select_autoescape(ESCAPE)
        )

    def load_data(self, name):
        """Attempt to load a json encoded datafile"""
        try:
            template_name, ext = os.path.splitext(name)

            path = os.path.join(DATA_DIR, template_name+".json")
            with open(path) as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def load_data_dir(self, data_dir):
        """Load all data files in a given directory"""
        print("--data dir--")
        for f in glob.iglob(data_dir + "*.json", recursive=True):
            
            print(f)
 
    def render(self, name):
        template = self.env.get_template(name)
        data = self.load_data(name)
        return template.render(data)

    def get_templates(self):
        return self.env.list_templates(["html", "htm", "xml"])

def generate():

    engine = TemplateEngine()
    for template in engine.get_templates():
        gen_path = os.path.join(SITE_DIR, template)
        with open(gen_path, 'w') as f:
            template_data = engine.render(template)
            f.write(template_data)
