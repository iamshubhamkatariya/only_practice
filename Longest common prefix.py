def longest_common_prefix(strs):
    if not strs:

        return ""

    base = min(strs, key=len)

    for i, ch in enumerate(base):
        for s in strs:
            if s[i] != ch:
                return base[:i]
    return base