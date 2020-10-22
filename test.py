def sort_main(w):
    a = []
    b = []
    c = []
    u = []
    for i in w[::-1]:
        b = get_list(i)
        a = u.copy()
        c = []
        u = sort_swap(a,b,c)
    return u

def get_list(i):
    j = []
    if i<10:
        if(i==2):
            j = ['a','b','c']
        if(i==3):
            j = ['d','e','f']
        if(i==4):
            j = ['g','h','i']
        if(i==5):
            j = ['j','k','l']
        if(i==6):
            j = ['m','n','o']
        if(i==7):
            j = ['p','q','r','s']
        if(i==8):
            j = ['t','u','v']
        if(i==9):
            j = ['w','x','y','z']
    else:
        temp = []
        temp.append(i//10)
        temp.append(i%10)
        j = sort_main(temp)
    return j

def sort_swap(a,b,c):
    for i in b:
        for j in a:
            c.append(i+j)
    if a == []:
        c = b
    if b == []:
        c = a
    return c

if __name__ == '__main__':
    w =eval(input('输入一个list,比如[2,3,4]'))
    u =sort_main(w)
    print(u)
