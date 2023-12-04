def check_number_color(color, number, max_dict):
    max_dict[color] = number if number > max_dict[color] else max_dict[color]
            
def check_line(line):
    
    max_dict =  {"red" : 0, "green" : 0, "blue" : 0}
    
    first_parse = line.split(": ")
    
    str_game = first_parse[1]
    second_parse = str_game.split("; ")
    
    for str_set in second_parse:
        third_parse = str_set.split(", ")
        for number_color in third_parse:
            items = number_color.split(" ")
            check_number_color(items[1].split("\n")[0], int(items[0]), max_dict)
    
    result = 1
    for value in max_dict.values():
        result *= value
        
    return result

def main():
    
    result = 0
    
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        result += check_line(line)
        
    print("\n ** \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()