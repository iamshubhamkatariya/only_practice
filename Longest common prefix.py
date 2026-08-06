def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(len(prefix)):
        char = prefix[i]

        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return prefix[:i]

    return prefix