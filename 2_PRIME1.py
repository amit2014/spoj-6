#!python3
#coding: utf-8
import cProfile
prof = cProfile.Profile()
prof.enable()

import fileinput
input_obj = fileinput.input()
primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
for data in input_obj:
    if not input_obj.isfirstline():
        inicio, fim = map(int, data.split())
        inicio -= 1

        while inicio <= fim:
            inicio += 1

            if inicio in primos:
                print(inicio)
                continue

            elif inicio > 1:
                divisor = 2
                limite = int(inicio ** 0.5) + 1

                if primos:
                    divisor = primos[-1]+1
                    if 0 in map(lambda x: inicio % x, primos):
                        continue

                while (divisor < limite and inicio % divisor): divisor+=1
                if divisor >= limite:
                    print(inicio)

        print()

prof.disable()
prof.print_stats()