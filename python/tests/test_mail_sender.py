from tests.httpclient import HttpClient
from mail_sender import MailSender
from user import User
from mail_sender import SendMailRequest
from unittest.mock import Mock

def test_send_v1():
    http_client = HttpClient()
    mail_sender = MailSender(http_client)
    user = User(name="user0", email="user1@example.com")
    message = "New notification"
    mail_sender.send_v1(user, message)
    expected_request = SendMailRequest(user.email, "New notification", message)

    assert http_client.was_sent(mail_sender.base_url, expected_request), "Email should have been sent"

def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    pass

def test_send_v1_with_mock():
    mock_http_client = Mock()
    mail_sender = MailSender(mock_http_client)
    user = User(name="user0", email="user1@example.com")
    message = "New notification"
    mail_sender.send_v1(user, message)
    expected_request = SendMailRequest(user.email, "New notification", message)
    
    # Verify the HTTP client was called correctly
    mock_http_client.post.assert_called_once_with(mail_sender.base_url, expected_request)