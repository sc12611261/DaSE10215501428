number=1
tmp=0
s=input()
i=1
temp=1
while i<len(s):
    if s[i-1]==s[i]:
        tmp=1
        temp+=1
    if temp>number:
        number=temp
    i+=1
    temp=1
if tmp==1:
    print("是")
else:
    print("否")
print(number)