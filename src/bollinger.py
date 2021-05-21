import pandas as pd 
import matplotlib.pyplot as plt 
import requests
import math
import numpy as np

def sma(data, window):
    sma = data.rolling(window = window).mean()
    return sma

def set_sma():
    SMA = ( Sum ( Price, n ) ) / n  

def bb(data, sma, window):
    std = data.rolling(window = window).std()
    upper_bb = sma + std * 2
    lower_bb = sma - std * 2
    return upper_bb, lower_bb
