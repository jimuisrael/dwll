# -*- coding: utf-8 -*-
"""
.. module:: dbu-messages
   :platform: Unix, Windows
   :synopsis: Manejador de mensajes de uso comun y principal

.. moduleauthor:: Diego Gonzalez <dgonzalez.jim@gmail.com>

"""
from . import models
from .memory import memory

class LanguageManager:
    """

    Language Manager
    ===================

    Description
        Manejador de lenguajes, permite conseguir el lenguaje principal del sistema.

    """

    DEFAULT = 'spanish'

    def get_default(self):
        """

        Get Default

        Description
            Permite consultar el lenguaje por defecto del sistema, si hay mas de uno
            devuelve el primero en localizarse

        :return
            models.Language -- El lenguaje principal del sistema

        """
        main_languages = models.Language.objects.get_active(default=True)

        if main_languages.exists():
            return main_languages.first().name

        name = self.DEFAULT

        models.Language.objects.create(
            name=name,
            title='Espanol',
            i18n='es',
            default=True
        )

        return name

    def get_by_name(self, name):
        """

        Get By Name

        Description
            Consulta un lenguaje por su nombre

        :return
            models.Language -- El lenguaje

        """
        main_languages = models.Language.objects.get_active(name=name)

        if main_languages.count() > 0:
            return main_languages.first()

        return None

    def get_language(self, request=None):
        """
        Get Default

        Description
            Permite obtener el lenguaje actualmente elegido en el sistema, lo obtiene
            de sesion. Si no esta en sesion aun, se toma el lenguaje por defecto y se lo
            registra en la sesion para una futura ocacion.

        :return
            models.Language -- El lenguaje principal del sistema

        """
        if request:
            return memory.manage(request).recover('dbu.languages.current', default_value=self.get_default())

        return self.get_default()


    def get_language_object(self, request):
        """
        Get Default

        Description
            Permite obtener el modelo lenguaje actualmente elegido en el sistema, lo obtiene
            de sesion. Si no esta en sesion aun, se toma el lenguaje por defecto y se lo
            registra en la sesion para una futura ocacion.

        :return
            String -- Abreviacion i18n

        """
        lang_name = self.get_language(request)
        languages = models.Language.objects.get_active(name = lang_name)

        if languages.exists():
            return languages.first()
        else:
            return self.create_language(lang_name)

    def change_language(self, request, name):
        """
        Change Language

        Description
            Permite realizar el cambio de lenguaje al indicado por el parametro 'name'

        :return
            Boolean -- True si el cambio fue realizado, False en caso contrario

        """
        languages = models.Language.objects.get_active(name = name)

        if languages.count() > 0:
            first = languages.first()
            memory.manage(request).store('dbu.languages.current', first.name)
            return True, first

        return False, None

    def create_language(self, name):
        """

        Create Language

        Description
            Crea lenguaje por defecto

        :param name:

        """
        try:
            return models.Language.objects.create(name = name, title = name)
        except Exception as e:
            languages = models.Language.objects.get_active(name = name)
            if languages.count() > 0:
                return languages.first()

            return None

languages = LanguageManager()