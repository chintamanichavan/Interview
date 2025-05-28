def sortByBits(arr):
    # Custom sort key function
    def sort_key(x):
        return (bin(x).count('1'), x)
    
    return sorted(arr, key=sort_key)
