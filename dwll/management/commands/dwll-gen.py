# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

import traceback

from dwll import generator

class ConsoleCommand:

    def menu(self):
        print('GENERADOR DWLL')
        print('Elija una actividad a realizar:')
        print('1. Generar nueva APP')
        print('0. Salir')

    def welcome(self):
        print('_____________________________________\n')
        print('Bienvenido a Django Web Lauch Library')
        print('_____________________________________\n')

    def main(self):
        self.welcome()
        self.menu()

        try:
            while (True):
                option = str(input('Ingrese actividad [y pulse ENTER]: '))
                if option == '0':
                    break
                elif option == '1':
                    self.option_1()
                    self.menu()
                else:
                    print('Actividad Incorrecta:', option)
        except Exception as e:
            print('Error al procesar: %s' % str(e))
            traceback.print_exc()

    def option_1(self):
        try:
            app_name = str(input('Ingrese un nombre de APP:'))
            
            option = str(input("Quiere autogenerar un modelo de ejemplo? (s/N) "))
            model_name = None
            if option == 's':
                model_name = str(input('Ingrese el nombre del modelo (tabla):'))
            
            generator.run_generator_engine('app', app_name, model_name)
        except Exception as e:
            print('Error al procesar opcion 1:', str(e))
            traceback.print_exc()

class Command(BaseCommand):
    """

    Comandos de configuracion

    """
    args = '<app app ...>'
    help = 'Console Code Generator'

    def handle(self, *args, **kwargs):
        """

        Generador de codigo por consola

        :param args:
        :param options:
        :return:
        """
        ConsoleCommand().main()
