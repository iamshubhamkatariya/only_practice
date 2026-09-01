def plus_one(digits: list[int]) -> list[int]:
    n = len(digits)
    
    # Last se start karke aage badho
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # Agar digit 9 hai to 0 ban jayega aur carry aage jayega
        digits[i] = 0
    
    # Agar yahan tak pahunche, iska matlab sab digits 0 ho gaye
    # aur carry abhi bhi 1 hai, to start mein 1 add karo
    digits.insert(0, 1)
    return digits

print(plus_one([1, 2, 3]))      # [1, 2, 4]
print(plus_one([4, 3, 2, 1]))   # [4, 3, 2, 2]
print(plus_one([9]))            # [1, 0]
print(plus_one([9, 9, 9]))      # [1, 0, 0, 0]