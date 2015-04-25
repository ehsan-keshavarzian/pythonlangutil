import inspect

def private_function(f):
    def inner_func(calling_obj, *args, **kwargs):
        stack = inspect.stack()
        local = stack[1][0].f_locals
        if "self" in local:
            class_name = local["self"].__class__.__name__
        elif "cls" in local:
            class_name = local["cls"].__name__
        else:
            class_name = None
        if class_name is None or class_name != calling_obj.__class__.__name__:
            raise Exception("Singleton class cannot be instantiated. Use get_instance method of the class.")
        return f(calling_obj, *args, **kwargs)            
    return inner_func

class Singleton(object):
    def __init__(self):
        pass
        
    def __call__(self, clas):
        class NewClass(clas):
            instance = None
            
            @private_function
            def __init__(self, *args, **kwargs):
                clas.__init__(self, *args, **kwargs)
                
            @classmethod
            def get_instance(cls):
                if cls.instance is None:
                    cls.instance = NewClass()
                return cls.instance
            
        return NewClass
    