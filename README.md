EventManager
============

My take on a pythonic, and simple event system.


Usage and explanation
=====================
####Event: This class represents an event.

___Example usage:___
```python
e = Event()  # Create event object
e += myfunction  # Register handler
e()  # Fire event, this will call all handlers
```
        
___Other:___
If a handler raises `StopIterator()` the event will not execute the rest of the handlers.
To bypass checks simply use `e.handlers.append(myfunction)` instead.


####EventManager This calss represents a list of events.

___Example usage:___

```python
em = EventManager()  # Create manager object.
em += "myevent"  # Add an empty event called "myevent".
em.myevent += myfunction  # Add handler to an event.
em.myevent()  # Fire the event: "myevent".
```

Examples
========
Add examples here, if you use this, please add a link to your code here!
