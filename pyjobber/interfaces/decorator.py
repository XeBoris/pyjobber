
CallCollector = []
ClassCollector = {}


class Collector():
    def __init__(self, handover):
        if handover.__name__ not in CallCollector:
            CallCollector.append(handover.__name__)
            ClassCollector[str(handover.__name__)] = handover.__call__()

    def __call__(self, *args, **kwargs):
        pass
