def up_normal_pyramid():
    for i in range(5):
        print(" "*(4-i), end="")
        print("*"*(1+2*i), end="")
        print(" "*(4-i))


def down_normal_pyramid():
    for i in range(5):
        print(" " * i, end="")
        print("*" * (9-(2*i)), end="")
        print(" " * i)


def down_half_pyramid():
    for i in range(5):
        print("*" * (5-i))


down_half_pyramid()