from fake_gen.base import Factory
from fake_gen.childrentree import ChildrenTree

class DictFactoryBuilder(type):
    """
    A metaclass that builds DictFactory based classes.
    """
    def __new__(meta, name, bases, dct):
        _child_factory_tree = ChildrenTree()
        _child_factory_tree.load_bases(bases)
        _child_factory_tree.update(dct)
        DictFactoryBuilder._clean_factories(dct)
        dct["_child_factory_tree"] = _child_factory_tree
        return super(DictFactoryBuilder, meta).__new__(meta, name, bases, dct)

    @staticmethod
    def _clean_factories(dct):
        """
        After we create the children factory, we don't need it anymore
        """
        keys = []
        for key in dct.keys():
            if issubclass(type(dct[key]), Factory):
                # avoid change dict in loop
                keys.append(key)
        for key in keys:
            dct.pop(key)
