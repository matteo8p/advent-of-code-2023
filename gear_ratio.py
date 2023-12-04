class SchematicNumber: 
    def __init__(self, number, row, start_col, end_col): 
        self.number = number
        self.row = row
        self.start_col = start_col
        self.end_col = end_col

schematic_numbers = []
engine_schematic = []

def get_schematic_numbers_in_row(row_values, row): 
    left = 0
    right = 0
    while left < len(row_values) and right < len(row_values): 
        if not(row_values[left].isdigit()): 
            left += 1
            right = left
        else: 
            while right < len(row_values) and row_values[right].isdigit(): 
                right += 1
            new_schematic_number = SchematicNumber(int(row_values[left:right]), row, left, right)
            schematic_numbers.append(new_schematic_number)
            left = right

def is_char_next_to_special_character(row, col): 
    return is_special_character(row - 1, col) or is_special_character(row + 1, col) or is_special_character(row, col - 1) or is_special_character(row, col + 1) or is_special_character(row - 1, col - 1) or is_special_character(row - 1, col + 1) or is_special_character(row + 1, col - 1) or is_special_character(row + 1, col + 1)
    
def is_schematic_number_next_to_special_character(schematic_number):
    row = schematic_number.row
    for col in range(schematic_number.start_col, schematic_number.end_col): 
        if is_char_next_to_special_character(row, col): 
            return True
    return False 

def is_special_character(row, col):
    if row < 0 or row >= len(engine_schematic): 
        return False
    if col < 0 or col >= len(engine_schematic[0]): 
        return False
    return not(engine_schematic[row][col].isdigit()) and engine_schematic[row][col] != '.'

def gear_ratio(): 
    trebuchet_example_file = open('data/gear_ratio_example.txt', 'r').readlines()
    for line in trebuchet_example_file: 
        engine_schematic.append(line)

    for row_num in range(0, len(engine_schematic)): 
        get_schematic_numbers_in_row(engine_schematic[row_num], row_num)

    answer = 0
    for schematic_number in schematic_numbers: 
        if is_schematic_number_next_to_special_character(schematic_number): 
            answer += schematic_number.number
    return answer

def main():
    print(gear_ratio())

if __name__ == "__main__":
    main()