my_tuple=(1,2,3,3,2,3,4,5,5,4,4,5,5,6,5,4,5,4)
max_count=max(my_tuple.count(item) for item in my_tuple)
print(max_count)