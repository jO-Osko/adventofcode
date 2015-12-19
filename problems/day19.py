DAY = 19

def part1(data):
    changes, start = parse_data(data.split("\n"))
    return len(make_next(start, changes))

def parse_data(data, reverse=False):
    changes = []
    for line in data:
        if not line.strip():
            break
        if reverse:
            changes.append(list(reversed(line.strip().split(" => "))))
        else:
            changes.append(line.strip().split(" => "))
    return changes, data[-1].strip()

def make_next(starter, changes):
    replaced = set()
    len_s = len(starter)
    for old, new in changes:
        le = len(old)
        for j in range(len_s - le +1):
            if starter[j:j+le] == old:
                replaced.add(starter[:j] + new + starter[j+le:])
    return replaced

def part2(data):
    changes, start = parse_data(data.split("\n"), True)
    changes.sort(key= lambda x: -len(x[0]))
    return find_shortest_path(start, "e", changes)

# Greedy, but works fast enough
def find_shortest_path(start, end, changes):
    mi = float("inf")
    def find_path(current, cost):
        if current == end:
            nonlocal mi
            if cost < mi:
                mi = cost
                print(mi)
        for nex in make_next(current, changes):
            find_path(nex, cost+1)

    find_path(start, 0)
    return mi

DATA = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"""

print(part1(DATA))
print(part2(DATA))
