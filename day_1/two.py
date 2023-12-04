import re

first = -1
last = -1
numbers = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

def get_first_last(str_input):
    global first
    global last
    first = -1
    last = -1
    for idx, char in enumerate(str_input):
        if char.isdigit():
            if first == -1:
                first = idx
            last = idx
        
def check_substring(str_input):
    global first
    global last
    result = [-1,-1]
    for key, value in numbers.items():
        for idx in re.finditer(key, str_input):
            idx_start = idx.start()
            if (first != -1 and idx_start < first) or first == -1:
                result.pop(0)
                result.insert(0, value)
                first = idx_start
            if (last != -1 and idx_start > last) or last == -1:
                result.pop()
                result.append(value)
                last = idx_start
    return result

def check_string(str_input):
    result = ""
    get_first_last(str_input)
    char_numbers = check_substring(str_input)
    if (char_numbers[0] != -1) and (char_numbers[1] != -1):
        result += str(char_numbers[0])
        result += str(char_numbers[1])
    elif(char_numbers[0] == -1) and (char_numbers[1] != -1):
        result += str(str_input[first]) if first != -1 else str(char_numbers[1])
        result += str(char_numbers[1])
    elif(char_numbers[0] != -1) and (char_numbers[1] == -1):
        result += str(char_numbers[0])  
        result += str(str_input[last]) if last != -1 else str(char_numbers[0])
    else:
        result += str_input[first]
        result += str_input[last] if last != -1 else str_input[first]
    return result

def main():
    
    result = 0
    
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        result += int(check_string(line))
        
    print("\n ** \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()