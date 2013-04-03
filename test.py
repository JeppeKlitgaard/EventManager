import unittest
from EventManager import EventManager, Event


class TestError(NotImplementedError):
    pass


test_event = Event()


def test_func_error():
    raise TestError()


def test_func():
    pass


def test_func_stop():
    raise StopIteration


def test_func_global(name):
    raise TestError()


class TestEvents(object):
    @staticmethod
    def test():
        raise TestError()


class EventTest(unittest.TestCase):
    def test_creation(self):
        Event()

    def test_creation_args(self):
        e = Event(test_func)
        self.assertIn(test_func, e)

    def test_clear(self):
        e = Event(test_func)
        e.clear()
        self.assertEqual(len(e), 0)

    def test_add_handler(self):
        e = Event()
        e.add_handler(test_func)
        self.assertIn(test_func, e)

    def test_add_handler_invalid(self):
        e = Event()

        with self.assertRaises(TypeError):
            e.add_handler("NotCallable")

    def test_remove_handler(self):
        e = Event()
        e.add_handler(test_func)
        e.remove_handler(test_func)
        self.assertNotIn(test_func, e)

    def test_fire(self):
        e = Event()
        e.add_handler(test_func_error)

        with self.assertRaises(TestError):
            e()

    def test_fire_stop(self):
        e = Event()
        e.add_handler(test_func_stop)
        e.add_handler(test_func_error)


class EventManagerTest(unittest.TestCase):
    def test_creation(self):
        EventManager()

    def test_creation_kwargs(self):
        em = EventManager(test=test_event)
        self.assertEqual(em.test, test_event)

    def test_fire_global(self):
        em = EventManager()
        em.test = Event(test_func)
        em.got_event.add_handler(test_func_global)

        with self.assertRaises(TestError):
            em.test()

    def test_apply(self):
        em = EventManager()
        events = TestEvents()
        em.apply(events)

        with self.assertRaises(TestError):
            em.test()


if __name__ == "__main__":
    unittest.main()
