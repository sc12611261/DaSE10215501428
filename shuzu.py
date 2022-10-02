l=list((range(1,6)))
lenth=len(l)
for i in range(0,lenth):
    print(l[lenth-i-1],end='\t')
print('\n')
while i>=0:
    print(l[i],end='\t')
    i-=1;
print('\n')
print(l[::-1])