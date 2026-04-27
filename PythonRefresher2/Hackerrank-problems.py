#In this challenge, the user enters a string and a substring.
#  You have to print the number of times that the substring occurs in the given string.
#  String traversal will take place from left to right, not from right to left.

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

##########################################################################################

#You are given a string and your task is to swap cases. In other words, convert all lowercase
#letters to uppercase letters and vice versa.

# Www.HackerRank.com → wWW.hACKERrANK.COM

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

#################################################################################################
#
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen


def split(str):
    splitstr= str.split(" ")
    joinstr= "_".join(splitstr)
    return joinstr

str = input("Enter a string : ")

sp = split(str)
print(sp)