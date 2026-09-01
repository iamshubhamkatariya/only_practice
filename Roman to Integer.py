def roman_to_int(s: str) -> int:
    roman_no = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(s)

    for i in range(n):
        value = roman_no[s[i]]

        if i + 1 < n and roman_no[s[i]] < roman_no[s[i + 1]]:
            total -= value
        else:
            total += value

    return total

print(roman_to_int("III"))