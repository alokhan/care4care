from django.test import TestCase

class SimpleTestCase(TestCase):
    def setUp(self):
        pass

    def test_1plus1(self):
        self.assertEqual(1+1, 2)
