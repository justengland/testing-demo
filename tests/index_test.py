import json
from test.support import EnvironmentVarGuard
import unittest
from index import foo


class InspectorCompletionHandlerTest(unittest.TestCase):
    # npm test -- tests.inspector_completion_handler_test.CompletionHandlerTestCase
    # npm run debug
    # python3 -m nose -v -w tests tests.inspector_completion_handler_test.InspectorCompletionHandlerTest
    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('VAR', 'value')

    def test_foo_valid(self):
        self.assertEqual(foo(9), 9)

    def test_foo_cause_error(self):
        with self.assertRaises(ValueError):
            foo(0)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

