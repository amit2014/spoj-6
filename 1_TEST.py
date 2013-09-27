#!python3
#coding:utf-8
import fileinput
for data in fileinput.input():
    if data.strip() and data.strip() == '42': break
    print(data.strip())