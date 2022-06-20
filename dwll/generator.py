from django.template.loader import render_to_string
from pathlib import Path

import shutil
import os
import traceback

from .memory import dinamic

BASE_DIR = Path(__file__).resolve().parent

class Template:

    PYTHON_FILE = 'py'
    HTML_FILE = 'html'

    def __init__(self, app_name, model_name, template_name, ext='py', do_replace=False):
        self.app_name = app_name
        self.model_name = model_name
        self.template_name = template_name
        self.ext = ext
        self.current_path = os.path.abspath(os.getcwd())
        self.do_replace = do_replace

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
                rendered = render_to_string(template_file, {'app_name': self.app_name, 
                                                            'model_name': self.model_name})
                to_path = os.path.join(self.current_path, self.app_name,
                    '%s.py' % ("__init__" if  self.template_name == 'init' else self.template_name))
                
                print('- Creando archivo Python:', self.template_name)
                
                with open(to_path, 'w') as f:
                    f.write(rendered)
            else:
                
                from_path = os.path.join(BASE_DIR, 'templates', template_file)
                if self.template_name in ['login','logout']:
                    self.create_dir(self.app_name, 'templates', 'account')
                    to_path = os.path.join(self.current_path, self.app_name, 'templates', 
                        'account', '%s.html' % self.template_name)
                elif self.template_name in ['list','form']:
                    self.create_dir(self.app_name, 'templates', self.app_name)
                    to_path = os.path.join(self.current_path, self.app_name, 'templates', 
                        self.app_name, '%s_%s.html' % (self.model_name, self.template_name))
                else:
                    self.create_dir(self.app_name, 'templates')
                    to_path = os.path.join(self.current_path, self.app_name, 'templates', 
                        '%s.html' % self.template_name)
                    
                print('- Creando archivo HTML:', self.template_name)
                
                shutil.copyfile(from_path, to_path)
                
                if self.do_replace:
                    self.replace_html_var(to_path)
        except Exception as e:
            print('Generation Error:',e)
            traceback.print_exc()
            
    def replace_html_var(self, final_path):
        dinamic.replace_html(final_path, '[ITEM]', self.model_name)

class Generator:

    def __init__(self, app_name, model_name=None):
        self.app_name = app_name
        self.model_name = model_name

class AppGenerator(Generator):

    def generate(self):
        Template(self.app_name, self.model_name, 'init').render()
        Template(self.app_name, self.model_name, 'apps').render()
        Template(self.app_name, self.model_name, 'admin').render()
        Template(self.app_name, self.model_name, 'models').render()
        Template(self.app_name, self.model_name, 'signals').render()
        Template(self.app_name, self.model_name, 'tests').render()
        Template(self.app_name, self.model_name, 'urls').render()
        Template(self.app_name, self.model_name, 'views').render()
        Template(self.app_name, self.model_name, 'forms').render()

class AppTemplatesGenerator(Generator):

    def generate(self):
        Template(self.app_name, None, 'base', 'html').render()
        Template(self.app_name, None, 'header', 'html').render()
        Template(self.app_name, None, 'footer', 'html').render()
        Template(self.app_name, None, 'home', 'html').render()
        Template(self.app_name, None, 'login', 'html').render()
        Template(self.app_name, None, 'logout', 'html').render()
        Template(self.app_name, None, 'menu', 'html').render()
        Template(self.app_name, None, 'messages', 'html').render()
        
        if self.model_name:
            Template(self.app_name, self.model_name, 'list', 'html', do_replace=True).render()
            Template(self.app_name, self.model_name, 'form', 'html').render()

def run_generator_engine(option, app_name=None, model_name=None):

    if option == 'app':
        if app_name:
            AppGenerator(app_name, model_name).generate()
            AppTemplatesGenerator(app_name, model_name).generate()