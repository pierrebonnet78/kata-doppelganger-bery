from discount_applier import DiscountApplier
from tests.notifier import Notifier
from user import User

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

