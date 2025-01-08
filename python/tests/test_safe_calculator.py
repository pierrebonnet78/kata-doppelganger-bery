import pytest
from safe_calculator import SafeCalculator
from tests.authorizer import Authorizer
from unittest.mock import Mock

def test_divide_should_not_raise_any_error_when_authorized():
    authorizer = Authorizer()
    authorizer.set_authorized(True)

    calculator = SafeCalculator(authorizer)
    result = calculator.add(1, 1)

    assert result == 2, "Result should be 2"

def test_divide_with_mock_authorizer():
    mock_authorizer = Mock()
    mock_authorizer.is_authorized.return_value = True

    calculator = SafeCalculator(mock_authorizer)
    result = calculator.add(1, 1)
    
    assert result == 2, "Result should be 2"
    