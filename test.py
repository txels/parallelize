from parallelize import listify, parallelize


@parallelize
def addition(x, y):
    return x + y


def assert_eq(actual, expected):
    assert actual == expected, f"\n{actual}\nis not\n{expected}"


assert_eq(listify({1: 8, 2: 28, 0: 3}), (3, 8, 28))
assert_eq(addition([(1, 2), (3, 5), (12, 16)]), ( 3, 8, 28 ))
assert_eq(addition(1, 5), 6)
