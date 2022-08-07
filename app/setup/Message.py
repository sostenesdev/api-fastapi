class Message():
    def __init__(self, data = None, success=True, message="", errors=[]):
        self.data = data
        self.success = success
        self.message = message
        errors = errors