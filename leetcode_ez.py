def run():
    from inspect import signature
    from json import loads, dumps

    solution = Solution()

    func = None
    for attr_name in dir(solution):
        if attr_name.startswith('_'):
            continue
        attr_value = getattr(solution, attr_name)
        if callable(attr_value):
            if func is not None:
                raise Exception('There are multiple methods in Solution class')
            func = attr_value
    if func is None:
        raise Exception('The function in Solution class is not found')

    params_length = len(signature(func).parameters)

    input_file = open(0)
    output_file = open('user.out', 'w')

    try:
        while True:
            output_file.write(
                dumps(
                    func(*[loads(next(input_file)) for _ in range(params_length)]),
                    separators=(',', ':')
                ) + '\n'
            )
    except StopIteration:
        exit()


run()
