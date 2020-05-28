def ft_filter(function_to_apply, list_of_inputs):
    if function_to_apply is None:
        return [e for e in list_of_inputs if e]
    return [e for e in list_of_inputs if function_to_apply(e)]


test = [1, 2, 3, 4, 5]
print(*filter(lambda x: x % 2, test))
print(*ft_filter(lambda x: x % 2, test))
