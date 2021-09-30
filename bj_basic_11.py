# 1


n, m = map(int, input().split())

card = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                result = max(result, card[i]+card[j]+card[k])

print(result)


#2


n = int(input())
result = 0

for i in range(1, n+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if (s == n):
        result = i
        break

print(result)


#3


num_student = int(input())
student_list = []

for i in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))


for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')


#4


n, m = map(int, input().split())
l = []
mini = []

for _ in range(n):
    l.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b) % 2 == 0:
                    if l[b][j] != 'W': idx1 += 1
                    if l[b][j] != 'B': idx2 += 1
                else :
                    if l[b][j] != 'B': idx1 += 1
                    if l[b][j] != 'W': idx2 += 1
        mini.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        mini.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(mini))                                   # 칠해야 하는 개수의 최소값


#5


n = int(input())

M_N = 666

cnt = 0

while True:
    if '666' in str(M_N):
        cnt += 1
    if cnt == n:
        print(M_N)
        break
    M_N += 1