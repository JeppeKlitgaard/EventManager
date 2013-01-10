class EventManager(object):
    """Represents a list of events.

    Example usage:
        ``
        em = EventManager()  # Create manager object.
        em += "myevent"  # Add an empty event called "myevent".
        em.myevent += myfunction  # Add handler to an event.
        em.myevent()  # Fire the event: "myevent".``

    See also: Event"""
    def __init__(self):
        self.events = {}

    def __check(self, name):
        if not isinstance(name, str):
            raise TypeError("'%s' is not a string." % name)
        else:
            return True

    def __iadd__(self, name):
        if self.__check(name):
            self.events[name] = Event()
        return self

    def __isub__(self, name):
        del self.events[name]
        return self

    def __getattr__(self, attr):
        try:
            return self.events[attr]
        except KeyError:
            raise AttributeError("Could not find event: '%s'" % attr)

    def __repr__(self):
        return "EventManager(%s)" % self.events.__repr__()


class Event(object):
    """Represents an event.
    To stop further handlers to be executed, simply raise StopIteration.

    Example usage:
        ``
        e = Event()  # Create event object
        e += myfunction  # Register handler
        e()  # Fire event, this will call all handlers``

        if a handler raises StopIterator() the event will not execute the
        rest of the handlers.

        To bypass checks simply use e.handlers.append(myfunction) instead."""
    def __init__(self):
        self.handlers = []

    def __check(self, handler):
        """Checks if the handler is sane (You never know these days!)."""
        if not hasattr(handler, "__call__"):
            raise TypeError("'%s' is not callable." % handler)
        else:
            return True

    def __iadd__(self, handler):
        if self.__check(handler):
            self.handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.handlers.remove(handler)
        return self

    def __call__(self, *args, **kwargs):
        for handler in self.handlers:
            try:
                handler(*args, **kwargs)
            except StopIteration:
                break

    def __repr__(self):
        return "Event(%s)" % self.handlers.__repr__()