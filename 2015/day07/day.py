def solve_part1(lines: list[str]) -> int:
    gates, wires = parse_input(lines)

    solve_circuit(gates, wires)

    return wires['a']


def solve_part2(lines: list[str]) -> int:
    new_b = solve_part1(lines)
    gates, wires = parse_input(lines)
    wires['b'] = new_b

    solve_circuit(gates, wires)

    return wires['a']


def parse_input(lines):
    wires = {}
    gates = {}
    for line in lines:
        logic, name = line.split(" -> ")
        if logic.isdecimal():
            wires[name] = int(logic)
        else:
            gates[name] = logic
    return gates, wires


def solve_circuit(gates, wires):
    while gates:
        keys = list(gates.keys())
        for gate in keys:
            logic = gates[gate]
            if 'NOT' in logic:
                op, in1 = logic.split(" ")
                if in1 not in wires:
                    continue
                wires[gate] = ~wires[in1] + 65536
            elif 'LSHIFT' in logic or 'RSHIFT' in logic:
                in1, op, in2 = gates[gate].split(" ")
                if in1 not in wires:
                    continue
                in2 = int(in2)
                if op == 'LSHIFT':
                    wires[gate] = wires[in1] << in2
                else:
                    wires[gate] = wires[in1] >> in2
            elif 'AND' in logic or 'OR' in logic:
                in1, op, in2 = gates[gate].split(" ")
                if in1.isdecimal() and in2 in wires:
                    if op == 'AND':
                        wires[gate] = int(in1) & wires[in2]
                    else:
                        wires[gate] = int(in1) | wires[in2]
                elif in2.isdecimal() and in1 in wires:
                    if op == 'AND':
                        wires[gate] = wires[in1] & int(in2)
                    else:
                        wires[gate] = wires[in1] | int(in2)
                else:
                    if in1 not in wires or in2 not in wires:
                        continue
                    if op == 'AND':
                        wires[gate] = wires[in1] & wires[in2]
                    else:
                        wires[gate] = wires[in1] | wires[in2]
            else:
                in1 = gates[gate]
                if in1 not in wires:
                    continue
                wires[gate] = wires[in1]

            gates.pop(gate)
