first = -1
last = -1

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

def check_string(str_input):
    result = ""
    get_first_last(str_input)
    result += str_input[first]
    result += str_input[last] if last != -1 else str_input[first]
    return result

def main():
    
    result = 0
    
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        result += int(check_string(line))
        
    print("\n * \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()