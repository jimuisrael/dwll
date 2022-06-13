from django.test import TestCase

from dwll.languages import languages
from dwll import messages
from dwll import configuration
from dwll import models
from dwll import mixins
from dwll.admins import modeladmin

from .fake_request import request

import datetime


class LanguageTestCase(TestCase):
    
    def test_default_language(self):
        language = languages.get_default()
        self.assertEqual(language, 'spanish')

        language = languages.get_by_name('spanish')
        self.assertEqual(language.id,1)

    def test_get_change_language(self):
        language = languages.get_language(request)
        self.assertEqual(language, 'spanish')

        success, language = languages.change_language(request, 'spanish')
        self.assertTrue(success)
        self.assertEqual(language.name, 'spanish')

        success, language = languages.change_language(request, 'english')
        self.assertFalse(success)
        self.assertEqual(language, None)

class MessageTestCase(TestCase):

    def test_get_message(self):
        value = messages.get_message(name='do.com.welcome', default='Bienvenido')
        self.assertEqual(value, 'Bienvenido')

        language = languages.create_language('english')
        self.assertEqual(language.name, 'english')

        value = messages.get_message(name='do.com.welcome', language=language, default='Welcome')
        self.assertEqual(value, 'Welcome')

        language = languages.get_by_name('spanish')
        self.assertEqual(language.name, 'spanish')

        value = messages.get_message(name='do.com.welcome', language=language)
        self.assertEqual(value, 'Bienvenido')

class MessageTestCase(TestCase):

    def test_get_value(self):
        self.assertEqual(configuration.get_value('com.myconfig.value', default='101'), '101')
        self.assertEqual(configuration.get_float('com.myconfig.decimal', default='101.22'), 101.22)
        self.assertEqual(configuration.get_integer('com.myconfig.integer', default='101'), 101)
        self.assertTrue(configuration.isTESTMode())

class ModelMixins(TestCase):

    def test_models(self):
        language = models.Language()
        language.save(request=request)
        
        self.assertEqual(language.creation_user, 'admin')
        self.assertEqual(language.creation_date.date(), datetime.date.today())

        last_modification = language.modification_date

        language.name = 'french'
        language.save()

        self.assertNotEqual(language.modification_date, last_modification)

        self.assertTrue(language.is_enabled())

        language.disable()

        self.assertFalse(language.is_enabled())

        actives = models.Language.objects.get_active()

        self.assertTrue(actives.count() == 0)

        class MyModel(mixins.AuditMixinCode):
            pass
            
        mymodel = MyModel()
        self.assertTrue(len(mymodel.generate_unique_id_12()) == 12)

        # Templatetag for messages simulation
        language = languages.get_language(request)
        msg = messages.get_message('message.title', language)
        self.assertEqual(msg, 'message.title')
