import math
def distance(x1, y1, x2, y2):
    dis = math.sqrt((math.pow((x2-x1),2))+(math.pow((y2 - y1),2)))
    return round(dis,2)
    # Your code here
print(distance(1,1,0,0))