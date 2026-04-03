#Daily challenge Gold: Solve the Matrix

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

matrix = [list(line) for line in MATRIX_STR.splitlines() if line]

decoded_message = ""

for col in range(len(matrix[0])):
    for row in matrix:
        char = row[col]
        if char.isalpha():
            decoded_message += char
        else:
            decoded_message += " "

print(decoded_message)