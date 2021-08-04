n, m = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

temp_list = a_list+b_list
print(*sorted(temp_list))