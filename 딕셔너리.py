
# 딕셔너리 자료형
# 대응관계를 나타내는 자료형  ---> 연관배열 , 해시(Hash)
# Key 와 Value 한 쌍으로 갖는 자료형
# Key를 통해 Value를 얻는다.

# << 딕셔너리 만들 때 주의사항 >>
# Key 값은 중복되면 안 된다.
# Key에 리스트를 쓸 수 없다.
# 하지만 Key에 튜플를 사용할 수 있다.  --> 키가 변하지 않는 값이면 사용가능(튜플은 변하지 않음)

a = {1:'hi'}   # Key로 정수 값 1, Value로 문자열 'hi' 사용
a = {'a':[1,2,3]}  # value에 리스트도 넣을 수 있다.

# 딕셔너리 쌍 추가
a = {1:'a'}
a[2] = 'b'
a  # {1: 'a', 2: 'b'}
a['name'] = 'pey'
a  # {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]
a  # {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 딕셔너리 요소 삭제하기 : del
del a[1]  # Key가 1인 딕셔너리 삭제
a  # {2: 'b', 'name': 'pey', 3: [1, 2, 3]}


# << 딕셔너리 함수 >>
# keys() : key만 모아 dict_keys객체로 돌려준다
a = {"name":"pey","phone":"01022223333","birth":"1118"}
a.keys()  # dict_keys(['name', 'phone', 'birth'])

# values() : value만 모아 dick_values객체로 돌려준다.
a.values()  # dict_values(['pey', '01022223333', '1118'])

# items() : key와 value의 쌍을 튜플로 묶은 값을 dick_items객체로 돌려준다.
a.items()  # dict_items([('name', 'pey'), ('phone', '01022223333'), ('birth', '1118')])

# clear() : 딕셔너리 안의 모든 요소를 삭제
a.clear()
a  # {}

# get(x) : x라는 key에 대응되는 value를 돌려준다.
a = {"name":"pey","phone":"01022223333","birth":"1118"}
a.get('name')  # 'pey'
a.get('phone')  # '01022223333'
# 찾는 값이 없으면 디폴트 값을 출력
a.get("birth222","없어요") # '없어요'

# in : key가 딕셔너리에 있는지 조사하기
# 있으면 True / 없으면 False
'name' in a  # True : dic 안에 name 이 존재한다
'name2' in a  # False : dic 안에 name2가 존재하지 않는다.







