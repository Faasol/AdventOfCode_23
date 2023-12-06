import re

def parse_line(line):
    
    result = ""
    line = line.strip()
    line = re.sub(' +', ' ', line)
    
    numbers = line.split(": ")[1]
    list_result = numbers.split(" ")
    
    for x in list_result:
        result += x
    
    return int(result)

def win_race(time, distance):
    result = 0
    
    for stop_time in range(time+1):
        travel = stop_time * (time - stop_time)
        if travel > distance:  result += 1
    
    return result

def main():
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    
    time = parse_line(lines[0])
    distance = parse_line(lines[1])
    
    print("\n ** \t -> \t" + str(win_race(time, distance)) + "\n")
    
if __name__ == '__main__':    
    main()