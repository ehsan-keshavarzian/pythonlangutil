

def signature(*types):
    def func(f):
        def inner_func(callingObj, *args, **kwargs):
            return f(callingObj, *args, **kwargs)
        inner_func.signature = types
        return inner_func
    return func
        
class Overload(object):
    def __init__(self, func):
        self.owner = None
        self.signatures = []
        self.methods = []
        self.methods.append(func)
        self.signatures.append(func.signature)
        
    def __get__(self, owner, ownerType=None):
        self.owner = owner or self
        return self
    
    def __call__(self, *args, **kwargs):
        signature = []
        for arg in args:
            signature.append(arg.__class__.__name__)
        for _, v in kwargs:
            signature.append(v.__class__.__name__)
        signature = tuple(signature)
        if signature in self.signatures:
            index = self.signatures.index(signature)
        else:
            raise Exception("There is no overload for this method with this signature.")
        return self.methods[index](self.owner, *args, **kwargs)
    
    def overload(self, func):
        self.methods.append(func)
        self.signatures.append(func.signature)
        return self
        
    