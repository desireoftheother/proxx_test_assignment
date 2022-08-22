import numpy as np


class BlackHolesField:
    """Class for storing the field info with Black Holes population functionality"""

    def __init__(self, size: int, num_of_holes: int) -> None:
        self.__size = size
        self.__num_of_holes = num_of_holes
        self.field = self.__generate_field(
            size=self.__size, num_of_holes=self.__num_of_holes
        )

    def __generate_field(self, size: int, num_of_holes: int) -> np.ndarray:
        field_array = np.zeros(size**2).astype(int)
        field_array[:num_of_holes] = 1
        np.random.shuffle(field_array)
        field_matrix = np.reshape(field_array, (size, size))
        return field_matrix
