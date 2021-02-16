# import sys
# import datetime
# print("Twinkle, twinkle, little star,")
# print("         How I wonder what you are! ")
# print("                 Up above the world so high,")
# print("                 Like a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("         How I wonder what you are")
#
# print("Python version")
# print(sys.version)
# print("Version info")
# print(sys.version_info)
#
# now = datetime.datetime.now()
# print ("Current date and time : ")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))


# 10
# num = int(input("Input a number: "))
# num1 = int( "%s" % num )
# num2 = int( "%s%s" % (num,num) )
# num3 = int( "%s%s%s" % (num,num,num) )
# print(num1+num2+num3)

# 11

# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)

# 12 calculate number of days between two dates
# from datetime import date
# fDate = date(2014, 7, 2)
# lDate = date(2014, 7, 11)
# print(lDate - fDate)


# 15
# from math import pi
# r = 6.0
# v = 4.0/3*pi*r**3
# print('the volume of the sphere is', v)

# 16

# def diff(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
#
# print(diff(18))

# 17
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(50000))

# 18

# def sum(x, y, z):
#     sum = x + y + z
#     if x == y == z:
#         sum = sum * 3
#     return sum
# print(sum(1,2,3))
# print(sum(0,0,0))

# 19
# def newString(str):
#     if len(str) >= 2 and str[:2] == "Is":
#         return str
#     return "Is"+str
# print(newString('array'))
# print(newString('hello world'))
# print(newString('isempty'))
# print(newString('Isempty'))

# # 20
# def checkNumber(num):
#     if (num % 2 == 1):
#         print("even number")
#     else:
#         print("odd number")
#
#
# print(checkNumber(45))
# print(checkNumber(10))


# 22
# def list_count_number(nums):
#     count = 0;
#     for num in nums:
#         if num == 4:
#             count = count + 1
#     return count
#
# print(list_count_number([4,4,4,4,4,5]))
# print(list_count_number([0,0,0,0,0,0]))

# 23

# def substr_copy(str, n):
#     flen=2
#     if flen > len(str):
#         flen = len(str)
#     substring = str[:flen]
#     result = ""
#     for i in range(n):
#         result = result + substring
#     return result
#
# print(substr_copy("abs",8))
# print(substr_copy('p', 3))

# 24 test whether a passed letter is a vowel or not
# def vowel(char):
#     all_vowel = 'aeiou'
#     return char in all_vowel
# print(vowel('c'))
# print(vowel('e'))

# 25
from setuptools._distutils.command.check import check

# def check(arr, n):
#     for num in arr:
#         if num == n:
#             return True
#     return False
#
#
# print(check([1, 3, 3, 3, 3, 3, 9], 9))
# print(check([1, 3, 3, 3, 3, 3, 9], 0))

# 26
# def pri(arr):
#     for i in arr:
#         for j in range(i):
#             print("*", end='')
#         print()
#
# pri([1,2,3,0,9])

# 27
# def toString(li):
#     result = ""
#     for i in li:
#         result += str(i)
#     return result
#
# print(toString([16,9,9,99,"ans"]))

# 28 print all even number form a given number
# def printAllEvenNum(numbers):
#     for i in numbers:
#         if i == 237:
#             break
#         elif i % 2 == 0:
#             print(i)


# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# printAllEvenNum(numbers)

# 29
# def notInList(list1, list2):
#     result = ''
#     for l1 in list1:
#         if l1 not in list2:
#             result = result + l1 + " "
#
#     for l1 in list2:
#         if l1 not in list1:
#             result = result + l1 + " "
#
#     return  result

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print(notInList(color_list_1, color_list_2))


# 32
# def lcm(x, y):
#     if x > y:
#         z = x
#     else:
#         z = y
#     while True:
#         if z%x == 0 and z%y == 0:
#             return z
#         else:
#             z+=1
#
# print(lcm(4,6))
# print(lcm(15,17))


# 36
# def addNum(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         raise TypeError("Input must be integers")
#     return a + b
# print(addNum(4,8.2))
#
# # 37
# def detail():
#     name, age = "simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
# detail()

# 40
# import math
# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
#
# print(distance)

# import struct
# print(struct.calcsize("P") * 8)

# 45
# from subprocess import call
# call(["ls", "-l"])

# 48
# str = "15.5"
# print(float(str))
# print(int(float(str)))

# 50
# for i in range(0, 10):
#     print('*', end="")

# 51
# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th
#
# print('Number of columns and Rows: ',terminal_size())

# 68
# if __name__ == '__main__':
#     s = 0
#     number = 156
#     while number != 0:
#         s = s + number % 10
#         number = number / 10

# num = int(input("Input a four digit number: "))
# x = num
# x1 = num

# 69
# def sort(a, b, c):
#     a1 = min(a, b, c)
#     a3 = max(a, b, c)
#     a2 = (a + b + c) - a1 - a3
#     print(a1, a2, a3)
# sort(1,8,0)
# sort(111,111,111)

# def test_distinct(data):
#   if len(data) == len(set(data)):
#     return True
#   else:
#     return False
# print(test_distinct([1,5,7,9]))
# print(test_distinct([2,4,5,5,7,9]))

data = [2, 4, 5, 5, 7, 9]
a = len(data)
n = len(set(data))
if a == n:
    print(True)
