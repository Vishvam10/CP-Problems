def areIsomorphic(s1: str, s2: str) -> bool:
    if(len(s1) != len(s2)) :
        return 0
    n = len(s1)
    mp = {}
    for i in range(n) :
        if(s1[i] not in mp and s2[i] not in mp.values()) :
            mp[s1[i]] = s2[i]

    temp = ""
    for ch in s1 :
        if(ch in mp) :
            temp += mp[ch]
            
    return 1 if temp == s2 else  0