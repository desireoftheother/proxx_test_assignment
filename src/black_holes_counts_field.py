import numpy as np
from scipy.ndimage import convolve
from black_holes_field import BlackHolesField


class BlackHolesCountsField:
    """Class for storing info about Black Holes count in each node"""

    def __init__(self, field: BlackHolesField):
        self.counts_matrix = self.__calculate_counts(field)

    def __calculate_counts(self, field: BlackHolesField) -> np.ndarray:
        kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        counts_matrix = convolve(field.field, kernel, mode="constant")
        return counts_matrix
