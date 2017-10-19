# -*- coding: utf-8 -*-
def left_rotation(array,d,n):
    if 1<=n<=10**5:
        if 1<=d<=n:
            for k in range(d):
                first=array[0]
                del array[0]
                array.append(first)
            return array
        else:
            return 'd is not in interval'
    else:
        return 'n is not in interval'
#left_rotation([1,2,3,4,5],99998,99999)

def number_needed(a,b):
    a,b=a.lower(),b.lower()
    dict_a={}
    dict_b={}
    for l in a:
        if l not in dict_a:
            dict_a[l]=1
        else:
            dict_a[l]+=1
    for l in b:
        if l not in dict_b:
            dict_b[l]=1
        else:
            dict_b[l]+=1
    score=0
    for l in dict_a:
        if l not in dict_b:
            score+=dict_a[l]
        elif dict_a[l]!=dict_b[l]:
            score+=abs(dict_a[l]-dict_b[l])
    for l in dict_b:
        if l not in dict_a:
            score+=dict_b[l]
    return score
#print(number_needed('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke'))

def ransom_note(magazine, ransom):
    magazine=magazine.split(' ')
    ransom=ransom.split(' ')
    dict_m={}
    dict_r={}
    for l in magazine:
        if l not in dict_m:
            dict_m[l]=1
        else:
            dict_m[l]+=1
    for l in ransom:
        if l not in dict_r:
            dict_r[l]=1
        else:
            dict_r[l]+=1
    print (dict_m)
    print (dict_r)
    result=True
    for x in dict_m:
        if x in dict_r:
            print (dict_m[x],dict_r[x])
            if dict_m[x]==dict_r[x]:
                result=True
            else:
                return False
    return result

#print (ransom_note('two times three is not four','two times two is four'))


def solve(n,m):
    score=0
    if m>n:
        score+=m-1
        score+=(m)*(n-1)
    else:
        score+=n-1
        score+=(n)*(m-1)
    return score
#print (solve(569073124,430672581))
#245084191090813043
#245084191090813043
#245084190660140463
import math
def divisor(input_list):
    for n in input_list:
        divisor_list=[]
        for i in range(1,int(str(n**(1/2)).split('.')[0])+1):
            if n%i==0:
                if i not in divisor_list:
                    divisor_list.append(i)
                if n/i not in divisor_list:
                    divisor_list.append(int(n/i))
        score=0
        for div in divisor_list:
            if div%2==0:
                score+=1
        print (score)
# t=input()
# input_list=[]
# for x in range(int(t)):
#     n=input()
#     input_list.append(int(n))
#
asd=[1458,2916,5832,11664,23328,46656,93312,186624,373248,746496]
#print (divisor(asd))
