from itertools import combinations

# 호출할때마다 결과가 달라진다 -> 반복해서 호출할 의도가 있다
# generator는 반복문에서 쓰이느느 것!

numbers = [i for i in range(1, 5)]

def print_test():
    for i in range(3):
        yield i
for test in print_test():
    print(test)
    # 리턴 타입에 해당하는 메모리 만큼을 먹어두고 호출할때마다 돌려쓰는 것임..!

combinations(numbers, 3) # 3칸의 박스 하나를 계속 돌려쓸

# 얘를 리스트 씌우면 다시 할당하는것임
list(combinations(numbers, 3)) # 쓸데없는...처리 하는 것임..

for num_set in combinations(numbers, 3):
    print(num_set)
    # 뽑은 케이스에 대한 로직 처리
    # combination을 쓸 때는 리스트를 씌워서 새로운 리스트에 넣는게 아님..!
    # 그래야 제너레이터로 구현됨 효율적으로 짜진 코드를 100프로 확인하는 것이다~
    # combinations를 안쓰고 직접 코드 짜는 이유는.. 중간에 가지치기해야될 경우들이 좀 있어서
    # combinations를 쓰려면 for문안에 쓰는것이 적합한 활용방법이다.

# 부분집합 짜는 코드
# (1,2,3,4,5) 의 부분집합을 구하세요
# 아무것도 안골랐을때, 하나골랐을때,, 다골랐을때의 모든 경우의수를 부분집합이라고함
# 뽑을지 말지에 대한 배열을 중복순열을 뽑아버리자
# 뽑으면 1, 아니면 0 이라하면 (11111) (11011) (11100).. 이런식으로 만들어질 것
# 다 만들어지면 depth가 5일때 끝날 것
# (10001)이면 ..


# 조합 코드에서 조금만 바꾸면 부분집합 코드가
def comb(cnt, idx):
	# 다음에 돌기시작해야되는 인덱스를 인자로 넣어 줘야됨
	if cnt == N:# 뽑을 떄 끝까지 다 뽑고, 출력을 모든 노드가 다 의미있으니까 뽑을떄마다 다 출력하는게 부분집합!
		print(answer)
		return
	for i in range(idx, N):
		answer.append(numbers[i])
		comb(cnt+1, i+1)
		# idx부터 n-1까지 중에 i를 고른 것
		# 뽑은 i 다음의 값을 넘겨줘야됨
		answer.pop() # 원복