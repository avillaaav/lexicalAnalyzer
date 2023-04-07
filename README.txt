CPSC 323 - PROJECT 1 - Angel Villa

How to set-up and run main.py:

What is main.py?
- main.py is a Python program designed to run the main function, lexer(), in order to act as a lexical analyzer which parses a character stream and outputs the tokens and lexemes onto a table for a user to look at. For example, if the source code given is:

while (t < lower) r = 28.00;

Then the program will parse every character individually and sort it the tokens and lexemes onto a table so a user can recognize what lexemes are a part of which token group. The program will ignore whitespaces.

How to Set-Up and run:
1) Load main.py into desired IDE. In this case, we use PyCharm IDE.
2) Set run configuration and project folder so it can reference the file input_scode.txt.
3) Press the play button so the code runs and outputs an "output" file which contains the sorted table.

How this code runs:
- This code is kind of hardcoded in the sense that it just uses an if statement with a bunch of else-ifs to determine when a token is recognized in the character stream, then runs a function to upload the token and corresponding lexeme to a table, and resets the lexeme and state back so that it can continue running down the character stream.
- It iterates through the entire character stream with an index starting at 0. The index will finish off by counting how many characters are in the character stream, and wait for the index to hit the total character count before outputting the "output" file.
- An index is used here so that it can iterate the entire character stream and output duplicate recognized token types and not stop at the first one it detects. So therefore, every character is considered in the character stream and the table will be complete.

Thank you.

Angel Villa