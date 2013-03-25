EventManager
============

My take on a pythonic, and simple event system.
It does not have any dependencies, beyond of course python!


Usage and explanation
=====================
####Event: This class represents an event.

___Example usage:___
```python
e = Event()  # Create event object
e.add_handler(myfunction)  # Register handler
e()  # Fire event, this will call all handlers
e.fire()  # This also same as e()
```
        
___Other:___
If a handler raises `StopIterator()` the event will not execute the rest of the handlers.
To bypass checks simply use `e.append(myfunction)` instead.


####EventManager This class represents a list of events.

___Example usage:___

```python
em = EventManager()  # Create manager object.
em["myevent"] = Event()  # Add an empty event called "myevent".
em["myevent"].add_handler(myfunction)  # Add handler to an event.
em["myevent"]()  # Fire the event: "myevent".
em.myevent()  # You can also use '.' instead of [""], I prefer using '.'
```

___Other:___
Every `EventManager` comes with a global event hook, it fires every time it gets a request to fire an event.
It acts like any ol' `event`, and can be found under `EventManager.got_event`

Examples
========
I use it in my McClientLib project. [McClientLib](https://github.com/dkkline/McClientLib)
Add examples here, if you use this, please add a link to your code here!
