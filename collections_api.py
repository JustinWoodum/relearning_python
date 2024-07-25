from collections import namedtuple, deque, Counter, OrderedDict, defaultdict

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(f"Namedtuple Point: x={p.x}, y={p.y}")

# deque
d = deque(['a', 'b', 'c'])
d.append('d')
d.appendleft('z')
print(f"Deque: {d}")
d.pop()
d.popleft()
print(f"Deque after pops: {d}")

# Counter
cnt = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(f"Counter: {cnt}")
print(f"Most common: {cnt.most_common(1)}")

# OrderedDict
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"OrderedDict: {od}")

# defaultdict
dd = defaultdict(lambda: 'default value')
dd['existing'] = 'exists'
print(f"defaultdict existing key: {dd['existing']}")
print(f"defaultdict non-existing key: {dd['non_existing']}")
