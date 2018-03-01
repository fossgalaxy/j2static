# Fake test case to check that tox works

import unittest
import j2static.main


class TestDiscoveryDefaults(unittest.TestCase):

    def setUp(self):
        self.engine = j2static.main.TemplateEngine()

    def test_abstract(self):
        result = self.engine.is_abstract('_base.html')
        return self.assertEqual(result, True)

    def test_abstract_dir(self):
        result = self.engine.is_abstract("/tmp/_base.html")
        return self.assertEqual(result, True)

    def test_abstract_not(self):
        result = self.engine.is_abstract("base.html")
        return self.assertEqual(result, False)

    def test_abstract_not_dir(self):
        result = self.engine.is_abstract("/tmp/base.html")
        return self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
