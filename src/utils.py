def check_if_cell_clear(black_holes_matrix, row: int, column: int) -> bool:
    if black_holes_matrix[row, column] == 1:
        result = False
    else:
        result = True
    return result
