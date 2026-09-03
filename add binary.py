# def add_binary(a: str, b: str) -> str:

#     decimal_sum = int(a, 2) + int(b, 2)
#     return bin(decimal_sum)[2:]

# print(add_binary('101', '110'))
# print(add_binary('1111', '1'))
# print(add_binary('001', '001'))

def add_binary_manual(a: str, b: str) -> str:
    i , j = len(a) -1, len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return '' .join(reversed(result))

print(add_binary_manual('101', '110'))
print(add_binary_manual('1111', '1'))