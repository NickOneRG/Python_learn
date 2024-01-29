# res = 0
# for i in input().split():
# 	res += (int(i)//2) + int(i)%2

# print(res)
  
print(sum([((int(i)//2) + int(i) % 2) for i in input().split()]))
