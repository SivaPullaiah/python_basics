# #1 solved
list_a = list(map(int, input().split())) # Defaultly saparator was space any no.of or tabs also
#list_a = list(map(int, input().split(',')))  #Now it will split the based on comma
print(list_a)
print(list_a.__class__.__name__)
print(list_a[1].__class__.__name__)