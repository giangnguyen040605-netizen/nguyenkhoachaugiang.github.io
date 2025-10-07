import sys

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    map_st, map_ts = {}, {}
    
    for cs, ct in zip(s, t):
        if (cs in map_st and map_st[cs] != ct) or (ct in map_ts and map_ts[ct] != cs):
            return False
        map_st[cs] = ct
        map_ts[ct] = cs
    
    return True

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    print(is_isomorphic(s, t))
