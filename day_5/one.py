def init_seeds(line, seeds, seeds_bool):
    parse = line.split(": ")[1]
    numbers = parse.split(" ")
    for number in numbers:
        seeds.append(int(number))
        seeds_bool.append(False)
    
def init_bools(seeds_bool):
    for i in range(len(seeds_bool)):
        seeds_bool[i] = False
        
def check_seeds(seeds, numbers, seeds_bool):
    for i in range(len(seeds)):
        if seeds[i] >= numbers[1] and seeds[i] < numbers[1] + numbers[2] and not seeds_bool[i]:
            seeds[i] += numbers[0] - numbers[1]
            seeds_bool[i] = True
        
def check_line(type_map, seeds, seeds_bool):
    for line in type_map:
        if line.count(":") == 1:  continue
        
        numbers = line.split(" ")
        numbers = [int(i) for i in numbers]
        
        check_seeds(seeds, numbers, seeds_bool)
        
    print(seeds)
    init_bools(seeds_bool)
    
def find_min(seeds):
    min_value = seeds[0]
    for i in range(1, len(seeds)):
        min_value = seeds[i] if seeds[i] < min_value else min_value
    return min_value

def main():
    
    seeds = []
    seeds_bool = []
    type_map = []
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if i==0:
            init_seeds(line, seeds, seeds_bool)
        elif line != '':
            type_map.append(line)
        else:
            check_line(type_map, seeds, seeds_bool)
            type_map = []
            
    check_line(type_map, seeds, seeds_bool)
    print("\n * \t -> \t" + str(find_min(seeds)) + "\n")
    
if __name__ == '__main__':    
    main()