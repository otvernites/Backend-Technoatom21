class CustomMeta(type):
    '''
    def __new__(mcs, name, bases, classdict):
        mcs.clsdict = classdict
        newattributes = {}
        for attrname, attrvalue in classdict.items():
            if re.match(r'__.*__', attrname):
                newattributes[attrname] = attrvalue
            else:
                newattributes["custom_" + attrname] = attrvalue
        return super().__new__(mcs, name, bases, newattributes)
    '''

    def __call__(cls):
        obj = super(CustomMeta, cls).__call__()
        methods = filter(lambda a: not a.startswith('__'), dir(obj))

        for elem in methods:
            setattr(obj, "custom_" + elem, getattr(obj, elem))
            try:
                delattr(obj, elem)
            except AttributeError:
                delattr(cls, elem)
        return obj


class CustomClass(metaclass=CustomMeta):
    x = 50
    str = "hello"
    val = -1

    def __init__(self, val=99):
        self.val = val
        self.item = 10

    def __set__(self, item=0, val=-2):
        self.item = item
        self.val = val

    @classmethod
    def line(cls):
        return 100

    @classmethod
    def size(cls):
        return 10, 1
