__all__ = ("Event", "EventManager", "VERSION")
VERSION = ("0", "3")


class Event(list):
    """This objects represents an event.
    It simply iterates thru a list of handlers once it's fired.

    If a handler raises StopIteration,
    it will not fire the rest of the handlers.

    Supports list methods, and the following:


    Event.clear() -> Clears list of handlers.

    Event.add_handler(handler) -> Adds a handler.
        Same as Event.append(handler), except it checks if the handler is sane.

    Event.remove_handler(handler) -> Removes a handler.
        Same as Event.remove(handler)

    Event.fire(*args, **kwargs) -> Fires event, by iterating thru handlers.
        Executing each handler with *args and **kwargs.

    Event(*args, **kwargs) -> Same as Event.fire(*args, **kwargs)

    Event.eventmanager => The EventManager for event.
    """
    def __init__(self, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        self.eventmanager = None
        self.names = set()

    def clear(self):
        del self[:]
        return True

    def add_handler(self, handler):
        if not hasattr(handler, "__call__"):
            raise TypeError("'%s' is not callable." % handler)

        self.append(handler)

    def remove_handler(self, handler):
        self.remove(handler)

    def fire(self, *args, **kwargs):
        if self.eventmanager:
            self.eventmanager.got_event(self.names, *args, **kwargs)

        for handler in self:
            try:
                handler(*args, **kwargs)
            except StopIteration:
                break

    def __call__(self, *args, **kwargs):
        self.fire(*args, **kwargs)


class EventManager(dict):
    """Object for managing events, basicly acts like a dict."""
    def __init__(self, *args, **kwargs):
        super(EventManager, self).__init__(*args, **kwargs)
        self.got_event = Event()

    def __setitem__(self, key, value):
        if not isinstance(value, Event):
            raise TypeError("'%s<%s>' is not an Event." % (key, value))

        super(EventManager, self).__setitem__(key, value)
        self[key].eventmanager = self

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value
