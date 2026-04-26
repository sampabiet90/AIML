# Write a program to count no. of vowels and print all the vowels.

str= 'sampa banerjee'
vowels = 'AEIOUaeiou'
count=0
l=[]

for s in str:
    if (s in vowels):
        l.extend(s)
        count= count+1
print(count)
print(l)
