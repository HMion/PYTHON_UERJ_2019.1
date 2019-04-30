def do_four(f,x):
    f(x)
    f(x)

def print_twice(a):
    print(a)
    print(a)
###############################################################################
do_four(print_twice,"spam")
