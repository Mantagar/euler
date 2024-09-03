travelHistory = [[0 for c in range(0,21)] for r in range(0,21)]
for i in range(0,21):
    travelHistory[0][i] = 1
    travelHistory[i][0] = 1

def travel(w, h):
    if travelHistory[h][w] == 0:
        # calculate ways recursivly
        travel(w-1,h)
        travel(w,h-1)
        travelHistory[h][w] = travelHistory[h-1][w] + travelHistory[h][w-1]
    

travel(20,20)
for i in range(0,21):
    print(travelHistory[i][i])

