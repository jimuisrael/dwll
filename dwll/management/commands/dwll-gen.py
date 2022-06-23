# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

import traceback
import os
import shutil

from dwll import generator

class ConsoleCommand:

    def menu(self):
        print('DWLL GENERATOR')
        print('What we gonna do?:')
        print('1. Generate New App')
        print('0. Salir')

    def welcome(self):
        print('_________________________\n')
        print('Welcome to Django Web Launch Library')
        print('_________________________\n')

    def main(self):
        self.welcome()
        self.menu()

        try:
            while (True):
                option = str(input("Select and option[and press ENTER]: "))
                if option == '0':
                    break
                elif option == '1':
                    self.option_1()
                    self.menu()
                else:
                    print('Invalid Option:', option)
        except Exception as e:
            print('Error to process: %s' % str(e))
            traceback.print_exc()

    def option_1(self):
        try:
            app_name = str(input('Set the app name:'))
            
            option = str(input("Do you need to generate example model? (y/N) "))
            model_name = None
            if option == 'y':
                model_name = str(input('Set the model name:'))
            
            generator.run_generator_engine('app', app_name, model_name)
        except Exception as e:
            print('Error al procesar opcion 1:', str(e))
            traceback.print_exc()

class Command(BaseCommand):
    """

    Comandos de configuracion

    """
    args = '<app app ...>'
    help = 'Console Code  Generator'

    def handle(self, *args, **kwargs):
        """

        Generador de codigo por consola

        :param args:
        :param options:
        :return:
        """
        ConsoleCommand().main()
