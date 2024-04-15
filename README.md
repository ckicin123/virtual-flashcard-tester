# virtual-flashcard-tester
flash cards but online and smarter

this program works by putting data into the data file and running the other file in python (installation at bottom)

in the data file if you type in:
example#answer#0

this will be interpreted as something for the program to test you on

"example" will be interpreted as the left side
"answer" will be interpreted as the right side
"0" will be a score of those 2 and how well you memorised them (always set this to 0 preferably)

(notice how the # splits the 3 apart)

(do not miss out on reading this line)-you can type in as many of the "example#answer#0" lines as you want and they will all be interpreted induvidually allowing you to add as many as you want

after you have put in data running the program will give you 2 choices:
- going from left to right
- going from right to left

for this example i will assume that the user has chosen left to right

after this the program will randomly pick from the lines you have worse memorised and test you on them
in the case of the data file only having "example#answer#0" in it the output would be:

what is

example

on the other side?
: (input prompt)

if you type in the other side correctly (in this case "answer") it will deem you correct 
if you don't type it correctly incase of typos or not wanting to type and just wanting to think of the answer there is a prompt that asks you if you were correct
every time you don't type it in perfectly character by character correct it will give you the answer and ask if you were correct

ACTUAL APPLICATIONAL USE:

let's say you typed in the data file:

first spanish word#english definition of word#0
second spanish word#english definition of 2nd word#0



now when you run the code it will ask you once again for:
- left to right
or
- right to left

now let's say the user chose left to right again

the output of the program:

what is

first spanish word

on the other side?
: (input prompt)



this is good as it tests if you know the spanish word in english helping you memorise it

INSTALLATION:
copy the file "memory helper" into your file explorer and run the python file inside called "memorytester" to use the program and of course edit the file "data" to add data for the program to work with

good thing to note is that the score increases faster the more you get correct in a row so words you definitely have memorised you'll get much less of

if you were to get this prompt correct it would then ask you for the second spanish word on the other side and so on

KEEP IN MIND if you chose right side to left side, in this example it would give a english definition and expect you to give the spanish word for it
