DAY = 21
from collections import Counter as C

SHOP = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

def part1(data, shop):
    data = C(parse_data(data.replace("Hit Points", "Hp").split("\n")))
    weapons, armor, rings = parse_shop(shop.split("\n"))
    return solve_part1(data, weapons, armor, rings)

def solve_part1(data, weapons, armor, rings):
    user = C({'Hp': 100, 'Damage': 0, 'Armor': 0, 'Cost':0})
    cost = float("inf")
    for w in possible_weapons(weapons):
        uw = user + w
        for a in possible_armor(armor):
            ua = uw +a
            for r in possible_rings(rings):
                ur = ua + r
                if user_wins(ur, data.copy()):
                    cost = min(cost, ur["Cost"])
    return cost
                    

def part2(data, shop):
    data = C(parse_data(data.replace("Hit Points", "Hp").split("\n")))
    weapons, armor, rings = parse_shop(shop.split("\n"))
    return solve_part2(data, weapons, armor, rings)

def solve_part2(data, weapons, armor, rings):
    user = C({'Hp': 100, 'Damage': 0, 'Armor': 0, 'Cost':0})
    cost = float("-inf")
    for w in possible_weapons(weapons):
        uw = user + w
        for a in possible_armor(armor):
            ua = uw +a
            for r in possible_rings(rings):
                ur = ua + r
                if not user_wins(ur, data.copy()):
                    cost = max(cost, ur["Cost"])
    return cost

def possible_weapons(weapons):
    for k in weapons:
        yield C({"Cost":k[0], "Damage":k[1], "Armor":k[2]})
        
def possible_armor(armor):
    yield C()
    for k in armor:
        yield C({"Cost":k[0], "Damage":k[1], "Armor":k[2]})

def possible_rings(rings):
    yield C()
    for k in rings:
        yield C({"Cost":k[0], "Damage":k[1], "Armor":k[2]})
    for k in rings:
        kk = C({"Cost":k[0], "Damage":k[1], "Armor":k[2]})
        for j in rings:
            if j != k:
                yield C({"Cost":j[0], "Damage":j[1], "Armor":j[2]}) + kk

def parse_data(data):
    return {i:int(k) for i,k in dict(map(lambda x: x.split(": "), data)).items()}

def parse_shop(data):
    weapons = []
    for j in range(1,len(data)):
        if data[j] == "":
            break
        
        weapons.append(list(map(int, data[j].split()[-3:])))

    armor = []
    for j in range(j+2,len(data)):
        if data[j] == "":
            break
        
        armor.append(list(map(int, data[j].split()[-3:])))

    rings = []
    for j in range(j+2,len(data)):
        if data[j] == "":
            break
        
        rings.append(list(map(int, data[j].split()[-3:])))
    return weapons, armor, rings

def user_wins(user, boss):
    def get_damage(p1, p2):
        return max(p1["Damage"] - p2["Armor"],1)

    while 1:
        boss["Hp"] -= get_damage(user, boss)
        if boss["Hp"] <= 0:
            return 1
        user["Hp"] -= get_damage(boss, user)
        if user["Hp"]  <= 0:
            return 0


DATA = """Hit Points: 103
Damage: 9
Armor: 2"""

print(part1(DATA, SHOP))
print(part2(DATA, SHOP))
