# CodeBreakers
A collection of Python scripts that help solve puzzles in the "Code Breakers" puzzles and other word puzzles.
A list of puzzles that can be solved with these scripts:
- Cryptograms (Dell, Code Breakers)
- Kriss Kross (Dell, Code Breakers)
- Letter, Please (Dell, Code Breakers)
- Letter Replacement (Dell, Code Breakers)
- Jumble (PennyPress) 
- 4 Pics 1 Word
- Scrabble


The Scripts:

========================================================
CryptogramSolver.py
========================================================
CryptogramSolver.py takes a cryptogram coded phrase as input. It then does letter frequency analysis and filters against a dictionary file and reduces the coded phrase down to a small number of possible solutions. Lots of times it filters the phrase down to just one solution!

Example: CryptogramSolver.py "alvaml bql vd xol qvbs xv ketsvu kold xolc qlbmeyl xoleq vaedevdt bql vdmc vaedevdt"
Output: people are on the road to wisdom when they realize their opinions are only opinions

========================================================
WordCracker.py
========================================================
WordCracker.py: takes a bunch of letters as input and cross references a dictionary file with the input letters and prints out all the possible words that can be made with the letters. This script is helpful when playing games such as "4 Pics 1 Word", "Jumble", "Scrabble", and other word games.
