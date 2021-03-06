# Code Breakers
A collection of Python scripts that help solve puzzles in the "Code Breakers" puzzles and other word puzzles.
A list of puzzles that can be solved with these scripts:
- Cryptograms (Dell, Code Breakers)
- Crypto-Kross (Dell, Code Breakers)
- Letter, Please (Dell, Code Breakers)
- Letter Replacement (Dell, Code Breakers)
- Jumble (PennyPress) 
- 4 Pics 1 Word
- Scrabble

#The Scripts:

#CryptogramSolver.py
CryptogramSolver.py takes a cryptogram coded phrase as input. It then does letter frequency analysis and filters against a dictionary file and reduces the coded phrase down to a small number of possible solutions. Lots of times it filters the phrase down to just one solution!

<b>Example:</b> CryptogramSolver.py "alvaml bql vd xol qvbs xv ketsvu kold xolc qlbmeyl xoleq vaedevdt bql vdmc vaedevdt"
<br><b>Output:</b> people are on the road to wisdom when they realize their opinions are only opinions

#WordCracker.py
WordCracker.py: takes a bunch of letters as input and cross references a dictionary file with the input letters and prints out all the possible words that can be made with the letters. This script is helpful when playing games such as "4 Pics 1 Word", "Jumble", "Scrabble", and other word games.

<b>Example:</b> WordCracker.py "oeolnsdes"
<br><b>Output:</b> The output will be a list of all possible words grouped by word length and sorted within each word length grouping.

#LetterReplacement.py
LetterReplacement.py: takes a coded phrase as input, the same way CryptogramSolver.py does. This puzzle is a little easier to solve as each Letter Replacement is either the letter BEFORE or AFTER the cipher letter. So if the cipher letter is "c" then the actual letter is either "b" or "d". Unlike a Cryptogram, the letter substitutions are not consistent, so a "c" in one part of the puzzle might be a "b" but in another part of the puzzle a "c" might be a "d".

<b>Example:</b> LetterReplacement.py "ugf qvsd tjlomd usvsi hr qbsfkx qtqd bme mfufs rjnomf"
<br><b>Output: </b>
<br>the pure simple truth is rarely pure and lever simple 
<br>the pure simple truth is rarely pure and never simple

#LetterPlease.py
LetterPlease.py: takes a coded NUMERIC phrase as input. Much like the telephone keypad, each number stands for one of 3 letters. Just like the LetterReplacement puzzle, each number/letter combination in the puzzle is not consistent. So a "2" might be an "a" in one part of the puzzle and later on in the same puzzle a "2" might represent a "c".
<br>Number Letter Substitutions:
- 2 = a b c
- 3 = d e f
- 4 = g h i
- 5 = j k l
- 6 = m n o
- 7 = p r s
- 8 = t u v
- 9 = w x y
<br><br><i>Note: the Code Breakers magazine for some reason does not include the letter q or z in their Letter Please puzzles.</i>

There are usually way to many combinations to combine all the possible word solutions into a possible full solution, so this script just outputs the possible word solution for every numeric coded word.

<br><b>Example: </b> LetterPlease.py "843 4472333 6878 438 87 28 749 46 843 6676464 43 48 92687 86 4283 487 273253278 46 487 7866224 29 6463"
<br><b>Output: </b>
<br><br>843
<br>the, tid, tie, vie
<br><br>4472333
<br>giraffe
<br><br>6878
<br>must, oust
<br>etc etc...

<br><b>In this case the solution was:</b> 
<br>the giraffe must get up at six in the morning if it wants to have its breakfast in its stomach by nine


#JumbleSolver.py
JumbleSolver.py: takes a list of coded words. There are no letter substitutions, the letters have just been scrambled. The script takes each scrambled word and outputs the possible words.
<br><br><b>Example: </b>JumbleSolver.py "prige rocka deibes thorug"
<br><b>Output: </b>
<br>Words for prige :
<br>=============================================================
<br>gripe
<br>
<br>Words for rocka :
<br>=============================================================
<br>croak
<br>
<br>Words for deibes :
<br>=============================================================
<br>beside
<br>
<br>Words for thorug :
<br>=============================================================
<br>trough
<br><br>If the final answer is a one word answer then just run the key letters thru JumbleSolver.py. If the final answer is more than one word then run WordCracker.py and sift thru the list of words looking for the correct words.
 

