import requests
import math
import sys
#import numpy as np

def sma(data, window):
    sma = data.rolling(window = window).mean()
    return sma

def sma(tab, n):
    cpt = 0.0

    for i in range (len(tab) - n, len(tab)):
        cpt += tab[i]
    cpt /= n
    return cpt

def upper_bb(tab, sma, n):
    bb = sma + standard_deviation(tab, n) * 2
    return bb

def lower_bb(tab, sma, n):
    bb = sma - standard_deviation(tab, n) * 2
    return bb

def standard_deviation(values, period_nbr):
    value = 0.0
    mean = sma(values, period_nbr)
    for i in range(len(values) - period_nbr, len(values)):
        value += (values[i] - mean) ** 2
    value /= period_nbr
    value = math.sqrt(value)
    return value
