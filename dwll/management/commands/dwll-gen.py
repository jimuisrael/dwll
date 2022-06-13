# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

import traceback
import os
import shutil

from dwll import gen_engine

class ConsoleCommand:
    """

    Console Main Code Generator

    """

    def __init__(self):

        self.generator = gen_engine.GeneratorEngine()

    def menu(self):
        """

        Menu

        Description
            Despliega el Menu

        :return:
        """
        print('DWLL GENERATOR')
        print('What we gonna do?:')
        print('1. Generate Base')

    def welcome(self):
        print('_________________________\n')
        print('Welcome to Django Web Launch Library')
        print('_________________________\n')

    def main(self):
        """

        MAIN

        Description
            Funcion principal de entrada

        :return:
        """
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
            app_name = str(input('Input the app name:'))
            if app_name:
                path = '{}'.format(app_name)
                # TODO: Copiar y generar archivos
                os.mkdir(path)
                shutil.copyfile(src, dst)
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


