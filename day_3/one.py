import re

def check_char(line, i):
    if line:
        return True if (line[i] != "." and not line[i].isdigit()) else False
    return False

def check_chars(line, prev_line, next_line, start, end):
    for i in range(start, end):
        if check_char(line, i) or check_char(prev_line, i) or check_char(next_line, i):
            return True
    return False
    
def check_line(line, prev_line, next_line):
    result = 0
    for idx in re.finditer("\d+", line):
        
        start = idx.start()
        end = idx.end()
        
        if check_chars(line, prev_line, next_line, start-1 if start-1 >= 0 else start, end+1 if end+1 < len(line) else end):
            result += int(line[start:end])
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
        
    print("\n * \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()