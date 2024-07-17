
#  product of two maximum interger in a given list
def max_product(nums):
#if no of elemts in a list is less than 2
  if len(nums)<2:

    return " Atleast two elemnents should be there"

# sorting given list by using sorted

  sorted_list= sorted(nums, reverse=True)

  print("Sorted list",sorted_list)

  max1= sorted_list[0]
  max2=sorted_list[1]

  return max1*max2

  #use case

nums=[2,7,8,5,4]

result= max_product(nums)

print("maximum product", result)

