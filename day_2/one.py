def check_number_color(color, number, first_star):
    for key, value in first_star.items():
        if key == color and number > value:
            return False
    return True
        
def check_line(line):
    
    first_star = {"red" : 12, "green" : 13, "blue" : 14}

    first_parse = line.split(": ")
    str_id = first_parse[0].split(" ")[1]
    
    str_game = first_parse[1]
    second_parse = str_game.split("; ")
    
    for str_set in second_parse:
        third_parse = str_set.split(", ")
        for number_color in third_parse:
            items = number_color.split(" ")
            if not check_number_color(items[1].split("\n")[0], int(items[0]), first_star):
                return 0
    
    return int(str_id)

def main():
    
    result = 0
    
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        result += check_line(line)
        
    print("\n * \t -> \t" + str(result) + "\n")
    
if __name__ == '__main__':    
    main()