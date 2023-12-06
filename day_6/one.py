import re

def parse_line(line):
    
    line = line.strip()
    line = re.sub(' +', ' ', line)
    
    numbers = line.split(": ")[1]
    result = numbers.split(" ")
    
    return [int(x) for x in result]

def win_race(time, distance):
    result = 0
    
    for stop_time in range(time+1):
        travel = stop_time * (time - stop_time)
        if travel > distance:  result += 1
    
    return result

def check_wins(time, distance):
    result = 1
    for i in range(len(time)):
        result *= win_race(time[i], distance[i])
    return result

def main():
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    
    time = parse_line(lines[0])
    distance = parse_line(lines[1])
    
    print("\n * \t -> \t" + str(check_wins(time, distance)) + "\n")
    
if __name__ == '__main__':    
    main()