from functools import reduce


def ft_reduce(function_to_apply, list_of_inputs):
    result = list_of_inputs[0]
    for el in list_of_inputs[1::]:
        result = function_to_apply(result, el)
    return result


def do_sum(x1, x2): return x1 + x2


print(reduce(do_sum, [1, 2, 3, 4]))
print(ft_reduce(do_sum, [1, 2, 3, 4]))


def do_mul(x1, x2): return x1 * x2


print(reduce(do_mul, [1, 2, 3, 4]))
print(ft_reduce(do_mul, [1, 2, 3, 4]))
