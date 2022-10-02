def square_1():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if (j*j>c and g==0):
            g=j-1
    while(abs(g*g-c)>0.0001):
        g+=0.00001
        i+=1
    print("%.5f" % g)
square_1()
def square_2():
    i=0
    c=2
    m_max=c
    m_min=0
    g=(m_max+m_min)/2
    while(abs(g*g-c)>0.00000000000001):
        if(g*g<c):
            m_min=g
        else:
            m_max=g
        g=(m_max+m_min)/2
        i+=1
    print("%.13f" % g)
square_2()
def square_3():
    c=2
    g=c/2
    i=0
    while(abs(g*g-c)>0.00000000000001):
        g=(g+c/g)/2
        i+=1
    print("%.13f" % g)
square_3()