__all__ = ("Event", "EventManager", "VERSION")
VERSION = ("0", "6")


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
        self.name = None

    def clear(self):
        """Clears list of handlers."""
        del self[:]

    def add_handler(self, handler):
        """Adds a handler. Also checks if it is callable."""
        if not hasattr(handler, "__call__"):  # Not callable
            raise TypeError("'%s' is not callable." % handler)

        self.append(handler)

    def remove_handler(self, handler):
        """Removes a handler."""
        self.remove(handler)

    def fire(self, *args, **kwargs):
        """Fires an event, thereby executing all it's handlers with given
        args and kwargs."""
        if self.eventmanager:
            # Fire global event. Assuming we have an eventmanager.
            self.eventmanager.got_event(self.name, *args, **kwargs)

        for handler in self:  # Iterate over handlers
            try:
                handler(*args, **kwargs)  # Execute handler with given args.
            except StopIteration:  # Stop iterating if handler raised StopIter
                break

    def __call__(self, *args, **kwargs):
        self.fire(*args, **kwargs)


class EventManager(dict):
    """Object for managing events, basicly acts like a dict."""
    def __init__(self, *args, **kwargs):
        super(EventManager, self).__init__(*args, **kwargs)
        self.got_event = Event()  # Setup out global event, this will
        # fire every time an event is fired.
        self.got_event.name = "GLOBAL"
        self.got_event.eventmanager = None  # To stop looping forever.

    def __setitem__(self, key, value):
        if isinstance(value, Event):  # If it is an event:
            value.name = key  # Set it's name.
            value.eventmanager = self  # Set it's eventmanager
        super(EventManager, self).__setitem__(key, value)

    def __getattr__(self, name):  # So we can use '.'
        return self[name]

    def __setattr__(self, name, value):  # So we can use '.'
        self[name] = value
