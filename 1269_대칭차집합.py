a, b = map(int, input().split())

first_set = set(input().split())
second_set = set(input().split())

print(len(first_set-second_set)+len(second_set-first_set))