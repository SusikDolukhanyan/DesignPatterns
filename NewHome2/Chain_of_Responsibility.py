
class Handler:
    def __init__(self, successor=None):
        self.successor = successor  

    def handle(self, request):
        if self.successor:
            return self.successor.handle(request)
        return "Request not handled"


class InfoHandler(Handler):
    def handle(self, request):
        if request == "Info":
            return "InfoHandler: Handling info level request."
        return super().handle(request)

class WarningHandler(Handler):
    def handle(self, request):
        if request == "Warning":
            return "WarningHandler: Handling warning level request."
        return super().handle(request)

class ErrorHandler(Handler):
    def handle(self, request):
        if request == "Error":
            return "ErrorHandler: Handling error level request."
        return super().handle(request)


if __name__ == "__main__":
    error_handler = ErrorHandler()
    warning_handler = WarningHandler(successor=error_handler)
    info_handler = InfoHandler(successor=warning_handler)

    
    requests = ["Info", "Warning", "Error", "Unknown"]

    for req in requests:
        print(f"Request: {req} -> Response: {info_handler.handle(req)}")
