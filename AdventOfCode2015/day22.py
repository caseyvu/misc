#!/usr/bin/env python
SPELLS =[[53, 1, 4, 0, 0, 0], [73, 1, 2, 2, 0, 0], [113, 6, 0, 0, 7, 0], [173, 6, 3, 0, 0, 0], [229, 5, 0, 0, 0, 101]]

BOSS_DAMAGE = 9
BOSS_HIT_POINT = 58
PLAYER_HIT_POINT = 50
PLAYER_MANA = 500

def play(spell, p_mana, p_hit_point, s_timer, p_timer, r_timer, b_hit_point, spent, min_mana, hard=0):
    # Before player play
    if(s_timer > 0):
        s_timer -= 1
    if(p_timer > 0):
        b_hit_point -= SPELLS[3][2]
        if b_hit_point <= 0 and spent < min_mana: # we win
            min_mana = spent
        p_timer -= 1
    if(r_timer > 0):
        p_mana += SPELLS[4][5]
        r_timer -= 1

    if((s_timer > 0 and spell == 2) or (p_timer > 0 and spell == 3) or (r_timer > 0 and spell == 4) or b_hit_point <= 0):
        return min_mana

    # Player play
    p_mana -= SPELLS[spell][0]
    spent += SPELLS[spell][0]

    p_hit_point -= hard # to enable hard mode

    if(spell == 0):
        b_hit_point -= SPELLS[spell][2]
    elif(spell == 1):
        b_hit_point -= SPELLS[spell][2]
        p_hit_point += SPELLS[spell][3]
    elif(spell == 2):
        s_timer = SPELLS[spell][1]
    elif(spell == 3):
        p_timer = SPELLS[spell][1]
    elif(spell == 4):
        r_timer = SPELLS[spell][1]

    # Before boss play
    p_defense = 0
    if(s_timer > 0):
        p_defense = SPELLS[2][4]
        s_timer -= 1
    if(p_timer > 0):
        b_hit_point -= SPELLS[3][2]
        p_timer -= 1
    if(r_timer > 0):
        p_mana += SPELLS[4][5]
        r_timer -= 1
    if b_hit_point <= 0 and spent < min_mana: # we win
        min_mana = spent
    p_hit_point -= (BOSS_DAMAGE - p_defense)
    if(p_hit_point <= 0 or p_mana < 0 or spent > min_mana or b_hit_point <= 0): # cut branch
        return min_mana

    # Player decide on next move
    for next_spell in range(len(SPELLS)):
        min_mana = play(next_spell, p_mana, p_hit_point, s_timer, p_timer, r_timer, b_hit_point, spent, min_mana, hard)
    return min_mana

# Part 1
min_mana = 9999
for next_spell in range(len(SPELLS)):
    min_mana = play(next_spell, PLAYER_MANA, PLAYER_HIT_POINT, 0, 0, 0, BOSS_HIT_POINT, 0, min_mana, hard=0)
print "(a) Result: %d" % min_mana

# Part 2
min_mana = 9999
for i in range(5):
    min_mana = play(i, PLAYER_MANA, PLAYER_HIT_POINT, 0, 0, 0, BOSS_HIT_POINT, 0, min_mana, hard=1)
print "(b) Result: %d" % min_mana