import re

def get_value_of_index(line, i):
    for idx_loop in re.finditer("\d+", line):
        if (idx_loop.start() <= i and i <= idx_loop.end()):
            return int(line[idx_loop.start():idx_loop.end()])
    return -1
    
def check_numbers(line, idx):
    result = []
    
    for i in range(idx - 1 if idx-1>=0 else idx, idx+2 if idx+1 < len(line) else idx):
        if line[i].isdigit():
            value = get_value_of_index(line, i)
            if value != -1 and value not in result: result.append(value)
            
    return result

def check_chars(line, prev_line, next_line, idx):
    result = []
    
    result += (check_numbers(prev_line, idx))
    result += (check_numbers(line, idx))
    result += (check_numbers(next_line, idx))
    
    ret = 1
    for value in result:
        ret *= value
    
    return ret if len(result) == 2 else 0
    
def check_line(line, prev_line, next_line):
    result = 0
    for idx in re.finditer("[*]", line):
        
        start = idx.start()
        result += check_chars(line, prev_line, next_line, start)
        
    return result

def main():
    
    result = 0
    
    file = open('input.txt', 'r')
    prev_line = ""
    lines = file.readlines()
    next_line = ""
    for idx, line in enumerate(lines):
        if idx < len(lines) - 1:
            next_line = lines[idx+1]
        else:
            next_line = ""
        result += check_line(line, prev_line, next_line)
        prev_line = line
        
    print("\n ** \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()