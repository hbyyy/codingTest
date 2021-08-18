import unittest


class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        with self.assertRaises(TypeError):
            s.split(2)


class WidgetTestCase(unittest.TestCase):
    def setUp(self) -> None:
        class Widget:
            def __init__(self, text):
                self.text = text
                self._size = (50, 50)

            def size(self):
                return self._size

            def resize(self, x, y):
                self._size = (x, y)

        self.widget = Widget("the Widget")

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), "incorrect default size")

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), "wrong size after resize")


@unittest.skip("")
class MyTestCase(unittest.TestCase):
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_nothing2(self):
        self.fail("shouldn't happen22")
