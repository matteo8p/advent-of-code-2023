mappings_dict = {
    "one": 1, 
    "two": 2, 
    "three": 3, 
    "four": 4, 
    "five": 5, 
    "six": 6,
    "seven": 7, 
    "eight": 8, 
    "nine": 9,                                
}

def getFirstNumber(calibration_value): 
    cur_val = calibration_value
    while len(cur_val) > 0: 
        if cur_val[0].isdigit(): 
            return int(cur_val[0])
        for key in mappings_dict.keys(): 
            if len(cur_val) >= len(key) and cur_val[0:len(key)] == key: 
                return mappings_dict[key]
        cur_val = cur_val[1:]
    raise Exception("first digit not found")

def getLastNumber(calibration_value): 
    cur_val = calibration_value[::-1]
    while len(cur_val) > 0: 
        if cur_val[0].isdigit(): 
            return int(cur_val[0])
        for key in mappings_dict.keys(): 
            if len(cur_val) >= len(key) and cur_val[0:len(key)] == key[::-1]: 
                return mappings_dict[key]
        cur_val = cur_val[1:]
    raise Exception("last digit not found")


def trebuchet(): 
    trebuchet_example_file = open('data/trebuchet_example.txt', 'r').readlines()
    trebuchet_problem_file = open('data/trebuchet.txt', 'r').readlines()
    run_example = False
    
    trebuchet_file = None
    if run_example: 
        trebuchet_file = trebuchet_example_file
    else: 
        trebuchet_file = trebuchet_problem_file
    
    sum_of_calibrations = 0; 
    for calibration_value in trebuchet_file: 
        sum_of_calibrations += 10 * getFirstNumber(calibration_value) + getLastNumber(calibration_value)
    return sum_of_calibrations


def main():
    print(trebuchet()); 

if __name__ == "__main__":
    main()