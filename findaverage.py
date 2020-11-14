import openpyxl
import openpyxl.utils
import countdemo

def find_average():
    game_data_rows = countdemo.get_data_rows("games-features.xlsx")
    count = -1
    total = 0
    for game_row in game_data_rows:
        count +=1
        column_number = openpyxl.utils.cell.column_index_from_string('P')-1
        owners_count = game_row[column_number].value
        if type(owners_count) is str:
            continue
        total = total+owners_count
    average_owners_count = total/count
    print(f"Reach game is owned by {average_owners_count} owners")

find_average()