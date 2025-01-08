class Authorizer:
    def __init__(self, is_authorized=True):
        self._is_authorized = is_authorized
    
    def authorize(self):
        return self._is_authorized
    
    def set_authorized(self, authorized):
        self._is_authorized = authorized