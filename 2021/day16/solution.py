from math import prod

def parse_file(filename):
    with open(filename, 'r') as f:
        return f.readline().strip()


def bits(packet):
    for hex in packet:
        decimal = int(hex, 16)
        for c in ('0' * 3 + f'{decimal:b}')[-4:]:
            yield int(c)


def consume(packet, nbits):
    n = 0
    for i in range(nbits):
        m = packet.__next__()
        n += (m << (nbits - i - 1))
    return n


def read_packet(packet):
    bits = 6
    version = consume(packet, 3)
    type = consume(packet, 3)

    if type == 4:
        should_continue = 1
        val = 0
        while should_continue > 0:
            should_continue = consume(packet, 1)
            val <<= 4
            val += consume(packet, 4)
            bits += 5
        # print(f'PACKET v{version} t{type} v{val}')
        expr = val
    else:
        vals = []
        len_type_id = consume(packet, 1)
        bits += 1
        if len_type_id == 0:
            bit_len = consume(packet, 15)
            bits += 15
            read = 0
            # print(f'PACKET v{version} t{type} l{len_type_id} b{bit_len}')
            # print(f'reading {bit_len} bits')
            while read < bit_len:
                v, b, val = read_packet(packet)
                read += b
                bits += b
                version += v
                vals.append(val)
                # print(f'{read} {bit_len}')
        else:
            num_packets = consume(packet, 11)
            bits += 11
            # print(f'PACKET v{version} t{type} l{len_type_id} n{num_packets}')
            # print(f'reading {num_packets} packets')
            for i in range(num_packets):
                v, b, val = read_packet(packet)
                version += v
                bits += b
                vals.append(val)
        
        if type == 0:
            expr = sum(vals)
        elif type == 1:
            expr = prod(vals)
        elif type == 2:
            expr = min(vals)
        elif type == 3:
            expr = max(vals)
        elif type == 5:
            expr = 1 if vals[0] > vals[1] else 0
        elif type == 6:
            expr = 1 if vals[0] < vals[1] else 0
        elif type == 7:
            expr = 1 if vals[0] == vals[1] else 0

    return version, bits, expr



def solve(input):
    packet = bits(input)

    ans = read_packet(packet)
    print(f'VERSION SUM: {ans[0]}; EXPRESSION {ans[2]}')


# solve('8A004A801A8002F478')
# solve('620080001611562C8802118E34')
# solve('C0015000016115A2E0802F182340')
# solve('A0016C880162017C3686B18A3D4780')

solve('C200B40A82')
solve('04005AC33890')
solve('880086C3E88112')
solve('CE00C43D881120')
solve('D8005AC2A8F0')
solve('F600BC2D8F')
solve('9C005AC2F8F0')
solve('9C0141080250320F1802104A08')

solve(parse_file('input.txt'))
