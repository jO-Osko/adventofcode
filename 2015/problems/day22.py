DAY = 22
from collections import Counter as C


DATA = """Hit Points: 58
Damage: 9"""

def part1(data):
    data = C(parse_data(data.replace("Hit Points", "Hp").split("\n")))
    return solve_part(data)

def part2(data):
    data = C(parse_data(data.replace("Hit Points", "Hp").split("\n")))
    return solve_part(data, True)


#Kill my dog, family, tea mug, destroy my car, all to kill one little bug with rewrite..., but finished it 
def solve_part(data, part2=False):
    mi = float("inf")

    def recurse(user_hp=50, boss_hp=data["Hp"], mana=500, shield=0, poison=0, recharge=0, player=1, cost=0):
        if cost >= mi:
            return
        
        if poison:
            boss_hp -= 3
            poison -= 1
        if recharge:
            mana += 101
            recharge -= 1
        
        if boss_hp < 0:
            nonlocal mi
            mi = min(mi,cost)
            return

        if player:

            if part2:
                user_hp -= 1
                if user_hp <= 0:
                    return
            
            if shield:
                shield -= 1

            if mana >= 53:
                recurse(user_hp, boss_hp-4, mana-53, shield, poison, recharge, not player, cost+53)

            if mana >= 73:
                recurse(user_hp + 2, boss_hp-2, mana-73, shield, poison, recharge, not player, cost+73)

            if mana >= 113 and not shield:
                recurse(user_hp, boss_hp, mana-113, 6, poison, recharge, not player, cost+113)

            if mana >= 173 and not poison:
                recurse(user_hp, boss_hp, mana-173, shield, 6, recharge, not player, cost+173)

            if mana >= 229 and not recharge:
                recurse(user_hp, boss_hp, mana-229, shield, poison, 5, not player, cost+229)
            
        else:
            if shield:
                user_hp -= data["Damage"] - 7
                shield -= 1
            else:
                user_hp -= 9

            if user_hp <= 0:
                return
            
            recurse(user_hp, boss_hp, mana, shield, poison, recharge, not player, cost)
        
    recurse()
    return mi
    

def parse_data(data):
    return {i:int(k) for i,k in dict(map(lambda x: x.split(": "), data)).items()}

print(part1(DATA))
print(part2(DATA))
