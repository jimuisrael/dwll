from django.test import TestCase

from dwll.languages import languages
from dwll import messages

from .fake_request import request

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
