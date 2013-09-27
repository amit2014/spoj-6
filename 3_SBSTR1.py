#!python3
#coding: utf-8
import fileinput
input_obj = fileinput.input()
for data in input_obj:
    A, B = data.strip().split()
    print(int(A.find(B) >= 0))