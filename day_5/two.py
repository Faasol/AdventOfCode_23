def parse_input(lines):
    seeds = []
    maps = []
    idx_maps = -1
    
    for line in lines:
        line = line.strip()
        if line.startswith("seeds: "):
            seeds = [int(x) for x in line.split(": ")[1].split(" ")]
        elif line == '':    
            maps.append([])
            idx_maps += 1
        elif line.count(":") == 1:  continue
        else:   parse_map(line, maps, idx_maps)
    
    for item in maps:
        item.sort()
        
    return seeds, maps
                

def parse_map(line, maps, i):
    dest, src, size = (int(x) for x in line.split())
    maps[i].append((src, dest, size))
    
def find_result(seeds, maps):
    
    result = 1_000_000_000_000
    
    for i in range(0, len(seeds), 2):
        
        source_ranges = [(seeds[i], seeds[i] + seeds[i+1] - 1)]
        dest_ranges = []
        
        for item in maps:
            for beg, end in source_ranges:
                for src, dest, size in item:
                    if end < src:
                        dest_ranges.append((beg, end))
                        break
                    elif beg >= src and beg < src + size:
                        if end >= src + size:
                            dest_ranges.append((dest + (beg - src), dest + size - 1))
                            beg = src + size
                        else:
                            dest_ranges.append((dest + (beg - src), dest + (end - src)))
                            break
                    elif beg < src and end >= src:
                        dest_ranges.append((beg, src - 1))
                        beg = src
                else:
                    dest_ranges.append((beg, end))
                    
            source_ranges = dest_ranges
            dest_ranges = []
            
        tmp = min(beg for beg, _ in source_ranges)
        result = tmp if tmp < result else result
        
    return result

def main():
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    seeds, maps = parse_input(lines)
            
    print("\n ** \t -> \t" + str(find_result(seeds, maps)) + "\n")
    
if __name__ == '__main__':    
    main()