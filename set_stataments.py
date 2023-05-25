# set은 집합이라고 부르기도 한다.
# s1 = {'이름','나이','성별'}
# s1= set(['이름','나이','성별'])
# print(s1)
# s2 = set(list('test'))
# print(s2)

# lista =['a','a','a','b','b','ab','o']
# seta = set(lista)
# print(len(seta))
# for a in seta:
#     print(a)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
s3 = s1|s2
s3 = s1.union(s2)
print(s3)

s3 = s2.difference(s1)
print(s3)

s1 = {1,2,3,4,5,6}
s1.add(7)
print(s1)

s1={1,3,5,7}
s2={2,4,6,8}
s1.update(s2)
print(s1)

s1= {1,2,3,4,5,6}
s1.remove(1)
print(s1)



