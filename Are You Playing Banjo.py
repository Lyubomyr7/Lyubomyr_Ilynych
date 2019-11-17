def areYouPlayingBanjo(name):
    if name[0].upper() == "R":
        return  name + " plays banjo"
    else:
        return name + " does not play banjo"
    # Implement me!
print(areYouPlayingBanjo("Lyub"))
print(areYouPlayingBanjo("Roman"))