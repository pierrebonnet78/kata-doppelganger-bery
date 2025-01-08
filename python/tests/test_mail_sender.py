from tests.httpclient import HttpClient
from mail_sender import MailSender
from user import User
from mail_sender import SendMailRequest

def test_send_v1():
    http_client = HttpClient()
    mail_sender = MailSender(http_client)
    user = User(name="user0", email="user1@example.com")
    message = "New notification"
    mail_sender.send_v1(user, message)
    request = SendMailRequest(user.email, "New notification", message)

    assert http_client.was_sent(mail_sender.base_url, request), "Email should have been sent"

def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    pass
