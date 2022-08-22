import numpy as np
from src.black_holes_counts_field import BlackHolesCountsField
from src.view_field import ViewField
from src.game_status import GameStatus
from src.utils import check_if_cell_clear
from src.black_holes_field import BlackHolesField


class Game:
    """Class which store and updates actual game flow information"""

    def __init__(self, board_size: int, black_hole_count: int):
        self.__black_holes_matrix = BlackHolesField(
            size=board_size, num_of_holes=black_hole_count
        )
        self.__size = board_size
        self.__black_holes_count = black_hole_count
        self.__counts_matrix = BlackHolesCountsField(field=self.__black_holes_matrix)
        self.__game_status_enum = GameStatus
        self.status = self.__game_status_enum.IN_PROGRESS
        self.view_field = ViewField(
            black_holes_field=self.__black_holes_matrix,
            counts_field=self.__counts_matrix,
            size=board_size,
        )

    def click(self, row: int, column: int) -> None:
        if row >= self.__size or column >= self.__size:
            print("Please, click again, your coordinate is out of range")
            return
        if not check_if_cell_clear(
            row=row, column=column, black_holes_matrix=self.__black_holes_matrix.field
        ):
            self.status = self.__game_status_enum.LOSE
        else:
            self.view_field.update_view_field(row_clicked=row, column_clicked=column)
            if (
                np.count_nonzero(self.view_field.view_field == 0)
                == self.__black_holes_count
            ):
                self.status = self.__game_status_enum.WIN
            else:
                self.status = self.__game_status_enum.IN_PROGRESS

    def show_field(self) -> None:
        for row in range(0, self.__size):
            for column in range(0, self.__size):
                if self.view_field.view_field[row, column] == 1:
                    if self.__counts_matrix.counts_matrix[row, column] == 0:
                        print("O", end=" ")
                    else:
                        print(self.__counts_matrix.counts_matrix[row, column], end=" ")
                if self.view_field.view_field[row, column] == 0:
                    print("_", end=" ")
                if (
                    self.__black_holes_matrix.field[row, column] == 1
                    and self.view_field.view_field[row, column] == 1
                ):
                    print("X", end=" ")
            print("\n")
