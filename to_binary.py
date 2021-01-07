from timeit import timeit

# def base10_to_binary(n:int) -> str:
#     rem_stack = []

#     while n > 0:
#         rem = n % 2
#         rem_stack.append(rem)
#         n = n // 2

#     bin_string = ""
#     while rem_stack:
#         bin_string += str(rem_stack.pop())

#     return bin_string

def base10_to_binary(n:int) -> str:
    rem_stack = []

    while n > 0:
        rem = n % 2
        rem_stack.append(rem)
        n = n // 2

    bin_string = []
    while rem_stack:
        bin_string.append(str(rem_stack.pop()))

    return ''.join(bin_string)

if __name__ == "__main__":
    print(base10_to_binary(5))
    assert base10_to_binary(1) == '1'
    assert base10_to_binary(2) == '10'
    assert base10_to_binary(3) == '11'
    assert base10_to_binary(int(10e10)) == '1011101001000011101101110100000000000'
