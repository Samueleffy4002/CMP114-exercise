def sum_of_list(list):
  sum = 0
  for number in list:
    sum += number
  return sum

my_list = [1, 2, 3, 4, 5]
print("The sum of my_list is", sum_of_list(my_list))