def solution(number):
    num=0
    sum =0
    while num<number:
        if num%3 == 0 or num%5 == 0:
            sum = sum+num
        num = num+1
    return sum

print(solution(10))
