def sortByBits(arr):
    # Custom sort key function
    def sort_key(x):
        return (bin(x).count('1'), x)
    
    return sorted(arr, key=sort_key)

# review 2025-06-17

# review 2026-05-01
