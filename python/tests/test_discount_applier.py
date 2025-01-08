from discount_applier import DiscountApplier
from tests.notifier import Notifier
from user import User
from unittest.mock import Mock

def test_apply_v1():
    notifier = Notifier()
    users = [
        User(name="user0", email="user1@example.com"),
        User(name="user1", email="user2@example.com"),
        User(name="user2", email="user3@example.com")
    ]
    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v1(10, users)

    for i, user in enumerate(users):
        assert notifier.was_notified(user), f"User {i} should have been notified"

def test_apply_v2():
    notifier = Notifier()
    users = [
        User(name="user0", email="user1@example.com"),
        User(name="user1", email="user2@example.com"),
        User(name="user2", email="user3@example.com")
    ]
    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v2(10, users)

    for i, user in enumerate(users):
        assert notifier.was_notified(user), f"User {i} should have been notified"

def test_apply_v1_with_mock():
    mock_notifier = Mock()
    
    users = [
        User(name="user0", email="user1@example.com"),
        User(name="user1", email="user2@example.com"),
        User(name="user2", email="user3@example.com")
    ]
    
    discount_applier = DiscountApplier(mock_notifier)
    discount_applier.apply_v1(10, users)

    assert mock_notifier.notify.call_count == 3
    for user in users:
        mock_notifier.notify.assert_any_call(user, "You've got a new discount of 10%")

def test_apply_v2_with_mock():
    mock_notifier = Mock()
    
    users = [
        User(name="user0", email="user1@example.com"),
        User(name="user1", email="user2@example.com"),
        User(name="user2", email="user3@example.com")
    ]
    
    discount_applier = DiscountApplier(mock_notifier)
    discount_applier.apply_v2(10, users)

    assert mock_notifier.notify.call_count == 3
    for user in users:
        mock_notifier.notify.assert_any_call(user, "You've got a new discount of 10%")