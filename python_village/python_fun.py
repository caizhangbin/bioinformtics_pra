#import this
print ("Hello World!")

a = 324
b = 24
c = a - b
print (c)
print (('a + b is'), a + b)

###
 
# Problem

# Given: Two positive integers a and b, each less than 1000.

# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
####

d = 958
e = 880

z = (d**2 + e**2)
print (z)

####
# Given: A string s of length at most 200 letters and four integers a, b, c and d.

# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
####

s = 'FEhluyoIgzOAFICYKgge6m8LwwdgdyaNOuCVkeBQYAjJPzaIfizhxhLeuciscusFrxJHJgrR5yydSgQsTbnwrUVu93HT8DKbXWNoFdulkeitianaYHeoOKDD3uUyK8vtfm34GunrboQG9DsVXRqgbsmO3R7mvzCbxjOCB.'
x = (54, 62, 101, 111)


y = s[54: 63] +' ' + s[101: 112]
print (y)

####
# Given: Two positive integers a and b (a<b<10000).

# Return: The sum of all odd integers from a through b, inclusively.
####
sum = 0
for x in range(4558 ,9058):
    if x % 2!= 0:
        sum = sum + x

print (sum)
    


###
# Given: A file containing at most 1000 lines.

# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

i = 1

f = open ("../python_village/txt/rosalind_ini5.txt", "r")

f2 = open ("../python_village/txt/output1.txt", "w")

f2.write ( "Even-numbered lines from rosalind_ini5.txt:\n" )
f2.write ( "----------\n" )
for line in f:
    if i % 2 == 0:
        f2.write (line)
    i += 1
    
f.close
f2.close

###
# Given: A string s of length at most 10000 letters.

# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
###

str = "We tried list and we tried dicts also we tried Zen"

for word in str.split(' '):
    print (word)

for key, value in dict.items():
    print (key)
    print (value)