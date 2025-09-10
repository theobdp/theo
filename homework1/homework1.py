
# --- Variable and Data Types ---

a = 10
print(a)
print(type(a))
#int, which is basically just an integer value

b = 1.5
print(b)
print(type(b))
#float, which is a number with a decimal point

c = 3j
print(c)
print(type(c))
#complex, which is a complex number where the j represents the imaginary component

d = "hello"
print(d)
print(type(d))
#string, which is a word or text

e = [1,2,3]
print(e)
print(type(e))
#list, collection of items that you can move around

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
#dict, collection of pairs that are like keys for each other

g = (1,2)
print(g)
print(type(g))
#tuple, like a list, but you can't move the items around

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
#list, but with different data types as the items

i = True
print(i)
print(type(i))
#bool, which is a boolean, either true or false

j = None
print(j)
print(type(j))
#NoneType, which is basically an N/A

k = [True, "blue", 12]
print(k)
print(type(k))
#list, but you can use different data types in one list

l = str(14)
print(l)
print(type(l))
#string, the string version of 14. basically l is "14"

m = 1e4
print(m)
print(type(m))
#float, this is scientific notation and it seems to default to being a float

#1. 9
#2. String, int, float, complex, list, tuple, boolean, NoneType, dict
#3. b m, k h e
#4. Because the command str() converted 14 to "14"
#5. A set, which is defined using {}. Duplicate items are removed. Items can be moved around. 

print("-----------------------------------")

print(10>9) #T
print(10==9) #F
print(10 <= 9) #F
print(bool("abc")) #T
print(bool(123)) #T
print(bool(["apple", "cherry", "banana"])) #T
print(bool(True)) #T
print(bool(False)) #F
print(bool(0)) #F
print(bool("")) #F
print(bool(" ")) #T
print(bool()) #F
print(bool([])) #F
print(bool({})) #F

print("------")

print(bool(True and False)) #F
print(bool(True and True)) #T
print(bool(False and False)) #F
print(bool(True or False)) #T
print(bool(True or True)) #T 
print(bool(False or False)) #F
print(bool(not(False))) #T
print(bool(not(True))) #F

#1. Booleans return either true or false, it returns true if what's inside is "real." If the statement inside is false, it returns false.  
#2. The one with print(bool(" ")). I thought this would return false like the rest of the ones around it.
#3. bool(1 == 1). This is true because 1 is equal to 1.
#4. bool(1+1 == 3). This is false because the statement inside is simply false. 1+1 != 3

print("---------------------")
print(10+5) #adds
print(10-5) #subtracts
print(2*4) #multiply
print(6/3) #divide, makes a float
print(5%2) #modulo, finds remainder if divided
print(3**2) #exponent, 3 to the second power
print(15//2) #divide, rounds down and makes an int
print("-----")
print(5==2) #is it equal? false
print(10 != 10) #is it not equal? false
print(2<5) #less than? true
print(12>5) #greater? true
print(5<=6) #less than or equal? true
print(1>=10) #greater than or equal? false

print("-----")
x=5
x-=4
x*=3
print(x)

print(bool(not(" ")))

#1. It compares two things, if their outputs are the same it is true, if not it is false. bool("hi" and 1) returns true, bool("hi" and 0) is false.
#2. Also compares, but will print true unless both outputs are false. bool("hi" or 0) is true, bool("" or 0) is false. 
#3. It makes the boolean the opposite of what it is. bool(not(" ")) is false, bool(not("")) is true. 


#1. One is divide, results in a float. The other is divide but chop the decimal, rounding down and making an int. 
#2. One is remainder, the other is dividing with no remainder. 
#3. The % one. 6%4 = 2
#4. They operate on the variable, setting it to something new. -=4 subtracts 4 from the current value of the variable. 

print("--------")
mystring = "hello"
print(mystring)
print(mystring[0])
print(mystring[1])
print(mystring[2])
print(mystring[3])
print(mystring[4])
print(mystring[-1])
print(mystring[1:3])
print(mystring[0:5:2])
print(len(mystring))
print(mystring + "goodbye")
print(7 * mystring)

name = "Oski"
print("Hello, my name is", name)
print(f"Hello, my name is {name}")

#1. Slicing is basically taking just a part of a string. A string is a collection of characters so you can choose which one you want. 
# In the ones where we had mystring[]
#2. It printed "hello, my name is oski"
#3. It printed the same thing as #2. 
#4. The third one has an f and the name variable is in curly brackets. The f makes it formatted better. 


#Terminal Commands
#cd: changes directories. move from one folder to another, cd python_decal_fa25
#ls: lists everything in the directory where you are. just call ls
#ls -a: lists everything in the directory including hidden files. ls -a
#mkdir: makes a directory in the directory where you are. basically makes a new folder. mkdir newfolder
#cat: concatenates. displays whatever is in a file. cat homework1.py
#pwd: prints where you are, what directory you are in and how you got there. pwd
#cd ..: moves up a directory, so you go to the parent directory of whatever you are in. cd ..
#cd .: doesn't seem to do much, kind of just keeps you where you are. cd .
#cd ~: moves you back to the root directory. cd ~
#cp: copies a file. cp homework1.py Desktop
#mv: moves a file or directory. mv homework1.py Desktop
#rm: removes a file or directory. rm homework1.py
#clear: clears the terminal screen. very helpful if you've called a lot of commands and you want to do something new. 
#grep: basically a search feature. it finds and shows all files within a directory that have a certain keyword. grep .py would show all files with .py


#1. touch: creates a file (not a directory). touch test.py
# echo: prints whatever comes after it into the terminal output. echo "hi there"
# curl: copies a url and the data within it, can be used for downloading content from a website. 
#2. ls lists the files that aren't hidden, while ls -a is forced to list everything that is there, including hidden files. 
#3. A file that isn't listed by ls, but is still there. 
#4. -r is a flag for the cp command, if you are copying a directory it copies everything that was in all the child directories too. 
# -i is a flag for the mv command, which makes terminal ask for confirmation if a file was going to overwrite another at the destination. 
# -f is a flag for the rm command, which forces removal of a file without confirmation