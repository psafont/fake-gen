import sys


PY2 = sys.version_info[0] == 2

if PY2:
    def implements_iterator(cls):
        cls.next = cls.__next__
        del cls.__next__
        return cls
else:
    implements_iterator = lambda x: x


def with_metaclass(meta, *bases):
    """Create a class with a metaclass.

    Source: http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/

    """

    class metaclass(meta):
        __call__ = type.__call__
        __init__ = type.__init__

        def __new__(cls, name, this_bases, d):
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, bases, d)
    return metaclass('temporary_class', None, {})
