from mock import Mock
import error_handler
from unittest.mock import patch
from unittest import TestCase

class TestErrorHandler(TestCase):
    def test_no_error(self):
        func = Mock()
        decorated_func = error_handler.error_handling(func)
        decorated_func(10)
        assert not func.called
        # assert response is redirect

    def test_has_error(self):
        expected = 'foo'
        func = Mock(side_effect=TypeError(expected))
        decorated_func = error_handler.error_handling(func)
        wrapped_mock = decorated_func(func)
        with patch.object(error_handler, 'send_message') as mock_error_handler:
            try:
                wrapped_mock(10)
            except TypeError as e:
                mock_error_handler.assert_called_once_with(message=f'Error Raised {expected}')
            finally:
                mock_error_handler.stop()
=