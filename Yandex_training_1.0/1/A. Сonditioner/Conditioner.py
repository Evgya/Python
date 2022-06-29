def get_state_t(troom, tcond, mode):
    cond = {
       "freeze": min(troom, tcond),
       "heat":   max(troom, tcond),
       "auto":   tcond,
       "fan":    troom
    }
    return cond[mode]

troom, tcond = map(int, input().split())
mode = input()
print(get_state_t(troom, tcond, mode))
