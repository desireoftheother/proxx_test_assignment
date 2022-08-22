from game import Game
from src.game_status import GameStatus

if __name__ == "__main__":
    print("Welcome to Proxx! Please, enter the size of the field")
    is_size_valid = False
    while not is_size_valid:
        size = int(input())
        if size > 0:
            is_size_valid = True
        else:
            print("Please, enter the valid size of the field")
    print("Please, enter the number of black holes!")
    is_bh_count_valid = False
    while not is_bh_count_valid:
        num_of_holes = int(input())
        if num_of_holes > 0 and num_of_holes < size**2:
            is_bh_count_valid = True
        else:
            print("Please, enter the number of black holes!")
    game_instance = Game(size, num_of_holes)
    print(game_instance.show_field())
    while game_instance.status == GameStatus.IN_PROGRESS:
        print("Enter row number")
        row = int(input())
        print("Please, enter column number")
        column = int(input())
        game_instance.click(row, column)
        print(game_instance.show_field())
    if game_instance.status == GameStatus.LOSE:
        print("Well, try again!")
    if game_instance.status == GameStatus.WIN:
        print("Congratulations!")
