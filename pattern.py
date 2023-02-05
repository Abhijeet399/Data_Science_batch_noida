n = 5
num = 1
gap = n - 1
for j in range(1, n + 1):
    num = j
    gap = gap - 1
          
    for i in range(1, j + 1):
        print(num, end="")
        num = num + 1
      
    num = num - 2
    for i in range(1, j):
        print(num, end="")
        num = num - 1
      
    print()

n = 5
i = 0
prev_count = 0
count = 0
while(i<n):
    count = i+1
    j = 0
    while(j<(2*i+1)):
        if (count<=(2*i + 1)):
            print(count, end="")
            count+=1
            prev_count = count-1
        else:
            prev_count-=1
            print(prev_count, end = "")
        j+=1
    i+=1
    print("")