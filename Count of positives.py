def count_positives_sum_negatives(arr):
    result=[]
    count_p = 0
    sum_n = 0
    if arr ==[]:
        return result
    for i in arr:
        if i>0:
            count_p+=1
        else:
            sum_n += i
    result.append(count_p)
    result.append(sum_n)
    return result