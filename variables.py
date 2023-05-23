# 이 #표시는 프로그래밍에서 주석이라 말한다.
# 주석은 파이썬의 인터프리터가 인식하지 못하도록 기호
# 단축키는 ctrl 슬래시

# 아래 a=1의 의미는 a와 1이 같다는 의미가 아니라,
# a라는 이름의 변수에 1을 담겠다는 뜻
a=1
b='1'

# print는 실행후 결과값을 가시적으로 보여주기 위해 터미널창에 출력하는 것
print(a)
print(b)

# 변수명규칙
# 변수명을 지울때는 숫자가 먼저 나와서는 안된다.
# 변수명 중간에 띄어쓰기, 특수기호등을 일반적으로 쓰지 않는다.
# 특수부호는 일반적으로 사용하지 않지만 _언더바는 번번히 사용한다.

#변수 자료형 출력해보기
print(type(a))
print(type(b))

c=2.1
print(type(c))
a=3
b=4
# 덧셈 : +, 빼기 : -, 곱하기 :*, 나누기 : /, 몫 : //, 나머지 : %
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# 자료의 형변환
# 숫자 -> 문자, 실수 -> 정수
a=10
b=20
#결과값이 1020이 나오도록 덧셈을 하여라
print(str(a)+str(b))
c=23333.33333
# c의 소수부분을 잘라서 출력하라
print(int(c))

# 문자 자료형
# 문자는 ""쌍따옴표 또는 ''홀따옴표로 표현을 한다.
# 'a'라는 문자를 변수에 저장하게 되면, 메모리상에 어떤 숫자값으로 저장될까?
# 아스키코드라는 문자의 메핑되는 테이블을 사용하여 약속된 숫자값으로 저장
#현대에는 아스키코드의 표현범위의 한계로 인해, utf-8을 표준으로 사용
x='a'
print(ord(x))
y='A'
print(ord(y))

# multi line으로 문자열을 표현하고 싶으면, 
# 쌍따옴표 3개를 사용하거나 홀따옴표 3개를 사용하면 된다.
a="""hello 
world"""
# 이스케이프문을 활용한 줄바꿈
# 이스케이프문이란 \n 또는 \t 등의 특수기호를 말한다.
# \n : 줄바꿈, \t : tap키
# 역슬래시의 또다른 활용 : 특수문자를 있는 그대로 표현하는 역할
# "쌍따옴표(")는 파이썬에서 문자를 의미한다"라는 문구를 출력해보세요
a="쌍따옴표(\")는 파이썬에서 문자를 의미한다"
print(a)
a = "hello \t world"
print(a)

# 그렇다면 python's easy 라는 문구를 출력해보자.
a="python's easy"
print(a)

# 문자열 더하기, 곱하기
# a라는 변수에 python이라는 문자열을 담고, 
# b라는 변수에는 is fun이라는 문자열을 담는다.
# 그리고 c라는 변수에 두 문자열을 더한 값을 넣어 c를 출력
a= 'python '
b= ' is fun'
c= a+b
print(c)
# python python is fun이라는 문자열을 c에 담아 출력
a= 'python '
b= ' is fun'
c= 2*a+b
print(c)
# 파이썬에서 인덱스란, 기본적으로 특정위치를 
# 가리키는 용도로 사용
# 인덱스의 사용방법은 원하는대상[숫자값]
# 프로그래밍에서는 대부분의 순서는 0부터 시작된다.
# 0,1,2,3,4,5... 의 체계
# 문자 h를 출력하라
a= "python's fun"
print(a[3])

# 문자열의 마지막문자를 출력해보자.
a= "python's fun python's fun python's fun"
print(a[-1])
# 문자열의 길이를 구하는 함수는 len()
print(a[len(a)-1])

# 문자열의 슬라이싱
# 슬라이싱이란 문자열을 잘라내는 것을 의미
#대상변수[x:y] : x이상 y 미만의
# index를 가진 문자열을 잘라낸다.
a= "python is fun"
# python만 잘라내서 b에 담아 출력해주세요
b= a[0:6]
print(b)
# x, y 자리에 값이 없으면 처음부터 또는 끝까지를 의미
# 6번째 문자부터 끝까지 잘라내서 변수 b에 담아 출력
b= a[6:]
print(b)
# a[x:y:z] 여기에서 z는 z-1 개씩 건너뛰고,
# 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력.
b=a[2:7:2]
print(b) 

a="20220505children's_day"
date=a[:8]
day=a[8:]
print(date)
print(day)

# 문자열 포맷팅이란 문자열 중간에 특정 문자(또는 숫자 등)를 삽입하는 방식,
# %s : 문자열, %d : 정수, %f는 실수
# 포맷팅을 왜 쓰는가? 
# 1) 문자열을 직접 삽입하면 1회성으로 coding 할수밖에 없지만,
# 포맷팅은 변수값을 삽입할 수 있다.
# 2) 따옴표를 여러번 안닫아도 된다.
language = input("좋아하는 언어를 입력하세요")
times = int(input('그 언어를 몇번이나 공부하셨나요'))
a= "I studied %s very hard %d times"%( "language", "times")
print(a)
# 아래와 같이 코딩하면 따옴표로 열고 닫고를 너무 많이해서 귀찮다.
a= "I studied" + language +  "very hard" + str(times)+ "times"
print(a)
# 나이가 몇살이신가요? 라고 해서 나이를 받고
# 몸무게가 몇킬로그램 이신가요? 라고해서 weight받고
# my age is %d, and weight %f kg
# 위 문자열을 포맷팅을 통해 사용자의 입력값에 따라
#달라지도록 만들고, 그결과값을 출력하라.

age= input("나이가 몇살이신가요?")
weight = input (" 몸무게가 몇킬로그램 이신가요?")
a = "my age is %d, and weight %f kg"%(int(age),float(weight))
print(a)
age= int(input("나이가 몇살이신가요?"))
weight = float(input (" 몸무게가 몇킬로그램 이신가요?"))
a = "my age is %d, and weight %f kg"%((age),(weight))
print(a)

# 문자열 관련 주요 함수
# count : 대상 문자열에 지정한 문자가 몇개가 있는지 출력하는 함수
# a="python"
# print(a.count('o'))

# find : 대상 문자열에서 지정한 문자가 몇번 index에 있는지 찾는 함수
# index : find와 같은 기능
print(a.find('o'))
print(a.index('o'))

# 없는 문자열 찾을 때는 -1 return
print(a.find('x'))

# 대소문자 변경 : upper()/ lower()
a = "hello"
print(a.upper())
b= "HELLO"
print(b.lower())

# 문자열 양쪽 공백을 없애는 함수 : strip()
a = '      hello world'
print(a.strip())

# 문자열 대체 : replace()
a = ' I studied python'
print(a.replace('python','java'))

# 공백을 기준으로 문자를 자르는 함수 : split()
a= "I studied python"
b=a.split()
print(b)

a= "I    studied    python"
b=a.split(" ")
c=a.split()
print(b)
print(c)

a= "I:studied:python"
b=a.split(':')
print(b)
x=float(input('x값을 입력하세요'))
#y= 2.5 * x**2 +3.3*x+6
y= 2.5 * pow(x,2) +3.3*x+6
print(y)

a=input("첫번째 단어를 입력하세요")
b=input("두번째 단어를 입력하세요")
c=input("세번째 단어를 입력하세요")
abbr= a[0]+b[0]+c[0]
print(abbr)

