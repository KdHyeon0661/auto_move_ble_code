import math


def calc_dist(rssi, tx):
    return round(math.pow(10, (tx - rssi) / 10 * 3.2), 2)

