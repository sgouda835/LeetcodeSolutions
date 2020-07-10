# def duplicate(nums):
#     return list(set([i for i in nums if nums.count(i)>1]))
import collections
def duplicate(nums):
    return [item for item,count in collections.Counter(nums).items() if count > 1]

nums =[1,2,3,4,5,6,7,1,2]
print(duplicate(nums))



# def get_duplicates(arr):
#     dup_arr = arr[:]
#     for i in set(arr):
#         dup_arr.remove(i)
#     return list(set(dup_arr))

# print (get_duplicates([1,2,3,5,6,7,5,2]))
