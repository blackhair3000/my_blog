import unittest
import threading

threading.Thread


class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertEqual(True, False)


import threading

try:
    from synchronize import make_synchronized
except ImportError:
    def make_synchronized(func):
        import threading
        func.__lock__ = threading.Lock()

        def synced_func(*args, **kws):
            with func.__lock__:
                return func(*args, **kws)

        return synced_func


class Singleton(object):
    instance = None

    @make_synchronized
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self.blog = "xiaorui.cc"

    def go(self):
        pass


def worker():
    e = Singleton()
    print(id(e))
    e.go()


def test():
    e1 = Singleton()
    e2 = Singleton()
    e1.blog = 123
    print(e1.blog) # 123
    print (e2.blog)  # 123
    print (id(e1))
    print (id(e2))


if __name__ == "__main__":
    test()
    task = []
    for one in range(30):
        t = threading.Thread(target=worker)
        t.join()
        task.append(t)

    for one in task:
        one.start()

    for one in task:
        one.join()
# if __name__ == '__main__':
#     unittest.main()
