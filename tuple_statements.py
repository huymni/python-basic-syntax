# t1 = (1,2,'a','b')
# print(t1)
# print(t1[0])

# del t1[0]
# print(t1)

# dic1 = {'이름': '홍길동', '나이':25, '성별': '남'}
# dic1 = {'이름': '홍길동', '나이':25, '성별': '남','성별':'여'}
# print(dic1)
dic1 = {'이름': '홍길동', '나이':25, '성별': '남','성별':'여'}
# dic1 = {'신분'}='학생'
print(dic1)

# del dic1['성별']
# print(dic1)

# keylist = dic1.keys()
# print(keylist)
# for a in keylist:
#     print(a)
#     print(dic1[a])

# keylist = dic1.values()
# print(keylist)
# for a in keylist:
#     print(a)






# keylist =dic1.items()
# print(keylist)
# for a in keylist:
#     print(a)

# templist1 =[]
# templist2 =[]

dic1 = {'이름': '홍길동', '나이':25, '성별': '남','성별':'여'}
keylist = dic1.keys()
print(keylist)
for a in keylist:
    print(a)
    print(dic1[a])

dic1 = {'a':1,"b":2,"c":3}
dic2 = {'a':2,"d":4, "f":5}
dic1.update(dic2)
print(dic1)


lista=['a','a','b','o','o','ab','ab']
dicta={}
for a in lista:
    

#if a  in dicta.keys()