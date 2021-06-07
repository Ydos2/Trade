import math
import sys

def sma(tab, n):
    cpt = 0.0
    j = 0
    mean_list = tab[-n:]
    for i in range (0, len(mean_list)):
        cpt += mean_list[i]
        j += 1
    return cpt / j

def upper_bb(tab, sma, n):
    bb = sma + (standard_deviation(tab, n) * 2)
    return bb

def lower_bb(tab, sma, n):
    bb = sma - (standard_deviation(tab, n) * 2)
    return bb

def standard_deviation(values, period_nbr):
    value = 0.0
    mean = sma(values, period_nbr)
    for i in range(len(values) - period_nbr, len(values)):
        value += (abs(values[i] - mean)) ** 2
    value /= period_nbr
    value = math.sqrt(value)
    return value
