#Author: Gentry Atkinson
#Organization: Texas University
#Data: 13 May, 2020
#This code will generate a numpy array of synthetic time series data, use the
#labelfix preprocessor to flip mu percent (0.03) of the labels, and the use the
#labelfix check_dataset function to identify some of the flipped labelsself.

import sklearn
from labelfix import check_dataset, preprocess_x_y_and_shuffle
from utils.gen_ts_data import generate_pattern_data
import numpy as np
import random

if __name__ == "__main__":
    print("creating 500 time series sequences with 3 labels")
    NUM_SAMPLES = 500
    LENGTH = 500
    amplitude = [2, 4, 8]
    pattern_length = [8, 16, 32]
    var_pattern_length = [16, 32, 64]
    var_amplitude = [1, 2, 3]

    data = np.zeros((NUM_SAMPLES, LENGTH))
    labels = np.zeros(NUM_SAMPLES)

    #generate synthetic data
    for i in range(NUM_SAMPLES):
        label = random.randint(0, 2);
        data[i,:]=generate_pattern_data(length=LENGTH, avg_pattern_length=pattern_length[label],
            avg_amplitude=amplitude[label], variance_pattern_length=var_pattern_length[label],
            variance_amplitude=var_amplitude[label]);
        labels[i]=label

    #pre-process and identify data
    data, labels = preprocess_x_y_and_shuffle(data, labels)