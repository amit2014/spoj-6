#!python3
#coding: utf-8
import fileinput
import string

def rpn(expression):
    # See http://en.wikipedia.org/wiki/Shunting-yard_algorithm
    operator, output = [], []
    for token in expression:
        if token in ['(', '^', '*', '/', '+', '-']:
            operator.append(token)
        elif token in string.ascii_lowercase:
            output.append(token)
        elif token == ')':
            last_left_parenthesis = ''.join(operator).rfind('(')
            i = len(operator)-1
            while i>last_left_parenthesis:
                output.append(operator.pop(i))
                i-=1
            operator.pop(i)

    return ''.join(output)


input_obj = fileinput.input()
for data in input_obj:
    if not input_obj.isfirstline():
        expression = data.strip()
        print(rpn(expression))