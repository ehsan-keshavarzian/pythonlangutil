import inspect


def private_variable(*variables):
    def func(f):
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
                if args[0] in variables:
                    raise Exception("this variable is private")
            return f(calling_obj, *args, **kwargs)            
        return inner_func
    return func

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
            raise Exception("This function is private and cannot be called outside its own class")
        return f(calling_obj, *args, **kwargs)            
    return inner_func