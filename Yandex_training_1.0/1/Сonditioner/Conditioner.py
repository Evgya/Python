troom, tcond = map(int, input().split())
mode = input()
cond = {
         "freeze": min(troom, tcond),
         "heat"  : max(troom, tcond),
         "auto"  : tcond,
         "fan"   : troom
}

print(cond[mode])
