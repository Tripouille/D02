def what_are_the_vars(*args, **kwargs):
    result = ObjectC()
    for i, a in enumerate(args):
        setattr(result, "var_" + str(i), a)
    for k, v in kwargs.items():
        if hasattr(result, k):
            return None
        setattr(result, k, v)
    return result


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)

# var_0: 7
# end
# var_0: ft_lol
# var_1: Hi
# end
# end
# a: 10
# hello: world
# var_0: 12
# var_1: Yes
# var_2: [0, 0, 0]
# end
# ERROR
# end
