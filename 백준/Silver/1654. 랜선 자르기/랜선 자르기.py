import sys
input = sys.stdin.readline

#이진탐색 사용!

num, N = map(int, input().split())

k=[]
for _ in range(num):
    k.append(int(input()))

maxLen=max(k)
minLen=1

while minLen <= maxLen:
    mid=(minLen+maxLen)//2
    tmp=0
    for i in k:
        tmp+=i//mid
    if tmp >= N:
        minLen=mid+1
    else:
        maxLen=mid-1
print(maxLen)
