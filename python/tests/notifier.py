class Notifier:
    def __init__(self):
        # Initialize an empty list to store notifications
        self.notifications = []

    def notify(self, user, message):
        print(f"Sending notification to {user}: {message}")
        # Store the notification
        self.notifications.append((user, message))

    def was_notified(self, user):
        # Check if user exists in any notification tuple
        return any(user == notif[0] for notif in self.notifications)