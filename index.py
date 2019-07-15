from error_handler import error_handling


# @error_handling('bar')
def foo(bar):
    if not isinstance(bar, int):
        raise TypeError('Bar must be an int')

    if bar <= 0:
        raise ValueError('The error has to be more than zero ')

    print(f'foo: {bar}')

    return bar


