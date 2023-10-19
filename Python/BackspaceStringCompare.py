def backspaceCompare(s: str, t: str) -> bool:
    def next_char(s, pointer):
        backspaces = 0
        while pointer >= 0:
            if s[pointer] == '#':
                backspaces += 1
                pointer -= 1
            elif backspaces > 0:
                backspaces -= 1
                pointer -= 1
            else:
                return s[pointer], pointer
        return None, pointer

    ptr_s, ptr_t = len(s) - 1, len(t) - 1
    while ptr_s >= 0 or ptr_t >= 0:
        char_s, ptr_s = next_char(s, ptr_s)
        char_t, ptr_t = next_char(t, ptr_t)
        if char_s != char_t:
            return False
        ptr_s -= 1
        ptr_t -= 1

    return True
