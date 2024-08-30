# import pandas
# dir(pandas)
# import math
# print(dir(math))

# x = 4
# y = 1

# # x = 15
# # y = 16

# print(format(x, 'b'))
# print(format(y, 'b'))

# a = x & y
# b = x | y
# c = ~x  # tricky!
# d = x ^ 5
# e = x >> 2
# f = x << 2

# print(f"a= {a}, b={b}, c={c}, d={d}, e={e}, f={f}")
# print(f" c in binary = {format(c,'b')}")

# lst = [5, 3, 1, 2, 4]
# lst.sort(reverse=True)
# # lst.reverse()
# print(lst)

# my_list = [1, 2, "in", True, "ABC"]
# print(my_list[-1])
# print(1 in my_list)  # outputs True
# print("A" not in my_list)  # outputs True
# print(3 not in my_list)  # outputs True
# print(False in my_list)  # outputs False

# table = [[":(", ":)", ":(", ":)"],
#          [":)", ":(", ":)", ":)"],
#          [":(", ":)", ":)", ":("],
#          [":)", ":)", ":)", ":("]]

# table = [[0,1,2,3,4],
#         [0,1,2,3,4],
#         [0,1,2,3,4],
#         [0,1,2,3,4],
#         [0,1,2,3,4]]

# print(table)
# print(table[0][0])  # outputs: ':('
# print(table[0][3])  # outputs: ':)'

# num = []
# vals = num[:]
# vals.append(1)
# num.append(3)
# print(vals)
# print(num)

# vals = [0,1,2]
# vals[0], vals[1] = vals[1], vals[2]
# print(vals)

# my_lst = [1,2,3]
# my_lst.insert(2, "*")
# print(my_lst)

# i=0
# while i<=5:
#   i+=1
#   if i==3:
#     break
#   print("*", i-1, i )

# my_list = [1,2,3,4]
# print(my_list[-3:-2])
# print(my_list[-3:-1])
# print(my_list[-3:])
# print(my_list[-3])

# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list

# print(create_list(5))

# # Example 1
# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)

# # Example 2
# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# # Example 3
# tuple_3 = (1, 2, 3, 5)
# print(len(tuple_3))

# # Example 4
# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2

# print(tuple_4)
# print(tuple_5)


# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }

# for key, value in pol_eng_dictionary.items():
#     print("Pol/Eng ->", key, ":", value)

# # list_1 = [9,8,7]
# # list_2 = [5,6,7]
# # print(list_1 +list_2)
# # print(list_1*2)

# e = pol_eng_dictionary
# if "water" in e:
#   print("Yes!!")

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)
# print(duplicates)

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#   d3.update(item)
# print(d3)

# my_list = ["car", "Ford", "flower", "Tulip"]
# t =  tuple(my_list)
# print(t)

# def fun(x):
#   if x % 2 == 0:
#     return 1
#   else:
#     return

# print(fun(fun(2))+1)
  

# colors = (("green", "#008000"), ("blue", "#0000FF"))
# print(len(colors))

# color_dict = {}
# for color in colors:
#   key = color[0]
#   item = color[1]
#   x = {key : item}
#   color_dict.update(x)
# print(color_dict)

# my_dictionary = {"A": 1, "B": 2}
# copy_my_dictionary = my_dictionary.copy()
# my_dictionary.clear()
# my_list = [1,2,3,4,5]
# llist = my_list.copy()
# my_list.clear()
# print(llist)


# colors = {
#     "white": (255, 255, 255),
#     "grey": (128, 128, 128),
#     "red": (255, 0, 0),
#     "green": (0, 128, 0)
#     }

# for col, rgb in colors.items():
#     print(col, ":", rgb)

# x = 1

# def fun(x):
#   x+=1
#   print(x)
#   print("foo")
#   del(x)
#   print(x)


# fun(x)

# def fun(x=2, out=3):
#   return x * out
# print(fun(3))

# value = input("Enter a value:")
# print(10/value)

# x = None
# y = 2

# print(x<y)

# def fun(x):
#   return x + 1

# x=2
# x=fun(x+1)
# print(x)

#THE OUTPUT OF AN INPUT STATEMENT IS A STRING
# try:
#   value = input("Enter a value: ")
#   print(value/value)
# except ValueError:
#   print("Value Error")
# except ZeroDivisionError:
#   print("Zero Error")
# except TypeError:
#   print("TypeError")
# except:
#   print("WHAT")

# def fun(x, y, z):
#   return x + 2 * y + 3 * z

# print(fun(0, z=1, y=3))

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# def f(x):
#   if x == 0:
#     return 0
#   return x + f(x-1)

# print(f(3))

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']
# print(v)

# for k in range(len(dictionary)):
#   v=dictionary[v]
#   print(v)

# print(v)

#The example question errors out because the function and the variable have the same name - there is a name clash - TYPE ERROR function does not support item deletion
# my_list1 = ['Mary', 'had', 'a', 'little', 'lamb']
# print(my_list1)
# def my_list(my_list):
#   del my_list[3]
#   my_list[3] = 'ram'

# print(my_list(my_list1))
#prints none because the function has no return
#print(my_list1)
#prints the modified list


# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']
# for i in range(len(my_list)-1):
#   dictionary[my_list[i]] = (my_list[i], )
#   print(dictionary)

# for i in sorted(dictionary.keys()):
#   k = dictionary[i]
#   print(i)
#   print(k[0])

# x = None
# y  = None

# if y == x:
#   print("YES!")
# else:
#   print("NO!")

# print(2%1)

# nums = [1,2,3]
# # del nums[2]
# #del nums[:]
# nums.insert(-1,5)
# print(nums)

# print(0/1)

# for i in range(1,2):
#   print(i)

# nums = (1,2,3)
# print(nums.index(3))

# try:
#   print(5/0)
# # except:
# #   print("sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):
#   print("Too bad...")

# a = 1
# b = 0
# a = a^b
# print(a^b)
# b = a^b
# print(b)
# a = a^b
# print(a)
# print(a, b)

# print(1^0)

# lst = [[x for x in range(3)] for y in range(3)]
# print(lst)

# for r in range(3):
#   for c in range(3):
#     if lst[r][c] % 2 != 0:
#       print("#")

# def fun(x, y):
#   if x == y:
#     return x
#   else:
#     return fun(x, y-1)
# print(fun(0,3))

# dct = {'one':'two', 'three':'one','two':'three'}
# v = dct['three']

# for k in range(len(dct)):
#   v=dct[v]
# print(v)

# print(math.e)
# print(math.exp(1))

#x = (math.log(1000))
# print(2.3**2.3)
# tup = (10, 3, 7)
# print(len(tup[0]))

# import sys

# for p in sys.path:
#     print(p)

# y = math.e**x
# print(y)
# print(math.e)
# print(math.log(1000,10))
# print(10*10*10)
# print(10**3)
# print(math.log10(1000))

# print(math.pow(10,3))

#for i in range(1):
#  print('#')
# else:
#   print('#')

# x = 5
# llist = [0, 1, 2, 3, 4]
# # vals = llist[0:5]
# # del vals[-4:-2]
# # print(llist)
# def hello():
#   print(x)
#   llist.append('a')
#   for i in llist:
#     print("hello")
#     #del llist[0]
#     #x -= 1 
#     #... python evaluates the right side first and can't find x  
#     print(llist)
#     print(x)

# hello()
# print(f"llist is {llist}")
# print(x)

# tup = (1,) + (1,)
# tup = tup + tup
# print(len(tup))
# print(tup)

# def fun(x):
#   if x % 2 ==0:
#     return 1
#   else:
#     return

# print(fun(fun(2))+1)


# tup = (1,2,4,8)
# print(tup)
# tup=tup[1:-1]
# print(tup)
# # tup = tup[0]
# # print(tup)
# tup = tup[0:1]
# print(tup)
# print(tup[0])
# dic = {1:1, 2:2}
# for x in dic.values():
#   print(x)

# print(1//2)
# print(1/2)
# print(2/1)
# print(hello, world!)

# for i in range(-2,-1):
#   print(i)

# foo = (1,2,3)
# print(foo.index(3))

# try:
#   print(5/0)
#   break
# except:
#   print("This error message")

# dct = {}
# dct['1'] = (1,2)
# dct['2'] = (2,1)
# print(dct)

# for x in dct.keys():
#   print(f"x={x}")
#   # print(dct[x][1], end="")

# print(dct['1'][1])
# print(dct['2'][1])

# lst = [[x for x in range(3)] for y in range(3)]

# print(lst)

# for r in range(3):
#   for c in range(3):
#     if lst[r][c] % 2 !=0:
#       print(r,c)
#       print('#')

# m_lst = [1,2]
# for v in range(2):
#   m_lst.insert(-1,(m_lst[v]))
#   print(m_lst)

# lst = [i for i in range(-1,-2)]
# print(lst)

# list = [0,1,2,3]
# new_list = []


# x = chr(ord('m')-1)
# print(x)

# s1 = 'Where are the snows of yesteryear?'
# s3 = s1.split('e')
# s2 = s1.split()
# print(s2)
# print(s3)
# print(s2[-2])

# the_list = ['Where', 'are', 'the', 'snows?']
# s =' '.join(the_list)
# print(s)

# d = s.count("s")
# print(d)
# c = s.upper()
# print(c)
# l=s.lower()
# print(l)
# u=s.capitalize()
# print(u)
# n=s.swapcase()
# print(n)
# t=s.title()
# print(t)

# l = "!   LINDA\n   !"
# x = l.count(" ")
# y=len(l)
# print(x, y)


# s1 = 'where are the Snows of Yesteryear?'
# s2 = s1.split()
# s3 = sorted(s2)
# # print(s2)
# # print(s3)
# print(s1)
# s4 = s2.sort()
# print(s4)


