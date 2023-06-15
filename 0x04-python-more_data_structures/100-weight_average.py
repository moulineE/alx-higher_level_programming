#!/usr/bin/python3
def weight_average(my_list=[]):
    avr = 0
    div = 0
    for i in range(len(my_list)):
        avr += my_list[i][0] * my_list[i][1]
        div += my_list[i][1]
    w_avr = avr / div
    return w_avr
