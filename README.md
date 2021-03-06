[![tests](https://travis-ci.com/psafont/fake-gen.svg?branch=master)](https://travis-ci.com/psafont/fake-gen)
[![coverage](https://codecov.io/gh/psafont/fake-gen/branch/master/graph/badge.svg)](https://codecov.io/gh/psafont/fake-gen)


fake-gen
===============

A simple package that generates data for tests.

fake_gen provides the basic Factory and DictFactory classes that generate content.
it also provides many more specialized factories that provide extended functionality.
every Factory instance knows how many elements its going to generate, this enables us to generate statistical results.

The DictFactory is especially useful if you want to generate data that you will later input to your NoSQL, Document based
database

In addition, using the DictFactory and the DependentField factories allows us to create factorys that depend on the results
of other factories. (see Examples for more information).

fake_gen isn't bound to a specifc database, but does include database specfic modules inside, like - extra.mongodb.py)
but it will always be clean of database related dependencies.

## Installation

    pip install fake-gen

## Examples
We integrate the awsome faker package to generate data using FakeDataFactory,
this allows us to generate all sorts of content like:
    * Names (First, last, full names)
    * companies
    * addresses
    * emails
    * urls
    * and much much more

lets create a very simple factory that generates Users:

```python
import fake_gen

class Users(fake_gen.DictFactory):
    id = fake_gen.CountingFactory(10)
    firstname = fake_gen.FakeDataFactory('firstName')
    lastname = fake_gen.FakeDataFactory('lastName')
    address = fake_gen.FakeDataFactory('address')
    age = fake_gen.RandomInteger(10, 30)
    gender = fake_gen.RandomSelection(['female', 'male'])

for user in Users().generate(10): # let say we only want 10 users
    print user
    # {'firstname': 'Toni', 'lastname': 'Schaden', 'gender': 'female', 'age': 18, 'address': '0641 Homenick Hills\nSouth Branson, RI 70388', 'id': 10}
    # {'firstname': 'Gene', 'lastname': 'Greenfelder', 'gender': 'male', 'age': 17, 'address': '292 Loy Lights Suite 328\nFritzfort, IN 73914', 'id': 11}
    # or more likely you'd want to insert them into your favorite database (MongoDB, ElasticSearch, ..)
```

When creating our own subclasses for DictFactory, we can make some fields dependent on other fields.
for example:

```python
class ExampleFactory(DictFactory):
    a = CountingFactory(10)
    b = ClonedField("a") # b will have the same value as field 'a'

for e in ExampleFactory().generate(100):
    print e

# {'a': 10, 'b': 10}
# {'a': 11, 'b': 11}
# ...
```

Lets say we want to generate something like events data, we want events to have
a start time, and an end time that will be 20 minutes in the future.
In addition, we want the event's start_time will be 12 minutes apart.

```python
import fake_gen

EVENT_TYPES = ["USER_DISCONNECT", "USER_CONNECTED", "USER_LOGIN", "USER_LOGOUT"]
class EventsFactory(fake_gen.DictFactory):
    start_time = fake_gen.DateIntervalFactory(datetime.datetime.now(), datetime.timedelta(minutes=12))
    end_time = fake_gen.RelativeToDatetimeField("start_time", datetime.timedelta(minutes=20))
    event_code = fake_gen.RandomSelection(EVENT_TYPES)

for event in EventFactory().generate(100):
    print event
    # {'start_time': datetime.datetime(2013, 12, 23, 13, 37, 1, 591878), 'end_time': datetime.datetime(2013, 12, 23, 13, 57, 1, 591878), 'event_code': 'USER_CONNECTED'}
    # {'start_time': datetime.datetime(2013, 12, 23, 13, 49, 1, 591878), 'end_time': datetime.datetime(2013, 12, 23, 14, 9, 1, 591878), 'event_code': 'USER_LOGIN'}
    # {'start_time': datetime.datetime(2013, 12, 23, 14, 1, 1, 591878), 'end_time': datetime.datetime(2013, 12, 23, 14, 21, 1, 591878), 'event_code': 'USER_DISCONNECT'}
```

We also have factories that allow us to generate different data distributed by different percentage, for example,
lets say we want to create a 'Job', that will have an assigned user field, a state field and a description field.
We want the state to be 'pending' in 90% of dictionaries and 'error' in the rest of them. In addition, we want that if the 'state' field is
'error' the assigned user will be 'support', or else it should be 'admin'.

```python
class Job(fake_gen.DictFactory):
    state = fake_gen.StatisticalValuesFactory([('pending', 90), ('error', 10)])
    assigned_user = fake_gen.ConditionalValueField('state', {'error': 'support'}, 'admin')
    description = fake_gen.RandomLengthStringFactory()

for i in Job().generate(10):
    print i
    # {'state': 'error', 'assigned_user': 'support', 'description': 'jUlyFByPxPdFlBPBfPaGaTPPuajFSHXKkyewzrQ'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'tOzkgmBBnxQZhSYEjVduyXGdLrtqeTZqRxmHNXbaJBfpdNxuLKWyTDxkCZgiZTLHeiKEswvIyDzAnuuOLtXmVWhjvazaOYuu'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'TIDVuvZRUBLLTtG'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'RgcSaFzmMrhwCAZjLofikmXJhtqkVOTsWHnqTXjgrxgzTKH'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'tLkSEkCbYDvlcDBDWUBGMmidEdOxeiLDBADDKnqGqWLnxUBqzOXFXnBxkiGTymuGNbUnmxyawzLGsiummCiwxNSw'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'tUyYLofuZpceaWYKkiRvksQLqFHGOiwACuPIvRxMIuftJPsObSqCBcrQnOkOhqAukfMwrY'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'JbFrUxrERMObfwhEtCQGcxEbimvoTFwJriSfRFLFkBpyemqEfqUCGKmVlgSlVoZrrnetEnLCgbfobFbTMQOZ'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'lqatAwdcQuMMOPiYdVMRyyQgEIzOlcoozijjdCfXsVoZnnTtQjPSGBFZQGSkPblJrTIYLAotiZoyYRFrlncevwuNcqfOmeXeCPD'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'VYxnhydWtIUFiOEPszVQHuxYBIUGDyAefZiPIgkWHCMmophiueXbixXtdwKQkuvWImuErMOOOcwevQHGApXkolhjAq'}
    # {'state': 'pending', 'assigned_user': 'admin', 'description': 'RcawgTkQggchdHppSyQxnbDdNxqkGqbQWnQMSlorqnAQLdAqyWnKtGpXaZuVdxcGQBImzVPQsYAbIFUIpqvDzwTDdRpleBrc'}
```

In version 1.0.5 we extended the DictFactory to support passing additional factories, or overriding existing factories, for a specific instance.
Lets take for example our 'User' example from the begining.

```python
import fake_gen
class Users(fake_gen.DictFactory):
    id = fake_gen.CountingFactory(10)
    firstname = fake_gen.FakeDataFactory('firstName')
    lastname = fake_gen.FakeDataFactory('lastName')
    address = fake_gen.FakeDataFactory('address')
    age = fake_gen.RandomInteger(10, 30)
    gender = fake_gen.RandomSelection(['female', 'male'])
```
But lets override it so the 'firstname' always returns John, and make the age be a random integer between 40 and 60 and add an 'email' field.

```python
for user in Users(firstname=fake_gen.Constant('John'), age=fake_gen.RandomInteger(40, 60), email=fake_gen.FakeDataFactory('email')).generate(10): # let say we only want 10 users
    print user
    #{'firstname': 'John', 'gender': 'male', 'age': 54, 'email': 'hazle.wehner@brekke.com', 'lastname': 'Willms', 'address': '245 Pfeffer Light Apt. 309\nEast Audieside, IN 11931', 'id': 10}
    #{'firstname': 'John', 'gender': 'male', 'age': 47, 'email': 'mariam25@gmail.com', 'lastname': 'Ratke', 'address': '98710 Freddy Gateway\nDelilahborough, GU 50849', 'id': 11}
    #{'firstname': 'John', 'gender': 'male', 'age': 55, 'email': 'tyler22@yahoo.com', 'lastname': 'Cormier', 'address': '432 Block Locks Apt. 547\nNew Estel, NJ 54026', 'id': 12}
    # or more likely you'd want to insert them into your favorite database (MongoDB, ElasticSearch, ..)
```

## Factories
See the Factorie's Docstrings for more examples and doctests.

#### Bases
|Factory Class| Description|
|:-------|:-----------|
| Factory | The base class of all the factories.|
| DictFactory | A very powerful base class. allows sub classing to create factories that generate dicts with a specific schema (see [Examples][#Examples]). |
| ListFactory | A factory that returns on each iteration a list of `elements_per_list` items returned from calls to the given factory. |
| Callable | Gets a callable object as an argument and returns the result of calling the object on every iteration |
| DependentCallable | Gets a callable object as an argument and returns the result of calling the object passing the defined fields as arguments on every iteration |
| ClonedField | A factory that copies the value of another factory. |
#### Dates
|Factory Class| Description|
|:-------|:-----------|
| RandomDateFactory | Generates random dates (python's datetime) between 2 dates|
| DateIntervalFactory | Generates datetime objects starting from `base` while adding  `delta` to it each iteration.
| RelativeToDatetimeField | Generates datetime object relative to another datetime field, like if you have `start_time` which is a RandomDateFactory field, and want an `end_time` field that is always 15 minutes later.|

And MUCH MUCH more..

## Todos
* Add usage documentation for each factory (using doctest maybe?)
* Add more tests
* Add GeoLocationFactories to generates Location and distance related data (for example, random points near a central point).
* Add MORE Statistical Factories
* more ideas welcome!
