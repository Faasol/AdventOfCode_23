import re

def win_check(win, mine):
    result = 0
    for number in mine:
        if number in win:
            if result == 0:
                result = 1
            else:
                result *= 2
    return result

def check_line(line):
    
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
    
    return win_check(win_numbers, mine_numbers)

def main():
    
    result = 0
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        result += check_line(line)
        
    print("\n * \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()