'''Questions provided by Rishu Garg (as of Nov2, 2017)
Answers by Prabal Dev
'''


'''1. Create a program file (say ’program1.py’), write python statements to
assign a variable to the string ”Hello World!” and print the value of the
variable. You should get comfortable with running programs from files'''
hey = "Hello World!"
print("ques1")
print(hey)
'''2. Try out different mathematical operators (+,-,*,/,**,%) on numbers'''
a = 3
b = 4
print("ques2")
print(a+b, a-b, a*b, a/b, a**b, a%b)
'''3. Write python statements (without using math library) to compute the
value of:
•
√4 −19 + 1002 − 3×6.55
√3 −1200'''
print("ques3")
print(4**0.5 -9 +1002 - 3*6.55)
print(3**0.5 -1200)
'''4.  Run the following python commands and identify what does each com-
mand do:

>>> a = 9.0; b = 9; c = 4
>>> print a / c
>>> print b / c
>>> print a // c
>>> print c / b
>>> print c / a
Why does the output of a / c and b / c different? Similarly, the output
of c / a and c / b?'''
a = 9.0
b = 9 
c = 4
print("ques4")
print(a/c)
print(b/c)
print(a//c)
print(c/b)
print(c/a)
'''5. Try out different relation operators (==, !=, <, >, <=, >=) for different
data types (integers, strings, etc.). These operators work on all types, not
just numbers, and return a boolean value. Make sure you understand how
to use them and what they are used for.'''
print("ques5")
a = "abc"
b = "ABC"
c = "65"
d = 65
print(a==b)
print(c==str(d))
'''6. For a quadratic equation ax2 + bx + c, take as input a, b and c from the
user. Write a program that computes the roots of this quadratic equation.
(Note: Do handle the case when roots are complex numbers)'''
import math
def quad_roots(a, b, c):
    D = b**2-4*a*c
    E = (math.sqrt(abs(D)))/(2*a)
    F = (-b)/(2*a)
    if D>=0:
        print("root1 = ", F + E)
        print("root2 = ", F - E)
    else:
        print("root1 = ", F, "+", E,"i")
        print("root2 = ", F, "-", E,"i")
print("ques6")
quad_roots(1,1,1)
quad_roots(1,5,1)
'''7. Given a string S = "Hello World!". Try different string indexing. For
example, try the following:
>>> S[1]
>>> S[-1]
>>> S[0:4]
>>> S[6:]
>>> S[:-1]
>>> S[:]
>>> S[::]
>>> S[::2]
>>> S[:3]+S[-2:]

Make sure you understand what each of the following outputs before pro-
ceeding forward.'''
S = "Hello World!"
print("ques7")
print(S[-1])
print(S[0:4])
print(S[6:])
print(S[:-1])
print(S[::])
print(S[:])
print(S[::2])
print(S[:3]+S[-2:])
'''
8. Try the commands from previous problem for list L = [1,2,3,4,5,6,7,8,9].
This problem is to understand that the indexing of elements is similar for
all sequence data types like string and list.'''
print("ques8")
L = [1,2,3,4,5,6,7,8,9]
print(L[:3]+L[-2:])
print(L[:3])
'''9. Write a program to print the reverse of a string.'''
print("ques9")
# method 1
print(S[::-1]) # by slicing
# method 2 by recursion
def rev_recursion(s):
    if len(s) == 0:
        return s
    else:
        return rev_recursion(s[1:])+s[0]
# method 3 by iteration
def rev_loop(s):
    rev_s = ""
    for i in s:
        rev_s = i + rev_s
    return rev_s
print(rev_recursion(S))
print(rev_loop(S))
'''10. Given a list of numbers A, create a new list B such that 
ith element of list
B is the sum of first i + 1 elements of A.
Example: A = [2, 3, 5, 7]
Your program should output: [2, 5, 10, 17]'''
A = [2, 3, 5, 7]
B = []
B.append(A[0])
for i in range(1,len(A)):
    B.append(B[i-1]+A[i])  
print("ques10")
print(B)
'''11. Write a program that initially has a list A containing n strings and pro-
duces a dictionary with the strings of the list A as keys and the corre-
sponding lengths of the strings as values.

Example: A = [’hello’, ’how’, ’are’, ’you?’]
Your program should output: {’hello’:5, ’how’:3, ’are’:3, ’you?’:4}'''
print("ques11")
A = ['hello', 'how', 'are', 'you?']
dict ={}
for x in A:
    if not x in dict:
        dict[x] = len(x)
print(dict)
'''12. Write a program which given an input number n, produces a list that
contains tuples (i, i2, i3) for all numbers i from 0 to n inclusive.'''
print("ques12")
def custom(n):
    L = []
    for i in range (0,n+1):
        T = ()
        for j in range (0, i+1):
            T = T + (j,)
        L.append(T)
    return L
print(custom(4))
'''13. Write a program that prints the sum of all even numbers in a list.'''
print("ques13")
L = [1,2,3,4,5,6,7,8,9,0]
def even_sum(L):
    sum = 0
    for x in L:
        if x % 2 == 0:
            sum += x
    return sum
print(even_sum(L))
'''14. Write a program that takes three numbers as input from the user and
prints the maximum and minimum of the three numbers.'''
print("ques14")
#try:
#    a = int(input("Enter a number "))
#    b = int(input("Enter another number "))
#    c = int(input("Enter last number "))
#except TypeError:
#    print("nan")
#except:
#    print("Something went wrong!")
#gr = max(a,b)
#greatest = max(c,gr)
#ls = min(a,b)
#least = min(c,ls)
#print("greatest = ", greatest, "least = ", least)
#print(max(max(a,b),c))
#print(min(min(a,b),c))
'''15. Write two programs to print the following pattern using
(a) while loop
(b) for loop
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7'''
print("ques15")
i = 1
j = 1
while(i<=7):
    while j <= i:
        print(str(j)+" ", end="")
        j +=1
    i+=1
    j = 1
    print("\n")
for i in range(1,8):
    for j in range(1,i+1):
        print(str(j)+" ", end="")
    print("\n")
'''16. A word or a phrase is a palindrome if it reads the same backwards as

forwards, for example: ”radar”, ”Was it a rat I saw?” (ignoring the punc-
tuation, capitalization and spacing). Write a program to check whether

the input string is a palindrome or not.'''
print("ques16")
#def isPalindrome(s):
#    newS = ""
#    s= s.lower()
#    for x in s:
#        if x in "abcdefghijklmnopqrstuvwxyz":
#            newS = newS + x
#    revS = newS[::-1]
#    if newS == revS:
#        return True
#    else:
#        return False
#another method by recursion
def isPalindrome(s):
    newS = ""
    s= s.lower()
    for x in s:
        if x in "abcdefghijklmnopqrstuvwxyz":
            newS = newS + x
    def isPal(s):
        if len(s)==1:
            return True
        else:
            return (s[0]==s[-1] and isPal(s[1:-1]))
    return isPal(newS)
print(isPalindrome("Was it a rat I saw?"))
'''17. A pangram is a sentence that contains all the letters of the English al-
phabet at least once, for example: ”The quick brown fox jumps over the

lazy dog”. Write a program which takes as input a sentence and prints
whether the sentence is a pangram or not.'''
def check_pangram(s):
    s = s.lower()
    newS = ""
    freq = {}
    for x in "abcdefghijklmnopqrstuvwxyz":
        freq[x] = 0
    for x in s:
        if x in "abcdefghijklmnopqrstuvwxyz":
            newS = newS + x
            freq[x] = freq[x]+1
    Occurences = freq.values()
    if 0 in Occurences:
        return False
    else:
        return True
print("ques17")
print(check_pangram("The quick brown fox jumps over the lazy dog."))
'''18. Write a program to determine the result of two-player Rock-Paper-Scissors
game. Ask the user for what the players played (using input), check if the
inputs are valid (i.e. either of ’rock’, ’paper’ or ’scissor’), compare them,
print out a message of congratulations to the winner, and ask if the players
want to start a new game. If yes, repeat the game, otherwise terminate
the program.
Rules of the game: Rock beats Scissors, Scissors beats Paper, Paper beats
Rock.'''
#def RPS(usr1, usr2):
#    usr1 = usr1.lower()
#    usr2 = usr2.lower()
#    points = {"rock":3,"scissor":2,"paper":1}
#    if (usr1 not in points) or (usr2 not in points):
#        return "bad arguments passed"
#    point_usr1 = points[usr1]
#    point_usr2 = points[usr2]
#    if point_usr1 > point_usr2:
#        player_num = 1
#    elif point_usr1 == point_usr2:
#        player_num = 0
#    else:
#        player_num =2
#    if player_num != 0:
#        return "player"+ str(player_num) + " wins!"
#    else:
#        return "match draw"
#print("ques18")
#resume = ["Y","y","YES","yes","1","Yes"]
#choice = "YES"
#while(choice in resume):
#    print("rock,scissor,paper")
#    usr1 = input("PLAYER 1 enter any one from above>>")
#    usr2 = input("PLAYER 2 enter any one from above--")
#    print(RPS(usr1,usr2))
#    print("Wanna play again?", end="")
#    choice = input()
'''19. One string is an anagram of another if the second is simply a rearrange-
ment of the first. For example, ’heart’ and ’earth’ are anagrams. The

strings ’python’ and ’typhon’ are anagrams as well. For the sake of sim-
plicity, assume that the two strings in question are made up of 26 low-
ercase alphabetic characters. Write a program that will take two strings

and prints a boolean value whether they are anagrams.'''
def anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    components1 = []
    components2 = []
    if(len(s1)==len(s2)):
        components1 = sorted(s1)
        components2 = sorted(s2)
        if components1 == components2:
            return True
        else:
            return False
    return False
print("ques19")
print(anagram("python","typhon"))

