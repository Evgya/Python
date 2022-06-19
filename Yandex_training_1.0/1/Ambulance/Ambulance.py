def get_P_N(K1, M, K2, P2, N2):
    if N2 > M:
        return -1, -1   
    n_flats_on_floor = tuple(
          n_flat for n_flat in range(max(K1,K2) + 1) 
          if 1 <= K2 - n_flat*M*(P2 - 1) - n_flat*(N2 - 1) <= n_flat
          )   
    if len(n_flats_on_floor) == 0:
        return -1, -1
    
    entrances = set()
    floors = set()
    for n_flat in n_flats_on_floor:
        P1 = (K1 - 1) // (M * n_flat)  + 1      
        entrances.add(P1)    
        N1 = (K1 - n_flat*M*(P1 - 1) - 1) // n_flat + 1         
        floors.add(N1)       
     
    if len(floors) > 1 and len(entrances) > 1:            
            return 0, 0
    if len(floors) > 1:
        return entrances.pop(), 0
    if len(entrances) > 1:
        return 0, floors.pop()
    return entrances.pop(), floors.pop()

K1, M, K2, P2, N2 = map(int, input().split())
P1, N1 = get_P_N(K1, M, K2, P2, N2)
print(P1, N1)