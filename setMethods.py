# sets = mutable , set elements = immutable
collection = set()
collection.add(1)
collection.add(2)
collection.add("apna")
collection.add((1,2,3))
collection.remove(1)
print(collection)
collection.clear()
 
print(len(collection))

collection = {"hello","apnacollege","world","coding","python"}
print(collection.pop())
print(collection.pop())


set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))  # {1,2,3,4}
print(set1.intersection(set2)) #{2,3}