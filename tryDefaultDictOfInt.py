import collections

arr = ['hello', 'world', 'hello', 'hi', 'hello', 'hi']
dict1 = collections.defaultdict(int)

for s in arr:
    dict1[s] += 1

print dict1
print dict(dict1)
