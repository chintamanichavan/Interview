def using_bit_manipulation(n):
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1
        print(count)
        return count


n = 11111111111111111111111111111101
using_bit_manipulation(n)