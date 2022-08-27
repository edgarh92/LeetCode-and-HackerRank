def twoSum(nums,target) :
    hashmap = {}
    
    for key,value in enumerate(nums):
        diff = target - value
        print(diff)
        if hashmap.get(diff): #get value, which is an index, using the diff as key
            print("found")
            return [key, hashmap.get(diff)]
        
        hashmap[diff] = key

print(twoSum([1,2,3], 3))