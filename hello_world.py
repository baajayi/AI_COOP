def equilibrum (num):
    right_sum=sum(num)
    left_sum=0
    for i in range(len(num)):
        right_sum-=num[i]
        if right_sum==left_sum:
            return i
        left_sum+=num[i]
    return -1

print(equilibrum([1,100,50,-51,1,1]))