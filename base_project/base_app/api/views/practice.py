# # # # # # # # Palindrome n symetric
# # # # # # a = 'madam'
# # # # # #
# # # # # # b = int(len(a)/2)
# # # # # # print(b)
# # # # # # if len(a)%2 == 0:
# # # # # #     first_half = a[:b]
# # # # # #     print("first_half %s", first_half)
# # # # # #     second_half = a[b:]
# # # # # #     print("second_half %s", second_half)
# # # # # #
# # # # # # else:
# # # # # #     first_half = a[:b]
# # # # # #     print("first_half %s", first_half)
# # # # # #     second_half = a[b+1:]
# # # # # #     print("second_half %s", second_half)
# # # # # #
# # # # # # if first_half == second_half:
# # # # # #         print("Symetric")
# # # # # # else:
# # # # # #     print("Not symetric")
# # # # # # print("second_half[::-1] ", second_half[::-1])
# # # # # # if first_half == second_half[::-1]:
# # # # # #     print("Palindrome")
# # # # # # else:
# # # # # #     print("Not palindrome")
# # # # # #
# # # # # # # s = "Hello world"
# # # # # # # new_string = ''
# # # # # # # new = s.split(' ')
# # # # # # # print(new)
# # # # # # # print(new[::-1])
# # # # # # # k = new[::-1]
# # # # # # # i = k[0] + " " + k[1]
# # # # # # # print(i)
# # # # # # # q = new_string.join(k)
# # # # # # # print(q)
# # # # # # # print(s.split(','))
# # # # # # #
# # # # # # # string = "geeks quiz practice code"
# # # # # # # # reversing words in a given string
# # # # # # # s = string.split()[::-1]
# # # # # # # print(s)
# # # # # # # l = []
# # # # # # # for i in s:
# # # # # # #     # apending reversed words to l
# # # # # # #     l.append(i)
# # # # # # # # printing reverse words
# # # # # # # print(" ".join(l))
# # # # # # #
# # # # # # # c = " I AM A GEEK"
# # # # # # # x = c.split()[::-1]
# # # # # # # print(x)
# # # # # # # h = []
# # # # # # # for d in x:
# # # # # # #     h.append(d)
# # # # # # # print(" ".jo
# # # # # # #
# # # # # # # in(h))
# # # # # # # GEEK A AM I
# # # # # #
# # # # # # # test_str = "GeeksForGeeks"
# # # # # # est_str ='geeksforgeek'
# # # # # # # s = int((len(est_str))/2)
# # # # # # # n = est_str[:s]
# # # # # # # print(n.upper())
# # # # # # # print(s)
# # # # # # # a = test_str[2]
# # # # # # # g = test_str.replace("e", "l")
# # # # # # # print(g)
# # # # # # # print(test_str)
# # # # # # # count = 0
# # # # # # # all_freq = {}
# # # # # # #
# # # # # # # start = est_str[0]
# # # # # # #
# # # # # # # for a in est_str:
# # # # # # #     if  a in all_freq:
# # # # # # #
# # # # # # #         all_freq[a] += 1
# # # # # # #     else:
# # # # # # #         all_freq[a] = 1
# # # # # # # print(all_freq)
# # # # # #
# # # # # #
# # # # # # # def total_fruits(**kwargs):
# # # # # # #     print(kwargs, type(kwargs))
# # # # # # #
# # # # # # #
# # # # # # # total_fruits(banana="a", mango="x", apple="z")
# # # # # #
# # # # # # # first = "madam"
# # # # # # #
# # # # # # # len_first = int(len(first)/2)
# # # # # # # print(len_first)
# # # # # # #
# # # # # # # if len(first) % 2 == 0 :
# # # # # # #     print("********")
# # # # # # #     first_half = first[:len_first]
# # # # # # #     print(first_half)
# # # # # # #     second = first[len_first:]
# # # # # # #     print(second)
# # # # # # # else:
# # # # # # #     print("&&&&&&&&&")
# # # # # # #     first_half = first[:len_first]
# # # # # # #     print("first_half", first_half)
# # # # # # #     second = first[len_first+1:]
# # # # # # #     print("second %s", second)
# # # # # # #     print("second %s", first[2:])
# # # # # string = "geeks quiz practice code"
# # # # # # reversing words in a given string
# # # # # # s = string.split()[::-1]
# # # # # # print(string.replace('e','h'))
# # # # # # dict = {}
# # # # # # for i in string:
# # # # # #     if i in dict:
# # # # # #         dict[i] += 1
# # # # # #     else:
# # # # # #         dict[i] = 1
# # # # # # print(dict)
# # # # # # rev_list = []
# # # # # # print(s)
# # # # # # for i in s:
# # # # # #     rev_list.append(i)
# # # # # # string = ""
# # # # # # print(" ".join(rev_list))
# # # # # # a = ['la' , 'dd', ['ww', 'aa',['ee', 'rr']]]
# # # # # # list_a = []
# # # # # # for s in a:
# # # # # #     if type(s) == list:
# # # # # #         for a in s:
# # # # # #             if type(a) == list:
# # # # # #                 for b in a:
# # # # # #                   list_a.append(a)
# # # # # #                  if type(a) == list:
# # # # # #                      for b in a:
# # # # # #                          list_a.append(b)
# # # # # #                  else:
# # # # # #                      list_a.append(a)
# # # # # #             else:
# # # # # #                 list_a.append(a)
# # # # # #     else:
# # # # # #         list_a.append(s)
# # # # # #     # else:
# # # # # # print(list_a)
# # # # # # s = [1,2,3]
# # # # # # x = list(map((lambda a:a*2), s))
# # # # # #
# # # # # # print(x)
# # # # # # from abc import ABC, abstractmethod
# # # # # # class Polygon(ABC):
# # # # # #
# # # # # #     @abstractmethod
# # # # # #     def noofsides(self):
# # # # # #         pass
# # # # # #
# # # # # #     def stingword(self):
# # # # # #         print("Hi this is rashmi")
# # # # # #
# # # # # # class triangle(Polygon):
# # # # # #     def noofsides(self):
# # # # # #         print("Have three side")
# # # # # #
# # # # # #
# # # # # #
# # # # # # class rectangle(Polygon):
# # # # # #     def noofsides(self):
# # # # # #         print("Have 4 sides")
# # # # # # #
# # # # # # # s = Polygon()
# # # # # # #
# # # # # # a = triangle()
# # # # # # a.noofsides()
# # # # # # a.stingword()
# # # # #
# # # # #
# # # # #
# # # # # class maths():
# # # # #     count = 1
# # # # #     def __init__(self, a,b,c):
# # # # #         self.a = a
# # # # #         self.b = b
# # # # #         self.c = c
# # # # #
# # # # #     def trangle(self,a,b,c):
# # # # #         print("Enter three side are %s, %s, %s", a,b,c)
# # # # #
# # # # #     @classmethod
# # # # #     def rectangle(cls, b,c):
# # # # #         print("This is rectangele %s %s %s", cls,b,c)
# # # # #         print(count)
# # # # #
# # # # #
# # # # #     @staticmethod
# # # # #     def poligon(z,x):
# # # # #         print("multipal %s, %s", z,x)
# # # # #
# # # # # j = maths(55,88,99)
# # # # # j.trangle(77,99,88)
# # # # # j.rectangle(22,44)
# # # # # # j.poligon(34,56)
# # # # # # j.rectangle(88,99)
# # # #
# # # # #
# # # # # s = "sanjakumar"
# # # # # print(s[:5])    2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
# # # # # print(s[5:])
# # # #
# # # # # a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# # # # #
# # # # # for i in a:
# # # # #     if i > 1:
# # # # #         if i % 2 == 0:
# # # # #             print("%s is not prime", i)
# # # # #         else:
# # # # #             print("%s is prime"
# # # # # l = [1,2,4,5]
# # # # # x = list(filter(lambda a:a>1,l))
# # # # # print(x)
# # # # # o = list(map(lambda a:a>1,l))
# # # # # print(o)
# # #
# # #
# # # #umbercount
# # # # a = "aaabbbccccdd"
# # # # # b = set(a)
# # # # # list = []
# # # # # print(b)
# # # # # for i in b:
# # # # #     count = 0
# # # # #     for s in a:
# # # # #         if s == i:
# # # # #             count += 1
# # # # #             if s in list:
# # # # #                 list.append(count)
# # # # #             else:
# # # # #                 list.append(s)
# # # # #
# # # # # print(list)
# # # # dict_wrd = {}
# # # # for i in a:
# # # #     if i in dict_wrd:
# # # #         dict_wrd[i] += 1
# # # #     else:
# # # #         dict_wrd[i] = 1
# # # #
# # # # print(dict_wrd)
# # # #
# # # # list = []
# # # # for key, value in dict_wrd.items():
# # # #     list.append(key)
# # # #     list.append(str(value))
# # # #
# # # # print(" " .join(list))
# # # #
# # # # list1 = [8,9,7]
# # # # list2 = [7,1,2]
# # # # list1.extend(list2)
# # # # print(list1)
# # #
# # # # Replace ovals
# # # # def replace_oval(old_string,replace_string):
# # # #     vowels = ('a', 'e', 'i', 'o', 'u')
# # # #
# # # #     for ele in vowels:
# # # #         old_string = old_string.replace(ele, replace_string)
# # # #
# # # #     return old_string
# # # # old_string = "Hello 1 World 2"
# # # # replace_string = ''
# # # # a = replace_oval(old_string,replace_string)
# # # # print(a)
# # # # 1.
# # # # a = '*'.join(['a','b','c'])
# # # # print(a)
# # # # 2.
# # # # s = "hello world"
# # # # a = s.split(" ")
# # # # print(a[::-1])
# # # # 3.
# # # x = "hello world"
# # # a = set(x)
# # # print(a)
# # # count = 0
# # # # dict = {}
# # # list = []
# # # for i in a:
# # #     for j in x:
# # #         if j == i:
# # #             count += 1
# # #             list.append(count)
# # #             list.append(j)
# # #
# # # print(list)
# # #
# # #
# #
# #
# # class Dates:
# #     def __init__(self, date):
# #         self.date = date
# #
# #     def getDate(self):
# #         return self.date
# #
# #     @staticmethod
# #     def toDashDate(date):
# #         print("This is static")
# #         return date.replace("/", "-")
# #
# # #
# # # class DatesWithSlashes(Dates):
# # #     def getDate(self):
# # #         return Dates.toDashDate(self.date)
# # #
# # #
# # # date = Dates("15-12-2016")
# # # dateFromDB = DatesWithSlashes("15/12/2016")
# # #
# # # if (date.getDate() == dateFromDB.getDate()):
# # #     print("Equal")
# # # else:
# # #     print("Unequal")
# # date = Dates("15-12-2016")
# # Dates.toDashDate("13-12-2012")
#
#
# #
# # ip = "aaabbccccddddd"
# # start_dict = {}
# # for i in ip:
# #     if i in start_dict:
# #         start_dict[i] += 1
# #     else:
# #         start_dict[i] = 1
# #
# #
# # print(start_dict)
# # print(type(start_dict))
# # start_list = []
# # for key, value in  start_dict.items():
# #     start_list.append(key)
# #     start_list.append(str(value))
# #
# # print("".join(start_list))
# # a = aaabbbbbmmaa
# # o = 3a5b
# # d = {a:1}
# # for i in d:
# #     if i in d:
# #         d[i +1]
# #     else:
# #         d[i] = 1
# #         {3:a,5:b,1:c}
#
# #
# # a = ['a','b'['c','d'['e','f']]]
# #
# # for i in a:
# #     print(i)
#
# #
# # a = [1,2,3,4]
# # b = list(filter((lambda b:b<2),a))
# # print(b)
# # fr = [6,5,4]
# # tr = [7,8,9]
# # print(list(zip(fr,tr))
#
# # new_list = []
# # for i in range(len(fr)):
# #     new_list.append(fr(i), tr(i))
# #
# # print(new_list)
# # def zippy(x, y):
# #     zipper = []
# #     for i in range(len(x)) :
# #         zipper.append((x[i],y[i]))
# #     return zipper
# #
# # a = zippy(fr, tr)
# # print(a)
#
# #
# # def zippy(x,y):
# #     li = []
# #     for i in range(len(x)):
# #         li.append((x[i], y[i]))
# #     return li
# # x = [1,2,3]
# # y = [5,6,7]
# # s = zippy(x,y)
# # print(s)
#
# # matrix = [[1, 2, 3], [4, 5, [6, 7, 8, 9]]]
# # li = []
# # for i in matrix:
# #     print(i)
# #     li.append()
# #     if type(i) == list:
# #         for j in i:
# #             if type(j) == list:
# #                 for k in j:
# #                     li.append(k)
# #
# # print(li)
# # create database square
# #
# # drop database square
# # create table nani(name varchar,address varchar)
# # drop table nani
# #
# # create index myinx on nani (name)
# #
# # alter table nani add name = address
#
#
#
# # a = [3,4,5,6]
# #
# # b = list(filter(lambda a:a<5,a))
# # print(b)
# #
# # c = list(map(lambda a:a+5,a))
# # print(c)
#
# # create procedure emp_info(emp_id int,emp_name varchar,emp_dep)
# # language'plpgsql'
# # as $$
# # begin
# # insert into emp_data values(emp_id,emp_name ,emp_dep);
# # commit;
# # end;
# #
# #
# # call emp_info('1','navya','teaching')
# #
# # create triger emp_trig
# # before insert
# # on table employee
# # for eack row
# #     set emp_total = sub1+sub2+sub3, emp_total*60/100
#
#
# # a = [1,2,3]
# #
# # b = [4,5,6]
# # new_list = []
# # def add_str(x,y):
# #     for i in range(len(x)):
# #         new_list.append((x[i],y[i]))
# #
# #     return new_list
# # s = add_str(x=a,y=b)
# # print(s)
# #
# import locale
#
# stringg = 'Hello 1 World 2'
# vowels = ('a','e','i','o','u')
#
# # def rem_ovl(stringg,vowels):
# #
# #     for j in vowels:
# #         if j in stringg:
# #            stringg.replace(j, " ")
# #            print(stringg)
# #     return stringg
# # a = rem_ovl(stringg,vowels)
#
#
# # g = 'Hello 1 World 2'
# # vowels = ('a','e','i','o','u')
# # for j in vowels:
# #     g = g.replace(j, '')
# # print(g)
# # def replace_oval(old_string,replace_string):
# #     vowels = ('a', 'e', 'i', 'o', 'u')
# #
# #     for ele in vowels:
# #         old_string = old_string.replace(ele, replace_string)
# #
# #     return old_string
# # old_string = "Hello 1 World 2"
# # replace_string = ''
# # a = replace_oval(old_string,replace_string)
# # print(a)
# # test_str = 'geeksforgeek'
# # halh = int(len(test_str)/2)
# # print(halh)
# # print(test_str[:halh] + test_str[halh:].upper())
#
# # v = 'geeksforgeeks'
# #
# # print(''.join(set(v)))
#
# # d = ['1','2','3'['4','5','6','7']]
# # list_1 = []
# # for i in d:
# #     if type(i)== list:
# #         print(i)
#
# # # sort
# # r = 'rashmi'
# # print(min(r))
# # l = []
# # len_str = len(r)
# # print(len_str)
# # for i in range(len_str):
# #     m = min(r)
# #     l.append(m)
# #     r = r.replace(m , '')
# #     print(r)
# # print(l)
#
#
# r = [1, 45, 21, 22, 67, 13]
# # m = min(r)
# # print(m)
# # l = []
# # len_str = len(r)
# # print(len_str)
# # for i in range(len_str):
# #     a = min(r)
# #     print(a)
# #     l.append(a)
# #     r.remove(a)
# #     print(r)
# # print(l)
# #
#
# # list1 = [10, 20, 1, 45, 99]
# # print(min(list1))
# #
# #
# #
# # sam_list = [11, 13, 15, 16, 13, 15, 16, 11]
# # len_sam_list = len(sam_list)
# # li = []
# # for i in sam_list:
# #     if i not in li:
# #         li.append(i)
# # print(li)
# #
# # l = "happy birthday"
# # c = l.split(" ")
# # print(" ".join(c[::-1]))
#
# #
# # h = 'amaama'
# # half = int(len(h)/2)
# # print(half)
# # if len(h) % 2 == 0:
# #     first_half = h[:half]
# #     sec_half = h[half:]
# #     print(first_half)
# #     print(sec_half)
# # else:
# #     first_half = h[:half]
# #     sec_half = h[half + 1:]
# #     print(first_half)
# #     print(sec_half)
# # #
# # if first_half == sec_half:
# #     print("Symetric")
# # else:
# #     print("Not Symetric")
# #
# # if first_half == sec_half[::-1]:
# #     print("palindrome")
# # else:
# #     print("not palindrome")
# # create
# # planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# # dict = {}
# # for value in planets:
# #     dict.update({value: value[0]})
# # print(dict)
# # k = "This is orange juice"
# # v = k.split(" ")
# # print(v)
# # if "orange" in v:
# #     print("Orange is present")
# # else:
# #     print("Orange not there")
#
# # s = "refrigerator"
# # count = 0
# # for i in s:
# #     count += 1
# # print(count)
#
# #
# # from collections import deque
# # q = deque()
# # q.append(1)
# # q.append(2)
# # q.append(3)
# # q.append(4)
# # print(q)
# # q.popleft()
# # print(q.__getitem__())
# # print(q)
# #
# # # mergesort
# # def mergsort(mlist):
# #     if len(mlist)> 1 :
# #         mid = int(len(mlist)/2)
# #         print("Mid %s", mid)
# #
# #         left_part = mlist[:mid]
# #         print("left_part", left_part)
# #         right_part = mlist[mid:]
# #         print("right_part %s", right_part)
# #
# #         i=j=k=0
# #         while i < len(left_part) and j < len(right_part):
# #             if left_part[i] < right_part[j]:
# #                 mlist[k] = left_part[i]
# #                 i = i+1
# #             else:
# #                 mlist[k] = right_part[i]
# #                 j = j+1
# #             k = k+1
# #
# #         while i < len(left_part):
# #             mlist[k] = left_part
# #             i = i+1
# #             k = k+1
# #
# #         while j < len(right_part):
# #             mlist[k] = right_part
# #             i = i+1
# #             k = k + 1
# #
# #     def printList(arr):
# #         for i in range(len(arr)):
# #             print(arr[i], end=" ")
# #         print()
# #     mlist = [2,4,1,6]
# #     s = mergsort(mlist)
# #     printList(mlist)
# #     print(s)
#
#
# #
# # class Node:
# #     def __self__(self,data):
# #         self.data = data
# #         self.next = None
# #         self.prev = None
# #
# # class doublelinklist:
# #     def __init__(self):
# #         self.head = None
# #
# #     def push(self, NewVal):
# #         NewNode = Node(NewVal)
# #         NewNode.next = self.head
# #         if self.head != Node:
# #             self.head.prev = NewNode
# #         self.head = NewNode
# #
# #     def insert(self, node):
#
# # def binary():
# #     serch_list = [5,34,65,78,82,91]
# #     serch_key = 4
# #
# #     first =0
# #     last = len(serch_list)-1
# #     find = False
# #
# #     while first <= last and not find:
# #         mid = (first + last) // 2
# #         print(mid)
# #
# #         print(serch_list[mid])
# #         if serch_key == serch_list[mid]:
# #             find = True
# #             print("Find %s",  find)
# #         else:
# #             if serch_key < serch_list[mid]:
# #                 last = mid -1
# #                 print("Last %s", last)
# #             else:
# #                 first = mid +1
# #                 print("first %s", first)
# #     return find
# #
# #
# #
# #
# # a = binary()
# # print("Outside %s", a)
# #
#
# # Correct selection sort
# # def selectionSort(array, size):
# #     for step in range(size):
# #         min_idx = step
# #         print("min_idx %s", min_idx)
# #
# #         for i in range(step + 1, size):
# #
# #             # to sort in descending order, change > to < in this line
# #             # select the minimum element in each loop
# #             print("I value %s", i)
# #             if array[i] < array[min_idx]:
# #                 print(array[i])
# #                 min_idx = i
# #
# #         # put min at the correct position
# #
# #         temp = array[step]
# #         array[step] = array[min_idx]
# #         array[min_idx] = temp
# #
# # data = [-2, 45, 0, 11, -9]
# # size = len(data)
# # selectionSort(data, size)
# # print('Sorted Array in Ascending Order:')
# # print(data)
# #
#
# # quick sort
# # function to find the partition position
# # def partition(array,low,high):
# #     piot = array[high]
# #     print("piot %s", piot)
# #
# #     i = low - 1
# #     for j in range(low, high):
# #         print("j th %s", j)
# #         if array[j] <= piot:
# #             i = i + 1
# #             print("array[i] %s", array[i])
# #             temp = array[i]
# #             array[i] = array[j]
# #             array[j] = temp
# #     (array[i + 1],array[high]) = (array[high], array[i + 1])
# #
# #     return i + 1
# #
# # def quicksort(array,low,high):
# #     if low < high:
# #         pi = partition(array, low, high)
# #
# #         quicksort(array, low, pi - 1)
# #         quicksort(array, pi + 1, high)
# #
# # data = [8, 7, 2, 1, 0, 9, 6]
# # print("Unsorted Array")
# # print(data)
# #
# # size = len(data)
# #
# # quicksort(data, 0, size - 1)
# #
# # print('Sorted Array in Ascending Order:')
# # print(data)
#
#
# # def bubbleSort(nlist):
# #     for passnum in range(len(nlist)-1,0,-1):
# #         print("passnum %s", passnum)
# #         for i in range(passnum):
# #             if nlist[i]>nlist[i+1]:
# #                 temp = nlist[i]
# #                 nlist[i] = nlist[i+1]
# #                 nlist[i+1] = temp
# #
# # nlist = [14,46,43,27,57,41,45,21,70]
# # bubbleSort(nlist)
# # print(nlist)
#
# # bubble sort
# # def buble(nlist):
# #     for part in range((len(nlist)-1),0,-1):
# #         for i in range(part):
# #             if nlist[i] > nlist[i+1]:
# #                 temp = nlist[i]
# #                 nlist[i] = nlist[i+1]
# #                 nlist[i+1] = temp
# nlist = ["2","33","4","21"]
# print("".join(nlist))
# # buble(nlist)
# # print(nlist)
# # liat = [1,2]
# # list2 = [3,4]
# # list1.appens(list2)   [1,2,3,4]
# # for key, value in dict.items():
# #     liat.append(key)
# #
# # object.k;m23321
# # __
# # l = "welcome dollar"
# # a = l.split(" ")
# # print(l.split(" "))
# #
# # # def selectionsort(array,low,high):
# #     for i in range(len(array)):
# #         min = i
# #         for j in range(i + 1, array[high]):
# #             if j['']
# # def sort(array):
# #
# #     for part in range(len(array)):
# #         min = part
# #         for i in range(len(array)-1,):
#
# #     for part in range(len(A)-1,0,-1):
# #         for i in range(part):
# #             if(array[i]>array[i+1]):
# #
# #
# #                 temp = array[i]
# #                 array[i] = array[i+1]
# #                 array[i+1] = temp
# # A = [64, 25, 12, 22, 11]
# # sort(array=A)
# # print(A)
#
#
# # def select(array):
# #     for step in range(len(array)):
# #         min = step
# #         for i in range(step + 1, 4):
# #             if array[i] < array[min]:
# #                 min = i
# #         temp = array[step]
# #         array[step] = array[min]
# #         array[min] = temp
# # array = [88,4,65,3]
# #
# # select(array)
# # print(array)
#
# # def selectionSort(array, size):
# #     for step in range(size):
# #         min_idx = step
# #         print("min_idx %s", min_idx)
# #
# #         for i in range(step + 1, size):
# #
# #             # to sort in descending order, change > to < in this line
# #             # select the minimum element in each loop
# #             print("I value %s", i)
# #             if array[i] < array[min_idx]:
# #                 print(array[i])
# #                 min_idx = i
# #
# #         # put min at the correct position
# #
# #         temp = array[step]
# #         array[step] = array[min_idx]
# #         array[min_idx] = temp
# #
# #
# # def parttion(array,low,high):
# #     print("low %s", low)
# #     print("high %s", high)
# #     mid = (low + high)//2
# #     print(mid)
# #     pivote = array[high-1]
# #     print("pivote %s", pivote)
# #     i = low - 1
# #     for j in range(low,high):
# #         if array[j] <= pivote:
# #             i = i + 1
# #             temp = array[i]
# #             array[i] = array[j]
# #             array[j] = temp
# #
# #
# #
# # array = [33,42,3,51,2]
# # low = 0
# # high = len(array)
# #
# # def quicksort(array,low,high):
# #     if low < high:
# #         pi = parttion(array,low,high)
# #         quicksort(array, low, pi -1)
# #         quicksort(array, pi + 1, high)
# #
#
# # import django
# # print(django.__version__)
#
#
# # def gener(arg):
# #     for i in arg:
# #         yield (i * i)
# # a = gener([1,2,3,4])
# # for i in a:
# #     print(i)
#
# # def gen(arg):
# #     li = []
# #     for i in arg:
# #         li.append(i*i)
# #     print(li)
# #
# # a = gen(arg = [1,2,3,4,5])
# # print(a)
#
# # importing the multiprocessing module
# #
# # import multiprocessing
# #
# #
# # def cube(n):
# #     # This function will print the cube of the given number
# #     print("The Cube is: {}".format(n * n * n))
# #
# #
# # def square(n):
# #     # This function will print the square of the given number
# #     print("The Square is: {}".format(n * n))
# #
# #
# # if __name__ == "__main__":
# #     # creating two processes
# #     process1 = multiprocessing.Process(target=square, args=(5,))
# #     process2 = multiprocessing.Process(target=cube, args=(5,))
# #
# #     # Here we start the process 1
# #     process1.start()
# #     # Here we start process 2
# #     process2.start()
# #
# #     # The join() method is used to wait for process 1 to complete
# #     process1.join()
# #     # It is used to wait for process 1 to complete
# #     process2.join()
# #
# #     # Print if both processes are completed
# #     print("Both processes are finished")
# #
# #
# #     onj = class1()
# #     class1.function
#
# # from ...models import EmployeeInfo
# #
# #
# #
# # def review_data():
# #     q = EmployeeInfo.objects.all()
# #     print(q)
# #
# #
# # review_data()
# # # l = [2,3,4,5]
# # print(l)
# # y = [2,5j,6]
# # c = y.sort
# #
# #
# # # for ?int()
# # print(c)
# a = [1,2,3]
# # # b = [sum(a[0:x+1]) for x in range(0, len(a))]
# # b = list(map(lambda x:2**x,a))
# # print(b)
# # print([i.lower() for i in "TURING"])
#
# # def list(val,list[]):
# #   list.append(val)
# # print((list(map(lambda x:x+1, a))))
#
# # l1 = [1,2,6,12]
# # l2 = [12,6,2,1]
# # print(l1 == l2)
# # print(set(l1) == set(l2))
# # a = ['wel','to','tu']
# # print("-".join(a))
#
# # t = '%(a)s %(b)s %(c)s'
# # print(t %dict(a='wel', b='to',c='ty'))
# # def f(x, l=[]):
# #     for i in range(x):
# #         l.append(i*i)
# #         print(l)
# # f(2)
# # f(3,[3,2,1])
# # f(3)
#
# # def f1():
# #     x = 50
# #     return x
# # f1()
# # print(x)
#
# # z = set('abc')
# # z.add('san')
# # z.update(set(['p','q']))
# # print(z)
#
# # x = "abcdef"
# # i = "a"
# # while i in x[:-1]:
# #     print(i, end="")
# # from functools import reduce
# # ops = ["5", "-2","4","c","d","9","+","+"]
# # return_list = []
# # list2_result = []
# # first_iter = False
# # for i in ops:
# #    if i.isalpha() and len(return_list) != 0:
# #        if first_iter != True:
# #           return_list.pop()
# #           first_iter = True
# #        else:
# #
# #            list1_result = return_list[-1]
# #            print("list1_result", list1_result)
# #            print(return_list[-1])
# #            new_input = int(2) * int(list1_result)
# #            return_list.append(int(new_input))
# #
# #    elif i == '+':
# #        print("*****", i)
# #        print("type", type(i))
# #        list2_result = return_list[-1]
# #        print("list2_result %s", list2_result)
# #        print("list2_result type %s", type(list2_result))
# #        list3_result = return_list[-2]
# #        print("list3_result %s", list3_result)
# #        print("list3_result %s", type(list3_result))
# #        list4_result = int(list2_result) + int(list3_result)
# #        return_list.append(int(list4_result))
# #    else:
# #        return_list.append(int(i))
# #
# # print("@@@@@@")
# # print(return_list)
# #
# # a = reduce(lambda a,b: a+b,return_list)
# # print(a)
# num = [1,2,3,4,3]
# dict = {}
# max_element  = max(num)
#
# print("****", a)
# print(a)
# start_dict = {}
# for i in num:
#     if i in start_dict:
#         start_dict[i] += 1
#     else:
#         start_dict[i] = 1
#
# print(start_dict)
#
# new_list = []
# for key, value in start_dict.items():
#     print(key)
#     print(value)
#     if value > 1:
#         new_list.append(key)
#
# miss_ele = max_element + 1
# print(miss_ele)
# print(new_list)
# new_list.append(miss_ele)
# print(new_list)
# # num = [1,2,3,4,3]
# # dict = {}
# # max_element  = max(num)
# #
# # print("****", a)
# # print(a)
# # start_dict = {}
# # for i in num:
# #     if i in start_dict:
# #         start_dict[i] += 1
# #     else:
# #         start_dict[i] = 1
# #
# # print(start_dict)
# #
# # new_list = []
# # for key, value in start_dict.items():
# #     print(key)
# #     print(value)
# #     if value > 1:
# #         print("**")
# #         num.remove(key)
# # print(num)
# # miss_ele = max_element + 1
# # print(miss_ele)
# # print(new_list)
# # new_list.append(miss_ele)
# # print(new_li
# # st)

from PIL import Image

im = Image.open('/home/rashmihk/Downloads/nataraj.jpeg')

print(im.size)
print(type(im.size))
# (400, 225)
# <class 'tuple'>

w, h = im.size
print('width: ', w)
print('height:', h)



# ajay manager account 45000 \n sunil clerk account 25000\n varun manager sales 50000 \n amit manager account 47000 \n tarun peon sales 15000 \n deepak clerk sales 23000 \n sunil peon sales 13000 \n satvik director purchase 80000
