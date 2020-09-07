#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:46:03 2020

@author: apple
"""

print('---------')
print('| ' + '  ' + '  ' + '  ' + '|')
print('| ' + '  ' + '  ' + '  ' + '|')
print('| ' + '  ' + '  ' + '  ' + '|')
print('---------')
code = ' ' * 9
lis = [list(code[0:3]), list(code[3:6]), list(code[6:9])]
n = 0
Xcount = 0
Ocount = 0
while n in range(9):
    position = input('Enter the coordinates: ')
    if ''.join(position.split()).isdigit() == True:
        if (int(position.split()[0]) in range(4)) and (int(position.split()[1]) in range(4)) is True:
            if lis[int(position.split()[1])-1][int(position.split()[0])-1] == 'X' or lis[int(position.split()[1])-1][int(position.split()[0])-1] == 'O':
                print('This cell is occupied! Choose another one!')
            else:
                if n % 2 == 0:
                    cor = 'X'
                    Xcount += 1
                else:
                    cor = 'O'
                    Ocount += 1
                    
                lis[int(position.split()[1])-1][int(position.split()[0])-1] = cor
                lis = [lis[0], lis[1], lis[2]]
                print('---------')
                print('| ' + str(lis[2][0]) + ' ' + str(lis[2][1]) + ' ' + str(lis[2][2]) + ' |')
                print('| ' + str(lis[1][0]) + ' ' + str(lis[1][1]) + ' ' + str(lis[1][2]) + ' |')
                print('| ' + str(lis[0][0]) + ' ' + str(lis[0][1]) + ' ' + str(lis[0][2]) + ' |')
                print('---------')
                n += 1
        else:
            print('Coordinates should be from 1 to 3!')
        
    else:
        print('You should enter numbers!')
        

    lis1 = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            if lis[i][j] == 'X':
                lis1[i][j] = 1
            elif lis[i][j] == 'O':
                lis1[i][j] = -1
            else:
                lis1[i][j] = 0
    row_count1 = lis1[0]
    row_count2 = lis1[1]
    row_count3 = lis1[2]
    diagonal_count1 = [lis1[0][0], lis1[1][1], lis1[2][2]]
    diagonal_count2 = [lis1[2][0], lis1[1][1], lis1[0][2]]
    col_count1 = [lis1[0][0], lis1[1][0], lis1[2][0]]
    col_count2 = [lis1[0][1], lis1[1][1], lis1[2][1]]
    col_count3 = [lis1[0][2], lis1[1][2], lis1[2][2]]
    
    count = [sum(row_count1), sum(row_count2), sum(row_count3), sum(diagonal_count1), sum(diagonal_count2), sum(col_count1), sum(col_count2), sum(col_count3)]
    if count.count(3) + count.count(-3) == 1:
        if count.count(3) == 1:
            print('X wins')
            break
        else:
            print('O wins')
            break
    else:
        if Xcount + Ocount == 9:
            print('Draw')
        else:
            continue
        