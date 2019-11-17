
def enough(cap, on, wait):
    place= cap-on

    if wait<place:
        people_on_station=0
    else:
        people_on_station = wait-place


    return people_on_station

print(enough(10,5,4))