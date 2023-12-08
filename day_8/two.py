from math import gcd

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

def get_result(wai, directions, steps):
    
    idx_dir = 0
    result = 0
    
    while not wai.endswith("Z"):
        left_or_right = 0 if directions[idx_dir] == "L" else 1
        wai = steps[wai][left_or_right]
        idx_dir = (idx_dir+1) % len(directions)
        result += 1
    
    return result

def lcm(numbers):
    lcm = 1
    for number in numbers:
        lcm = (lcm * number)//gcd(lcm, number)
    return lcm
    
def complete_path(directions, steps):
    
    wai = []
    keys = list(steps.keys())
    for key in keys:
        if key.endswith("A"):
            wai.append(key)
    
    results = []
    
    for item in wai:
        results.append(get_result(item, directions, steps))
    
    return lcm(results)
        

def main():
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    directions, steps = parse_input(lines)
        
    print("\n ** \t -> \t" + str(complete_path(directions, steps)) + "\n")
    
if __name__ == '__main__':    
    main()