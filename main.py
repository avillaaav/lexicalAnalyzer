class Token:
    def __init__(self, token_type, lexeme):          # __init__ used to initialize attri
        self.token_type = token_type                 # constructor uses two params, token_type & lexeme
        self.lexeme = lexeme

    def __repr__(self):                              # __repr__ method used to return class obj as string
        return f"{self.token_type}\t{self.lexeme}"   # this will output our token types and lexemes

def lexer(input_scode):                              # organized states
    q0 = 'initial'                                   # each of the following are our token types, and each one matches to a state
    q1 = 'keyword'
    q2 = 'separator'
    q3 = 'identifier'
    q4 = 'operator'
    q5 = 'real'
    q6 = 'integer'

    state = q0                                      # starts out state at q0, everything is empty
    lexeme = ''                                     # empty string initialized
    tokens = []                                     # tokens list

    def appendToken_resetState():                   # this function appends lexem & token, and reset state & lexeme to continue
        nonlocal state, lexeme, tokens              # nonlocal variables used to access outside function

        if lexeme == "while":                       # if lexeme = keyword, set to state q1 - ONLY WORKS FOR WHILE
            state = q1

        tokens.append(Token(state, lexeme))         # state and lexeme added to list (output)

        state = q0                                  # reset state and current lexeme back to start
        lexeme = ''

    i = 0                                           # we will use an index to go through every char in source code, so set index = 0

# TOKEN RECOGNIZER
# ________________________________________________________________________________________________________________
    while i < len(input_scode):
        char = input_scode[i]                       # assign char at index 'i' to the char variable, we will use this to iterate

        if state == q0:
            if char.isspace():                      # USED TO IGNORE SPACES IN INPUT
                i += 1
                continue

            elif char.isalpha() or char == '_':     # if the char is letter or underscore, set state to q3, and append
                state = q3
                lexeme += char

            elif char.isdigit():                    # if the char is a numerical digit, change state to q6, append to list
                state = q6
                lexeme += char

            elif char in "([{;)]}":                 # if the char is a seperator such as ()[]{}, set state to q2, append to list
                state = q2
                lexeme += char

            elif char in "<>=!+-*/%":               # if the char is operator such as given below, set state to q4, append to list
                state = q4
                lexeme += char

            elif char == '.':                       # if the char is real decimal number, set state to q5, append to list
                state = q5
                lexeme += char

# STATE RECOGNIZER
# ________________________________________________________________________________________________________________
        else:
            if state == q3:
                if char.isalpha() or char == '_':  # if the char is numeric or underscore, append it
                    lexeme += char

                else:                              # else, reset and run function appendToken_resetState - ADDS TO OUTPUT
                    appendToken_resetState()
                    continue

            elif state == q6:
                if char.isdigit():                 # check for more digits
                    lexeme += char

                elif char == '.':                  # if the char is a period, this defines it as real number
                    state = q5
                    lexeme += char

                else:                              # run function appendToken_resetState which adds to output
                    appendToken_resetState()
                    continue

            elif state == q5:                      # if the char is number, append to table

                if char.isdigit():                 # check for more numbers IN the number
                    lexeme += char

                else:
                    appendToken_resetState()       # add to output
                    continue

            elif state == q4:
                if char in "<>=!":                 # if char is one of the operators, add to list
                    lexeme += char                 # check if << >> == <= >= etc.

                else:                              # run function appendToken_resetState - ADD TO OUTPUT
                    appendToken_resetState()
                    continue

            elif state == q2:
                # ADD TO OUTPUT
                appendToken_resetState()
                continue
# ________________________________________________________________________________________________________________
        # increment index 'i', move to next character in index_scode.txt
        i += 1

    # add final token to output once the code is done iterating
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
        # write the header
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
