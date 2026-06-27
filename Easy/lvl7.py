import math
def solver(nums):
    n=len(nums)
    pass_count=0
    highest=-1
    for i in range(n):
        if nums[i]>40:
            pass_count+=1
        if nums[i]>highest:
            highest=nums[i]
    return pass_count,highest,average

nums = [int(x) for x in input("Enter the numbers separated by spaces: ").split()]
pass_count, highest, average = solver(nums)
print(f"Number of students who passed: {pass_count}")
print(f"Highest score: {highest}")     
print(f"Average score: {average:.2f}") 




