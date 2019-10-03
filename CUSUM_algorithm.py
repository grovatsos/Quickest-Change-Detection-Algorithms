import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm
import math

pre_change_mu = 0
pre_change_sigma = 1
post_change_mu = 1
post_change_sigma = 1
threshold = 50
repetitions = 100
changepoint = 50
delays = np.zeros(repetitions)


for j in range(repetitions):
    Observations = np.array([0])
    CUSUM_statistic = np.array([0])
    flag = 0
    i = 0
    while flag == 0:
        i = i + 1
        if i < changepoint:
            Observations = np.append(Observations, random.normalvariate(pre_change_mu, pre_change_sigma))
        else:
            Observations = np.append(Observations , random.normalvariate(post_change_mu,post_change_sigma))
        LLR = math.log(norm.pdf(Observations[i], post_change_mu, post_change_sigma)  / norm.pdf(Observations[i], pre_change_mu, pre_change_sigma)   )
        CUSUM_statistic = np.append(CUSUM_statistic, max(CUSUM_statistic[i-1] + LLR,0) )

        if CUSUM_statistic[i] > threshold:
            flag = 1
            delays[j] = i - changepoint + 1
            #delays[j] = i
plt.plot( CUSUM_statistic)
print("The expected delay for a threshold of",threshold,"and a changepoint equals to",changepoint,"is",np.mean(delays),".")