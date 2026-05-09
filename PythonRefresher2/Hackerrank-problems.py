# #In this challenge, the user enters a string and a substring.
# #  You have to print the number of times that the substring occurs in the given string.
# #  String traversal will take place from left to right, not from right to left.

def count_sub_string(s,t):
    count =0
    for i in range( len(s)):
       m = s[i:i+len(t)]
       if(m==t):
           count= count+1
           
    return count


str= input("Enter a string: ")
substring = input("Enter a substring: ")

count = count_sub_string(str,substring)
print(count)

# ##########################################################################################

# #You are given a string and your task is to swap cases. In other words, convert all lowercase
# #letters to uppercase letters and vice versa.

# # Www.HackerRank.com → wWW.hACKERrANK.COM

def swap(str):
    s=""
    for i in range(len(str)):
        if(str[i].isupper()):
            s+=(str[i].lower())
        else:
            s+=(str[i].upper())


    return s 

str = input("Enter a string: ")
swap_string= swap(str)
print(swap_string)

# #################################################################################################
# #
# # You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen


def split(str):
    splitstr= str.split(" ")
    joinstr= "_".join(splitstr)
    return joinstr

str = input("Enter a string : ")

sp = split(str)
print(sp)

# #######################################################################################

# # Given an integer, , perform the following conditional actions:

# # If  is odd, print Weird
# # If  is even and in the inclusive range of 2 to 5, print Not Weird
# # If  is even and in the inclusive range of 6 to 20, print Weird
# # If  is even and greater than 20, print Not Weird
def printCondn(j):
    if(j%2==0 and 2<j<5):
        print("Not Weird")
    if(j%2==0 and 6<j<20):
         print(" Weird")
    if(j%2==0 and j>20):
         print(" Not Weird")
    else:
        print(" Weird")
     

i = (int)(input)("Enter and integer: ")

printCondn(i)

# ########################################################################################

# #Given the participants' score sheet for your University Sports Day, 
# # you are required to find the runner-up score. You are given  scores. 
# # Store them in a list and find the score of the runner-up.

def findrunnerup(i):
   i = list(map(int, i))
   i.sort()  
   print(i)
   return i[-2]

i = (input)("Enter scores: ").split()

print(findrunnerup(i))

# ##############################################################################################

# #Given an array of integers nums and an integer target, return indices of the two numbers 
# # such that they add up to target.
# #nums = [2,7,11,15], target = 9

def twoSum( nums, target) :
    my_list=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[j] + nums[i]== target):
                my_list.extend([i,j])

    return my_list





nums =  list(map(int, input("Enter integers: ").split()))
target = int(input("Enter target: "))
print(twoSum(nums,target))
# ###############################################################################

# # Write a function to find the longest common prefix string amongst an array of strings.

# # If there is no common prefix, return an empty string 

# #strs = ["flower","flow","flight"]

def findCommon(strs):
    my_string=""
    strs.sort()
    shortest_length_string= strs[0]
    for i in range(len(shortest_length_string)):
        first_char=shortest_length_string[i]
        for s in strs:
           if(s[i] != first_char):
             return my_string
        my_string += first_char   

    return my_string


strs= input("Enter the array: ").split()
print(findCommon(strs))

############################################################################

#Given a string s consisting of words and spaces, return the length of the last word 
# in the string.

s= "Hello World banerjee"
strs=s.split()
length = len(strs[-1])
print(length)

##############################################################

def compareTriplets(a, b):
   count_a=0
   count_b=0

   for i in range(len(a)):
        if(a[i] > b[i]):
            count_a=count_a+1
          
        elif(a[i]<b[i]):
            count_b=count_b+1
            
   return [count_a,count_b]

a = list(map(int, input("Enter integers: ").split()))
b = list(map(int, input("Enter integers: ").split()))

result = compareTriplets(a, b)
print(result)

##################################################################

def merge_the_tools(string, k):
    # your code goes here
    length=len(string)
   
    
    for i in range(0,length,k):
      substring = string[i:i+k]
      unique=""
      for ch in substring:
         if ch not in unique:
            unique+=ch
         
           
      print(unique)
          
            
          
str= input("Enter the string :")
variable = int(input("enter integer"))
merge_the_tools(str,variable)
###################################################
from collections import Counter
def price_calculation(no_of_shoe,shoe_size_list,no_of_customer,customer_list):
   total_price =0
   d=Counter(shoe_size_list)
   print(d)

   size_count =0
   
   for size,price in customer_list:
         if size in d.keys() and d[size]>0 :
               
               total_price +=price
               d[size] = d[size]-1

   print(total_price)
         
      
no_of_shoe = int(input("enter no of shoe: "))
list_shoe_size=list(map(int, input("Enter list of shoe size: ").split()))
no_of_customer = int(input("Enter no of customer: "))
customer =[]
for i in range(no_of_customer):
    size, price = map(int, input().split())
    customer.append((size,price))
price_calculation(no_of_shoe,list_shoe_size,no_of_customer,customer)

###########################################################################
from collections import Counter
def top3mostcommonchar(str1):
     l=[]
     for ch in str1:
          l.append(ch)

     d = Counter(l)
     sortd=sorted(d.items(), key= lambda x: (x[1],x[0]),reverse=True)
     for key,value in sortd[:3]:
          print (key ,value)
     
          

str1 = input("Enter string: ")
top3mostcommonchar(str1)