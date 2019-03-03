time = 1
tort = [0]
hare = [0]
distance = 100

while time <= 180:
    tstart = 0
    tort.append(tort[time - 1] + ((4/3) * (100) / 60))
    if tort[time] >= 100: tort[time] = 0
    if time >= 30:
        hare.append(hare[time-1] + ((6) * (100) / 60))
        if hare[time] >= 100: hare[time] = 0
    else:
        hare.append(0)

    print('Time is ' + str(time))
    print('Tortoise is at ' + str(tort[time]))
    print('Hare is at ' + str(hare[time]))
    print('-------------------------')

    time = time + 1

