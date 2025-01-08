import pytest
from safe_calculator import SafeCalculator
from tests.authorizer import Authorizer

def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in
    # SafeCalculator.add
    authorizer = Authorizer()
    authorizer.set_authorized(True)

    calculator = SafeCalculator(authorizer)


    result = calculator.add(1, 1)
    assert result == 2, "Result should be 2"
    