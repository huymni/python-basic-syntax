# list는 변수마다 값을 할당해서 사용하기에, 관리의 어려움이 있으므로
# 한 변수에 값을 집합시켜놓은 것.

# a='김혜민'
# b='김강민'
# c='이성금'
# # print(a)
# # print(b)
# # print(c)

# # 하나의 변수로 여러개의 데이터를 관리
# # list의 경우에[] 대괄호를 사용하여 데이터를 집합
# # lista=[10,20,30]
# # # list안의 각각의 값에 접근할때에는 index를 사용
# # print(lista[0])
# # print(lista[1])
# # print(lista[2])


# # 여러개의 데이터를 범위를 지정해서 가져오고 싶을때는 slicing 사용
# # 슬라이싱의 결과값은 같은 list로 출력
# # 0~5번째까지 출력
# # print(lista[0:5])
# # # 0~5번째까지 출력한 결과물의 type출력
# # print(type(lista[0:5]))

# # 문자열은 내부적으로 list와 유사한 자료구조
# # 문자열은 값을 추가하거나 수정할수가 없다.
# # list는 값의 추가, 삭제, 수정이 가능한 구조를 가지고 있다.

# # list안에 list의 값을 조회하는 방법
# # list_ex1 = ["a",'b','c',[1,2,3]]
# # number = list_ex1[3]
# # print(number[0]+number[2])
# # print(list_ex1[3][0]+list_ex1[3][2])

# # 리스트 더하기 또는 곱하기
# # list를 2개 선언하고 만들어서,
# # 2개를 더해서 하나의 리스트로 만들어보자 그리고 출력
# # lista=['가','나','다']
# # listb=[0,1,2]
# # listc=lista + listb
# # print(listc*10)

# # 리스트 길이 구하기 : len
# # print(len(lista))

# # 리스트 값 수정하기
# # -> 1개의 값만 바꿀 땐 1개의 값으로 대치
# # -> 여러값을 바꿀 땐 다른 리스트로 대치

# # lista=[1,3,5,6,7,9]
# # list[1]=4
# # print(lista)
# # list[2]=[5,5,5]
# # print(lista)

# # 리스트 요소 개수 세기
# # lista=['1','2','3','4','1','1','3']
# # counta = lista.count('1')
# # print(counta)

# # # 리스트 요소 삭제하기 : del 변수 [index]
# # lista=['1','2','3','4','1','1','3']
# # del lista[2]
# # print(lista)

# # 리스트 요소 삭제하기 : remove
# lista=[1,2,3,4,1,1,3]
# lista.remove(3)
# print(lista)

# # 모든 특정한 숫자 3값을 삭제하려면? pass!
# # del, for range
# lista=[1,2,3,4,1,1,3]
# for a in range(0, len(lista)):
#     if lista[a] == 3:
#         del lista[a]
# print(lista)

# list append : 리스트 맨 뒤로 추가
lista = [1,3,5,7]
# 9,10을 append이용해서 추가해서 출력
lista.append(9)
lista.append(10)
print(lista)

# list insert : index를 지정하여 추가 기능
# lista.index(2,"abc") 추가 후 출력
lista.insert(2,"abc")
print(lista)


# list extend :iterable객체를 list에 추가할때 사용
# extend는 각 요소를 꺼내어 맨 뒤에 추가
listb = [10,20,30]
lista.append(listb)
#lista.extend(listb)
print(lista)

# list의 정렬은 sort()함수 사용
# sort()는 오름차순 정렬
# reverse=True 옵션을 주면 내림차순 정렬
numa = [5,3,6,4,7,9,8]
numa.sort(reverse=True)
print(numa)

chlist = ['bra','john','ab']
chlist.sort()
print(chlist)

# list뒤집기 : reverse()
chlist.reverse()
print(chlist)

# list위치 반환 :index()
lista= ['김물쇠','김갑돌','김갑순','김철수']
print(lista.index('김철수'))

# 마지막요소 끄집어 내기 : pop()
# remove and return last value
# print(lista.pop())
lista.pop()
lastvalue = lista.pop()
print(lastvalue)

# 문자 리스트를 문자열로 만들기
lista ['hello','world','python']
st1 = ""
st2=st1.join(lista)
for a in lista:
    st1 =st1 + a
print(st2)
# 문자열을 문자 리스트로 만들기
sta = 'hello world python'
mysta1=list(sta)
print(mysta1)
mysta2=sta.split()
print(mysta2)
