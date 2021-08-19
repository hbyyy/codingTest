# # from unittest.mock import Mock
# #
# #
# # class ProductionClass:
# #     pass
# #
# #
# # thing = ProductionClass()
# # thing.method = Mock(return_value=3)
# # print(thing.method(3, 4, 5, key="value"))
# #
# # thing.method.assert_called_with(3, 4, 5, key="value")
# #
# # mock = Mock(side_effect=KeyError('foo'))
# # mock()
# #
# # mock = Mock()
# # values = {"a": 1, "b": 2, "c": 3}
# #
# #
# # def side_effect(arg):
# #     return values[arg]
# #
# #
# # mock.side_effect = side_effect
# # print(mock("a"), mock("b"), mock("c"))
# #
# # mock.side_effect = [5, 4, 3, 2, 1]
# # print(mock(), mock(), mock())
# #
# from unittest.mock import Mock, MagicMock
#
# mock = Mock()
# mock.__str__ = Mock(return_value='test __str__')
# print(str(mock))
#
#
import unittest
from unittest.mock import patch, Mock

from funcc import a_func


class SampleTestCase(unittest.TestCase):
    @patch('funcc.a_func.inner_func', create=True)
    def test_call(self, mock_inner_func):
        a_func()
        mock_inner_func.assert_not_called()

