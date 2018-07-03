import math
import random
from fake_gen.base import Factory
from fake_gen.errors import InvalidDistribution
from fake_gen.factories.generic import Constant

class DistributionFactory(Factory):
    """
    Returns values from a factory depending on a discrete distribution.
    :param distribution: an iterator of 2-item tuples. Each tuple must contain
        a constant or a factory as the first value and a probability in % as
        the second.
    Note:
    The sum of all percentages should be 100.

    Examples,
    >>> import fake_gen
    >>> percentages = [50, 50]
    >>> ok = zip([fake_gen.Constant('foo'), 'bar'], percentages)
    >>> f = [i for i in DistributionFactory(ok).generate(4)]
    >>> f.count('foo')
    2
    >>> f.count('bar')
    2
    >>> percentages = [50, 80]
    >>> wrong = zip(['foo', 'bar'], percentages)
    >>> f = [i for i in DistributionFactory(wrong).generate(4)] # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
     ...
    InvalidDistribution: Need a total of a 100% probability. Got 70% instead
    """
    def __init__(self, distribution):
        super(DistributionFactory, self).__init__()

        probability = sum(prob for _, prob in distribution)
        if probability != 100:
            raise InvalidDistribution(
                "A distribution must have a total of a 100% probability. Got {}% instead"
                .format(probability))

        def facto(value):
            return value if isinstance(value, Factory) else Constant(value)

        self._distribution = [(facto(value), probability) for (value, probability) in distribution]

    def set_element_amount(self, element_amount):
        super(DistributionFactory, self).set_element_amount(element_amount)
        for index, (factory, probability) in enumerate(self._distribution):
            amount = int(math.ceil(element_amount * (probability / 100.0)))
            factory.set_element_amount(amount)
            self._distribution[index] = factory, amount

    def __call__(self):
        index, chance = random.choice(list(enumerate(self._distribution)))
        factory, amount = chance
        amount -= 1
        if amount == 0:
            self._distribution.remove(chance)
        else:
            self._distribution[index] = factory, amount
        return factory()
