def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        _, times = lines[0].split(':')
        times = list(map(int, times.split()))
        _, dists = lines[1].split(':')
        dists = list(map(int, dists.split()))

        return times, dists


def num_wins(time, dist):
    wins = 0
    for i in range(1, time-1):
        if i * (time - i) > dist:
            wins += 1
    return wins


def solve(filename):
    times, dists = parse_file(filename)
    ans = 1

    for i in range(len(times)):
        ans *= num_wins(times[i], dists[i])

    print(f'P1 {filename}: {ans}')


solve('example.txt')
solve('input.txt')

solve('example2.txt')
pasolvert1('input2.txt')
