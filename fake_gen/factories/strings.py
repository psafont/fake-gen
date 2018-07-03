import random
import string
from fake_gen.base import Factory


class RandomLengthStringFactory(Factory):
    """
    Generates random strings between 2 lengths

    :param min_chars: minimum amount of characters
    :param max_chars: maximum amount of characters
    :param prefix: string that must be present before the random characters
    :param suffix: string that must be present after the random characters

    Examples,
    >>> all(len(chars) == 5 for chars in RandomLengthStringFactory(5, 5).generate(200))
    True
    """
    MIN_CHAR_DEFAULT = 3
    MAX_CHAR_DEFAULT = 100

    def __init__(self, min_chars=None, max_chars=None, prefix=None, suffix=None):
        super(RandomLengthStringFactory, self).__init__()

        if not isinstance(min_chars, int):
            raise TypeError("min_chars needs to be an integer")
        if not isinstance(max_chars, int):
            raise TypeError("max_chars needs to be an integer")

        self._min_chars = min_chars if min_chars else self.MIN_CHAR_DEFAULT
        self._max_chars = max_chars if max_chars else self.MAX_CHAR_DEFAULT
        self._prefix = prefix if prefix else ''
        self._suffix = suffix if suffix else ''

    def __call__(self):
        length = random.randint(self._min_chars, self._max_chars)
        random_parts = [self._prefix]
        random_parts += [random.choice(string.ascii_letters) for _ in range(length)]
        random_parts += [self._suffix]

        return ''.join(random_parts)

class HashHexDigestFactory(Factory):
    """
    Returns on each iteration the result of the hash `hash_class`.hexdigest(), generated
    from the pseudo random string.

    :param hash_class: Any hash class from the hashlib package, like hashlib.md5
    :param element_amount: The amount of values that will be generated

    Examples,
    >> for i in HashHexDigestFactory(hashlib.md5).generate(3):
    ..      print(i)
    aaaa6305d730ca70eae904ca47e427c8
    d172baa4019279f3f78a624f2a0b3e2b
    78cd377dc9421cd4252d8110f9acb7c4

    >> for i in HashHexDigestFactory(hashlib.sha224).generate(3):
    ..      print(i)
    8dfd75184b6b5f9be73050dc084a8a3ebcf4c45fc5ca334df911c7c5
    ee1822b3cd7f58eb81bd37b7e5933d73a62578a2c060e7e4808569d0
    3c2ecb8fd519795f77620614ed5b45ccd611a12aa9d355683ac791d9
    """

    _MAX_VALUE_LENGTH = 100
    _MIN_VALUE_LENGTH = 3

    def __init__(self, hash_class):
        super(HashHexDigestFactory, self).__init__()
        self._hash_class = hash_class

    def __call__(self):
        length = random.randint(self._MIN_VALUE_LENGTH, self._MAX_VALUE_LENGTH)
        random_string = u''.join([random.choice(string.ascii_letters) for _ in range(length)])
        return self._hash_class(random_string.encode()).hexdigest()
