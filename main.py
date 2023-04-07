class Token:
    def __init__(self, token_type, lexeme):          # constructor method that is used for our Token class
        self.token_type = token_type                 # constructor uses two params, token_type & lexeme
        self.lexeme = lexeme

    def __repr__(self):                              # __repr__ method used for our class as well
        return f"{self.token_type}\t{self.lexeme}"   # this will output our token types and lexemes

def lexer(input_scode):                              # this is our lexer class that takes in our given source code file
    # each of the following are our token types, and each one matches to a state
    q0 = 'initial'
    q1 = 'keyword'
    q2 = 'separator'
    q3 = 'identifier'
    q4 = 'operator'
    q5 = 'real'
    q6 = 'integer'

    # starts out state at q0, everything is empty
    state = q0
    lexeme = ''                                     # empty string initialized
    tokens = []                                     # tokens list

    def appendToken_resetState():                   # this function appends Lexeme as token, and reset state & lexeme to continue
        nonlocal state, lexeme, tokens              # nonlocal variables used to access outside function

        if lexeme == "while":                       # if lexeme = keyword, set to state q1
            state = q1                              # state = q1

        tokens.append(Token(state, lexeme))         # state and lexeme added to list (output)

        # reset state and current lexeme back to start
        state = q0
        lexeme = ''

    # we will use an index to go through every char in source code, so set index = 0
    i = 0

# TOKEN RECOGNIZER
# ________________________________________________________________________________________________________________
    while i < len(input_scode):
        # assign char at index 'i' to the char variable, we will use this to iterate
        char = input_scode[i]

        # when initial state, determine next state
        if state == q0:
            # if character is blank, +1 to i and iterate to next i
            if char.isspace():
                i += 1
                continue

            # if the char is letter or underscore, set state to q3 , and append lexeme
            elif char.isalpha() or char == '_':
                state = q3
                lexeme += char

            # if the char is a numeral digit, change state to q6, and append the lexeme to the list
            elif char.isdigit():
                state = q6
                lexeme += char

            # if the char is a seperator such as ()[]{}, set state to q2, and append lexeme to list
            elif char in "([{;)]}":
                state = q2
                lexeme += char

            # if the char is operator such as given below, set state to q4, and append lexeme to list
            elif char in "<>=!+-*/%":
                state = q4
                lexeme += char

            # if the char is real decimal number, set state to q5, and append lexeme to list
            elif char == '.':
                state = q5
                lexeme += char

# STATE RECOGNIZER
# ________________________________________________________________________________________________________________
        # if state is not in initial state q0
        else:
            # if in state 3
            if state == q3:
                # if the char is numeric or underscore, append it to lexeme
                if char.isalnum() or char == '_':
                    lexeme += char
                # else, reset and run function appendToken_resetState
                else:
                    appendToken_resetState()
                    continue

            # if state = q6
            elif state == q6:
                # if char is a digit, append to lexeme
                if char.isdigit():
                    lexeme += char
                # if the char is a period, transition to real state q5 & append char to list
                elif char == '.':
                    state = q5
                    lexeme += char
                # else, reset and run function appendToken_resetState
                else:
                    appendToken_resetState()
                    continue

            # if state = q5
            elif state == q5:
                # if the char is number, append to table
                if char.isdigit():
                    lexeme += char
                # else, reset and run function appendToken_resetState
                else:
                    appendToken_resetState()
                    continue

            # if state is q4
            elif state == q4:
                # if char is one of the operators, add to list
                if char in "<>=!":
                    lexeme += char
                # else, reset and run function appendToken_resetState
                else:
                    appendToken_resetState()
                    continue

            # if state = q2
            elif state == q2:
                # create a token & reset state lexeme
                appendToken_resetState()
                continue
# ________________________________________________________________________________________________________________
        # increment index 'i', move to next character in index_scode.txt
        i += 1

    # add final token if needed
    if state != q0:
        appendToken_resetState()

    return tokens

def main():
    # read frmo source code from file input_scode.txt
    with open('input_scode.txt', 'r') as input_file:
        input_scode = input_file.read()

    # call the lexer function in order to token size the given source code
    tokens = lexer(input_scode)

    # write table into file
    with open('output', 'w') as output_file:
        # Write the header
        output_file.write("TOKEN\t----\tLEXEME\n")
        output_file.write("______________________\n")

        # write each token and lexeme after header of table in output file
        for token in tokens:
            output_file.write(f"{token.token_type}     \t{token.lexeme}\n")

    # print output file created message
    print("Token & Lexeme chart has been printed in the 'output' file.")

# main function call
if __name__ == "__main__":
    main()
