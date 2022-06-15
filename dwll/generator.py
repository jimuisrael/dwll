from django.template.loader import render_to_string
from pathlib import Path

import shutil
import os
import traceback

BASE_DIR = Path(__file__).resolve().parent

class Template:

    PYTHON_FILE = 'py'
    HTML_FILE = 'html'

    def __init__(self, app_name, template_name, ext='py'):
        self.app_name = app_name
        self.template_name = template_name
        self.ext = ext
        self.current_path = os.path.abspath(os.getcwd())

        print('Generating file {} at path'.format(self.template_name, self.current_path))

    def create_dir(self, dirname, secondary='', third=''):
        try:
            path = os.path.join(self.current_path, dirname, secondary, third)
            if not os.path.isdir(path):
                os.mkdir(path)
        except:
            pass

    def render(self):
        """
        Renderiza el template dado en el archivo solicitado
        """
        try:
            template_file = '%s_template.html' % self.template_name

            if self.ext == self.PYTHON_FILE:
                self.create_dir(self.app_name)
                rendered = render_to_string(template_file, {'app_name': self.app_name})
                to_path = os.path.join(self.current_path, self.app_name,
                    '%s.py' % ("__init__" if  self.template_name == 'init' else self.template_name))
                print('Creando archivo Python en', to_path)
                with open(to_path, 'w') as f:
                    f.write(rendered)
            else:
                
                from_path = os.path.join(BASE_DIR, 'templates', template_file)
                if self.template_name in ['login','logout']:
                    self.create_dir(self.app_name, 'templates', 'account')
                    to_path = os.path.join(self.current_path, self.app_name, 'templates', 
                        'account', '%s.html' % self.template_name)
                else:
                    self.create_dir(self.app_name, 'templates')
                    to_path = os.path.join(self.current_path, self.app_name, 'templates', 
                        '%s.html' % self.template_name)
                print('Creando archivo HTML desde', from_path, 'hasta', to_path)
                shutil.copyfile(from_path, to_path)
        except Exception as e:
            print('Generation Error:',e)
            traceback.print_exc()

class Generator:

    def __init__(self, app_name):
        self.app_name = app_name

class AppGenerator(Generator):

    def generate(self):
        Template(self.app_name, 'init').render()
        Template(self.app_name, 'apps').render()
        Template(self.app_name, 'models').render()
        Template(self.app_name, 'signals').render()
        Template(self.app_name, 'tests').render()
        Template(self.app_name, 'urls').render()
        Template(self.app_name, 'views').render()

class AppTemplatesGenerator(Generator):

    def generate(self):
        Template(self.app_name, 'base', 'html').render()
        Template(self.app_name, 'header', 'html').render()
        Template(self.app_name, 'footer', 'html').render()
        Template(self.app_name, 'home', 'html').render()
        Template(self.app_name, 'login', 'html').render()
        Template(self.app_name, 'logout', 'html').render()
        Template(self.app_name, 'menu', 'html').render()


def run_generator_engine(option, app_name=None):

    if option == 'app':
        if app_name:
            AppGenerator(app_name).generate()
            AppTemplatesGenerator(app_name).generate()