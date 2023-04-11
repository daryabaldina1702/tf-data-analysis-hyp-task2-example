import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 834411281 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, p_value = ks_2samp(x, y)
    alpha = 0.07
    return p_value < alpha
