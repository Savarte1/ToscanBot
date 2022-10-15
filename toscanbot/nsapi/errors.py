class NSApiError(Exception):
    pass


class NoAgentError(NSApiError):
    pass


class NSConnectError(NSApiError):
    pass