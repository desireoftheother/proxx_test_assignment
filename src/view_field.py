import numpy as np
from black_holes_field import BlackHolesField
from black_holes_counts_field import BlackHolesCountsField


class ViewField:
    """Class which stores data about open and closed parts of the field.
    By convention, 0 is closed cell, 1 is an open one"""

    def __init__(
        self,
        black_holes_field: BlackHolesField,
        counts_field: BlackHolesCountsField,
        size: int,
    ):
        self.view_field = np.zeros((size, size)).astype(int)
        self.__black_holes_field = black_holes_field.field
        self.__counts_field = counts_field.counts_matrix
        self.__size = size

    def update_view_field(self, row_clicked: int, column_clicked: int):
        if (
            row_clicked < 0
            or column_clicked < 0
            or row_clicked >= self.__size
            or column_clicked >= self.__size
        ):
            return
        if self.__counts_field[row_clicked, column_clicked] != 0:
            self.view_field[row_clicked, column_clicked] = 1
            return
        elif (
            (self.__counts_field[row_clicked, column_clicked] == 0)
            and (self.__black_holes_field[row_clicked, column_clicked] != 1)
            and (self.view_field[row_clicked, column_clicked] == 0)
        ):
            self.view_field[row_clicked, column_clicked] = 1
            self.update_view_field(row_clicked, column_clicked - 1)
            self.update_view_field(row_clicked, column_clicked + 1)
            self.update_view_field(row_clicked - 1, column_clicked)
            self.update_view_field(row_clicked + 1, column_clicked)
            return
