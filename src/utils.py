from typing import List
from logger import infoLogger
import re 
def TotalAmountOfDamage(damageList : List[int]):
    total = 0
    for damage in damageList:
        total += int(damage)
    return total 

def TotalAmountOfHeal(healList : List[int]):
    total = 0
    for heal in healList : 
        total += int(heal)
    return total

def update_hero_rankings(heroes: list["Hero"]) -> None:
    ranked_by_damage = sorted(heroes, key=lambda h: h.TotalAmountOfDamage, reverse=True)
    for rank, hero in enumerate(ranked_by_damage, 1):
        hero.DamageRank = rank

    ranked_by_heal = sorted(heroes, key=lambda h: h.TotalAmountOfHeal, reverse=True)
    for rank, hero in enumerate(ranked_by_heal, 1):
        hero.HealRank = rank

    ranked_by_shield = sorted(heroes, key=lambda h: h.TotalAmountOfShield, reverse=True)
    for rank, hero in enumerate(ranked_by_shield, 1):
        hero.ShieldRank = rank

    
def extractPlayerName(line):
    infoLogger.debug(f"Line: '{line}'")
    match = re.search(r"^\s*([\wÀ-ÖØ-öø-ÿ'-]+)", line)
    infoLogger.debug(f"Match: {match}")
    if match:
        pseudo = match.group(1)
        #infoLogger.info(f"Player name extracted: {pseudo}")
        return pseudo

def formatNumber(num: int) -> str:
    """
    Formate un nombre avec des suffixes standard :
    K = milliers, M = millions, B = milliards.
    
    Exemples :
        930       -> "930"
        1050      -> "1.1K"
        1750      -> "1.8K"
        2670      -> "2.7K"
        1250000   -> "1.2M"
        2000000000 -> "2.0B"
    """
    # Milliards
    if abs(num) >= 1_000_000_000:
        return f"{num / 1_000_000_000:.1f}B"
    # Millions
    elif abs(num) >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    # Milliers
    elif abs(num) >= 1_000:
        return f"{num / 1_000:.1f}K"
    # En dessous de 1000 → brut
    else:
        return str(num)

def checkIndirectCompatibility(IncomingValue, hero):
    from GameHeroes import GameHeroes
    if IncomingValue["indirect"] != None :
        for spell in hero.spells:
            if spell.name in IncomingValue["indirect"]:
                return 1
    return 0

def isControlledByAI(line) :
    match = re.search(r"isControlledByAI=(true|false)", line)
    if match:
        return match.group(1).lower() == "true"
    return None