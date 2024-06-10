def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
                
my_list=list(map(int,input().split()))
print("Original List:",my_list)
selection_sort(my_list)
print("Sorted List:",my_list)




# arr=[1,2,3,4,5,6]#adding array numbers
# for i in range(len(arr)):
#     sum+=i
# print(sum)