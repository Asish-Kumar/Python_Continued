# def get_fib_sum(num):
#     if num == 1 or num == 2:
#         return num
#     return get_fib_sum(num - 1) + get_fib_sum(num - 2)
#
#
# print(get_fib_sum(5))


def fib(num):
    if num == 1 or num == 2:
        result = 1
    else:
        result = fib(num-1) + fib(num-2)
    return result

print(fib(5))


