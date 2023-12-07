import math

def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        _, times = lines[0].split(':')
        times = list(map(int, times.split()))
        _, dists = lines[1].split(':')
        dists = list(map(int, dists.split()))

        return times, dists


# i * (time - i) = dist
# i*time - i^2 = dist

# -i^2 + time*i - dist = 0

# (-time+-sqrt(time^2-4*dist))/-2

# Time:      71530
# Distance:  940200

time = 53897698
dist = 313109012141201

root1 = math.floor((time-math.sqrt(time**2-4*dist))/2)
root2 = math.floor((time+math.sqrt(time**2-4*dist))/2)

print(root2 - root1)


def num_wins(time, dist):
    wins = 0

    first_index = 0
    last_index = time
    for i in range(1, time-1):
        if i * (time - i) > dist:
            first_index = i
            break

    for i in range(time-1, 0, -1):
        if i * (time - i) > dist:
            last_index = i
            break
            
    return last_index - first_index + 1


def solve(filename):
    times, dists = parse_file(filename)
    ans = 1

    for i in range(len(times)):
        ans *= num_wins(times[i], dists[i])

    print(f'solve {filename}: {ans}')


solve('example.txt')
solve('input.txt')

solve('example2.txt')
solve('input2.txt')
