def parse_input(lines):
    directions = []
    steps = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        if line == '': continue
        elif i == 0:
            directions = [*line]
        else:
            left_and_right = []
            node = line.split(" = ")
            values = ""
            for char in node[1]:
                if char.isalpha():
                    values += char
                elif values:
                    left_and_right.append(values)
                    values = ""
            steps[node[0]] = left_and_right
    
    return directions, steps

def complete_path(directions, steps):
    
    wai = "AAA"
    idx_dir = 0
    result = 0
    
    while wai != "ZZZ":
        left_or_right = 0 if directions[idx_dir] == "L" else 1
        wai = steps[wai][left_or_right]
        idx_dir = (idx_dir+1) % len(directions)
        result += 1
    
    return result
        

def main():
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    directions, steps = parse_input(lines)
        
    print("\n * \t -> \t" + str(complete_path(directions, steps)) + "\n")
    
if __name__ == '__main__':    
    main()