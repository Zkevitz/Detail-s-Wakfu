from utils import TotalAmountOfDamage, TotalAmountOfHeal, extractPlayerName, update_hero_rankings, checkIndirectCompatibility
from interface_support import updateHeroValue
from logger import infoLogger, errorLogger
from Hero.GameHeroes import GameHeroes
#from extractData import extractData
import re

PlayedHeroes = []
lastHeroes = None
def parseSpellInLine(line):
    global lastHeroes
    match = re.search(r"lance le sort\s+([^(]+?)(?:\s*\([^)]*\))?$", line)
    if match :
        match = match.group(1).strip()
        print(match)
        for hero in PlayedHeroes:
            for spell in hero.spells:
                if spell.name == match:
                    lastHeroes = hero
                    hero.UsedSpell.append(spell)
                    return spell
    lastHeroes = None
    return None

def parseDamageInLine(line):
    match = re.search(r"([+-])\s*([\d\s ]+)\s*PV", line)
    element = re.search(r'PV\s*\(([^)]+)\)', line)
    indirect = re.search(r'\(([^()]*)\)(?!.*\([^()]*\))', line)
    if match:
        sign = match.group(1)   
        #print("match group 2 --> ", match.group(2))
        value = re.sub(r'\D', '', match.group(2))  # nettoyage espaces
        if element :
            parsedElement = element.group(1)
        if indirect :
            parsedIndirect = indirect.group(1)
            print("indirect --> ", parsedIndirect)
        return {"sign": sign, "value": value, "element": parsedElement, "indirect": parsedIndirect} 
    return None

def parseShieldInLine(line):
    pattern = r'(\d[\d\u00A0\u202F ]*)(?=\s*Armure\b)'
    match = re.search(pattern, line, flags=re.IGNORECASE)
    indirect = re.search(r'\(([^()]*)\)(?!.*\([^()]*\))', line)
    parsedIndirect = None
    if not match:
        return None

    raw_number = match.group(1)
    cleaned = re.sub(r'[\s\u00A0\u202F]', '', raw_number)
    if indirect :
        parsedIndirect = indirect.group(1)
        print("indirect --> ", parsedIndirect)
    try:
        value = int(cleaned)
    except ValueError:
        return None

    print(f"nombre d'armure trouve : {value}")
    return {"sign": "+", "value": value, "element": "Shield", "indirect": parsedIndirect}
    
def handle_spell(line):
    global lastHeroes
    #infoLogger.info(f"handle spell -->  {line}")
    IncomingValue = parseDamageInLine(line)
    if "pour le tour suivant." in line and lastHeroes != None:
        lastHeroes.PlayedTurn += 1
    print(lastHeroes)
    if IncomingValue and lastHeroes:
        for hero in PlayedHeroes:
            if lastHeroes != None and hero.name == lastHeroes.name or checkIndirectCompatibility(IncomingValue, hero) == 1:
                if IncomingValue["sign"] == '+' and IncomingValue["element"] != "Shield":
                    hero.HealDone.append(int(IncomingValue["value"]))
                    hero.TotalAmountOfHeal += int(IncomingValue["value"])
                elif IncomingValue["element"] == "Shield":
                    hero.ShieldDone.append(int(IncomingValue["value"]))
                    hero.TotalAmountOfShield += int(IncomingValue["value"])
                else :
                    hero.DamageDone.append(int(IncomingValue["value"]))
                    hero.TotalAmountOfDamage += int(IncomingValue["value"])
                break      
        update_hero_rankings(PlayedHeroes)
        updateHeroValue(PlayedHeroes)

def handleShield(line) :
    IncomingValue = parseShieldInLine(line)
    if IncomingValue :
        for hero in PlayedHeroes: 
            if lastHeroes != None and hero.name == lastHeroes.name :
                hero.ShieldDone.append(int(IncomingValue["value"]))
                hero.TotalAmountOfShield += int(IncomingValue["value"])
                break
        update_hero_rankings(PlayedHeroes)
        updateHeroValue(PlayedHeroes)