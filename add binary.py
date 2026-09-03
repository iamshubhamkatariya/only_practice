def add_binary(a: str, b: str) -> str:

    decimal_sum = int(a, 2) + int(b, 2)
    return bin(decimal_sum)[2:]

print(add_binary('101', '110'))
print(add_binary('1111', '1'))
print(add_binary('001', '001'))