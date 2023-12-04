import re

def win_check(win, mine):
    result = 0
    for number in mine:
        if number in win:
            result += 1
    return result

def check_line(line, i, copies):
    
    result = 0
    
    line = re.sub(' +', ' ', line)
    first_parse = line.split(": ")
    
    str_game = first_parse[1]
    second_parse = str_game.split("| ")
    str_win_numbers = second_parse[0]
    parse = str_win_numbers.split(" ")
    
    win_numbers = []
    for number in parse:
        if number:  win_numbers.append(int(number))
    
    str_mine_numbers = second_parse[1]
    parse = str_mine_numbers.split(" ")        
    mine_numbers = []
    for number in parse:
        if number:  mine_numbers.append(int(number))
        
    result = win_check(win_numbers, mine_numbers)
    for j in range(i+1, i + result + 1):
        copies[j] += copies[i]

def main():
    
    result = 0
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    copies = [1 for x in range(len(lines))]
    
    for i, line in enumerate(lines):
        check_line(line, i, copies)
    
    for value in copies:
        result += value
        
    print("\n ** \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()