number=1
for i in range(1,101):
    if i%2==0:
        continue
    elif i%2==1:
        print(i,end='\t')
        if i<50:
          number*=i
print('\n')
print(number)