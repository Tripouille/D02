def ft_map(function_to_apply, list_of_inputs):
    return [function_to_apply(e) for e in list_of_inputs]


test = [1, 2, 3, 4, 5]
print(*map(lambda x: x * 2, test))
print(*ft_map(lambda x: x * 2, test))
