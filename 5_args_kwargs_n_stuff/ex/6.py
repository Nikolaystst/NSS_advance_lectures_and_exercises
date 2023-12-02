def func_executor(*args):
    result = []

    for k, v in args:
        result.append(f"{k.__name__} - {k(*v)}")

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
# multiply_numbers(1, 2)
# sum_numbers(2, 4)
