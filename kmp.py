#coding=utf-8
#KMP  
def kmp_match(s, p):  
    m = len(s); n = len(p)  
    cur = 0#起始指针cur  
    table = partial_table(p)  
    c = 0
    while cur<=m-n: 
        mark = True
        for i in range(n):  
            if s[i+cur]!=p[i]:  
                cur += max(i - table[i-1], 1)#有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位  
                mark = False
                break  
        if mark:
            c += 1
            cur += n - table[n-1]
                  
    return c  
  
#部分匹配表  
def partial_table(p):  
    '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''  
    prefix = set()  
    postfix = set()  
    ret = [0]  
    for i in range(1,len(p)):  
        prefix.add(p[:i])  
        postfix = {p[j:i+1] for j in range(1,i+1)}  
        ret.append(len((prefix&postfix or {''}).pop()))  
    return ret  
#print(partial_table('HA'))
#print kmp_match('HAHAHA','HA')

while True:
    try:
        n = int(raw_input())
        for i in range(n):
            a = raw_input()
            b = raw_input()
            print(kmp_match(b,a))
        
    except EOFError:
        break