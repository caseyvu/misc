#!/usr/bin/env python
import itertools

WEAPONS = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
ARMORS = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
RINGS= [(0,0,0),(0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]

BOSS_HIT_POINT = 103
BOSS_DAMAGE = 9
BOSS_DEFENSE = 2
PLAYER_HIT_POINT = 100

def check_if_win(p_hit_point, p_damage, p_defense, b_hit_point, b_damage, b_defense):
    damage1 = p_damage - b_defense if p_damage > b_defense else 1
    boss_die_after = b_hit_point / damage1
    if b_hit_point % damage1 > 0:
        boss_die_after += 1

    damage2 = b_damage - p_defense if b_damage > p_defense else 1
    player_die_after = p_hit_point / damage2
    if p_hit_point % damage2 > 0:
        player_die_after += 1

    if player_die_after >= boss_die_after:
        return True
    return False

def min_cost():
    MIN_COST = None
    for weapon in WEAPONS:
        for armor in ARMORS:
            for rings_comb in itertools.combinations(RINGS,2):
                items = [weapon, armor] + [i for i in rings_comb]
                cost = sum([item[0] for item in items])
                damage = sum([item[1] for item in items])
                defense = sum([item[2] for item in items])
                if check_if_win(PLAYER_HIT_POINT, damage, defense, BOSS_HIT_POINT, BOSS_DAMAGE, BOSS_DEFENSE):
                    if MIN_COST is None or MIN_COST > cost:
                        MIN_COST = cost
    return MIN_COST

def max_cost(): # yet still lose
    MAX_COST = None
    for weapon in WEAPONS:
        for armor in ARMORS:
            for rings_comb in itertools.combinations(RINGS,2):
                items = [weapon, armor] + [i for i in rings_comb]
                cost = sum([item[0] for item in items])
                damage = sum([item[1] for item in items])
                defense = sum([item[2] for item in items])
                if check_if_win(PLAYER_HIT_POINT, damage, defense, BOSS_HIT_POINT, BOSS_DAMAGE, BOSS_DEFENSE) is False:
                    if MAX_COST is None or MAX_COST < cost:
                        MAX_COST = cost
    return MAX_COST

print "Min cost yet win: %d" % min_cost()
print "Max cost yet lost: %d" % max_cost()