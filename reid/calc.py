import numpy as np

def calc_distance(feat1, feat2):
    distance = np.linalg.norm(feat1 - feat2)
    return distance