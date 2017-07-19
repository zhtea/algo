#coding=utf-8

"""
版本:python2

使用manacher算法求解最长回文子串
算法时间复杂度为O(N),空间复杂度O(N)

"""

def manacher(query):
    #对长度为N的字符串依次插入N+1个特殊符号，构造出的新字符串可以使得所有回文串长度都是奇数
    n = len(query)
    l = "#"
    for i in query:
        l = l+i+"#"
    n = 2*n + 1
    p = [0] * n # p用来存储每个字符所在位置，以该字符为中心的最长回文子串的,中心点到最右边的距离
    mx = 0 #用来存储当前最长长度的中心店所在位置
    mx_i = 0 #记录最长子串的最右所在位置
    for i in range(n):
        if mx_i > i :
            p[i] = min(p[2*mx - i],p[mx_i-i])
        else:
            p[i] = 1
            while i-p[i]>-1 and i+p[i]<n and  l[i-p[i]] == l[i+p[i]]:
                p[i] += 1
            if p[i] > mx_i-mx:
                mx_i = p[i] +i
                mx = i
    #print(mx_i)
    return mx_i-mx-1


        



while True:
    try:
        N = input()
        for qw in range(N):
            query = raw_input()
            #print(query)
            print(manacher(query))
    except EOFError:
        break