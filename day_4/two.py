import re

def check_copies(copies, line, num):
    result = []
    for number in copies:
        if number == num:
            result += check_line(line, num)
    return result
    
def modify_list(num, copies):
    for i in range(len(copies)):
        copies[i] += num

def win_check(win, mine):
    result = 0
    for number in mine:
        if number in win:
            result += 1
    return result

def check_line(line, i):
    result = []
    
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
        
    for j in range(1, win_check(win_numbers, mine_numbers)+1):
        result.append(j + i)
    
    return result

def main():
    
    copies = []
    result = 0
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    for i, line in enumerate(lines):
        copies += check_line(line, i+1)
        copies += check_copies(copies, line, i+1)
        result += 1 + copies.count(i+1)
        tmp = [k for k in copies if k != i+1]
        copies = tmp    
        
    print("\n ** \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()