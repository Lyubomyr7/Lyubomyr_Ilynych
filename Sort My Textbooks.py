def sorter(textbooks):
    return sorted(textbooks,key=lambda x: x.lower())


print(sorter([ 'Geometry','algebra', 'History', 'English']))
