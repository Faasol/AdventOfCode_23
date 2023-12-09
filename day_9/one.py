def parse_line(line):
    return [int(x) for x in line.split(" ")]

def get_result(history_list):
    result = 0
    for i in range(len(history_list)):
        result += history_list[-1-i][-1]
    return result

def get_history_list(numbers):
    result = []
    for i in range(len(numbers)-1):
        result.append(numbers[i+1]-numbers[i])
    return result

def is_all_zero(numbers):
    if not numbers: return False
    for number in numbers:
        if number != 0: return False
    return True

def get_history(numbers):
    history_list = []
    partial_result = []
    history_list.append(numbers)
    
    while not is_all_zero(partial_result):
        partial_result = get_history_list(numbers)
        history_list.append(partial_result)
        numbers = partial_result
    
    return get_result(history_list)
    
def main():
    
    result = 0
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        numbers = parse_line(line)
        result += get_history(numbers)
        
    print("\n * \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()