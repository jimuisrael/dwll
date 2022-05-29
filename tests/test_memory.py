from dwll.memory import memory
from dwll.memory import topmemory

from .fake_request import request

import unittest

class TestLanguage(unittest.TestCase):

    def test_memory_storage(self):
        value = memory.manage(request).store("VARIABLE1", "VALUE1")
        self.assertEqual(value, "VALUE1")

        value = memory.manage(request).recover("VARIABLE1")
        self.assertEqual(value, "VALUE1")

        value = memory.manage(request).update("VARIABLE1", "VALUE2")
        self.assertEqual(value, "VALUE2")

        value = memory.manage(request).recover("VARIABLE1")
        self.assertEqual(value, "VALUE2")

        topmemory.top.clean_by_step(request)

        value = memory.manage(request).recover("VARIABLE1")
        self.assertEqual(value, None)

if __name__ == '__main__':
    unittest.main()