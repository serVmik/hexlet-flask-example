def g():
    print('hi')


def f():
    print('HI')


def print_start_end(f_):
    print('start')
    f_()
    print('end')


print_start_end(f)
