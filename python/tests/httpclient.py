class HttpClient :
    def __init__(self):
        # Initialize an empty list to store emails
        self.emails = []

    def post(self, url, request):
        print(f"Sending email to {request.recipient} with subject {request.subject} and body {request.body} at {url}")
        # Store the request
        self.emails.append((url, request))

    def was_sent(self, url, request):
        # Check if request  exists in any emails tuple
        return any(url == email[0] and request == email[1] for email in self.emails)