def parse_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())

    return lines


chunks = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def part1(filename):
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    ans = 0
    lines = parse_file(filename)
    for line in lines:
        open_chunks = []
        for c in line:
            if c in chunks.keys():
                open_chunks.append(c)
            else:
                open_chunk = open_chunks.pop()
                if chunks[open_chunk] != c:
                    ans += scores[c]
                    continue
        
    print(f'ANSWER: {ans}')


def incomplete_lines(lines):
    for line in lines:
        open_chunks = []
        for c in line:
            if c in chunks.keys():
                open_chunks.append(c)
            else:
                open_chunk = open_chunks.pop()
                if chunks[open_chunk] != c:
                    break
        else:
            yield open_chunks


def part2(filename):
    score_vals = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    scores = []
    lines = parse_file(filename)
    for opens in incomplete_lines(lines):
        score = 0
        while len(opens):
            score *= 5
            score += score_vals[chunks[opens.pop()]]
        scores.append(score)
    scores.sort()

    ans = scores[int(len(scores)/2)]

    print(f'ANSWER: {ans}')


part2('input.txt')
