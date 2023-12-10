'''
Time complexity
O(a + a + d) = O(2a + d) = O(a + b)

Space complexity
O(d)
'''
def create_table(array):
     min_value = min(array) # O(a)
     max_value = max(array) # O(a)
     # create list of size (max - min + 1)
     table = [0] * (max_value - min_value + 1) # O(d), where d = max - min
     return table

print(create_table([1,2,3,4,5]))
