
def getFirstNumber(calibration_value): 
    for char in calibration_value: 
        if char.isdigit(): 
            return int(char)
    raise Exception("first digit not found")

def getLastNumber(calibration_value): 
    for char in calibration_value[::-1]: 
        if char.isdigit(): 
            return int(char)
    raise Exception("Last digit not found")


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