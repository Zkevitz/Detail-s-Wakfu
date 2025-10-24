import json
from typing import Iterable, Any
import random
from Hero.hero import Hero
from Hero.GameHeroes import GameHeroes

def _to_serializable(obj: Any):
    """
    Tente de convertir un objet en une forme sérialisable en JSON :
    - Si c'est un type simple (int, float, str, bool, None) -> retourne tel quel
    - Si c'est une dict -> convertit récursivement
    - Si c'est une list/tuple/set -> convertit récursivement en list
    - Si l'objet a __dict__ -> utilise obj.__dict__ (converti récursivement)
    - Sinon -> retourne str(obj) en dernier recours
    """
    # Types primitifs JSON-friendly
    if obj is None or isinstance(obj, (str, int, float, bool)):
        return obj

    if isinstance(obj, dict):
        return {str(k): _to_serializable(v) for k, v in obj.items()}

    if isinstance(obj, (list, tuple, set)):
        return [_to_serializable(v) for v in obj]

    # Si l'objet a __dict__, on l'utilise (ex: instances de classes)
    if hasattr(obj, "__dict__"):
        return _to_serializable(obj.__dict__)

    # Si l'objet a une représentation en dict via une méthode comme to_dict()
    if hasattr(obj, "to_dict") and callable(getattr(obj, "to_dict")):
        try:
            return _to_serializable(obj.to_dict())
        except Exception:
            pass

    # Dernier recours : représentation textuelle
    try:
        return str(obj)
    except Exception:
        return None


def extractData(playedHeroes: Iterable) :
    """
    Extrait toutes les valeurs des objets dans playedHeroes et les écrit dans un fichier JSON.
    - playedHeroes : itérable d'objets Hero
    - output_filename : nom du fichier de sortie (par défaut 'rapport.json')
    """
    data_list = []
    numero = random.randint(1000, 9999)
    output_filename = f"Rapport/rapport_{numero}.json"
    for hero in playedHeroes:
        # Tenter d'obtenir un dict propre à partir de l'objet hero
        # On utilise d'abord __dict__ si disponible, sinon on tente une conversion générique
        if hasattr(hero, "__dict__"):
            hero_dict = _to_serializable(hero.__dict__)
        else:
            # Si l'objet n'a pas __dict__, on tente une conversion générique
            hero_dict = _to_serializable(hero)

        # Assurer que les clés utiles existent (optionnel)
        # Remplace les objets complexes par leurs versions sérialisées
        # (la fonction _to_serializable a déjà converti récursivement)
        data_list.append(hero_dict)

    # Écrire dans le fichier JSON (remplace le fichier existant)
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)

    print(f"Export terminé : {output_filename} ({len(data_list)} héros exportés)")
    return output_filename

def loadHeroesFromJson(input_filename: str, playedHeroes: list[Hero]) -> list[Hero]:
    print(input_filename)
    if len(playedHeroes) != 0 :
        for hero in playedHeroes :
            hero.clear()
        playedHeroes.clear()
    try:
        with open(input_filename, "r", encoding="utf-8") as f:
            data_list = json.load(f)
    except FileNotFoundError:
        print(f"❌ Fichier introuvable : {input_filename}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de lecture JSON : {e}")
        return []

    heroes = []
    for data in data_list:
        #Création de base avec les seuls arguments du constructeur
        tmphero = Hero(
            className=data.get("className", "Inconnu"),
            name=data.get("name", "")
        )
        for hero in GameHeroes:
            if hero.className == tmphero.className:
                hero = hero
                break
        # Réinjection des autres attributs s’ils existent dans le JSON
        for key, value in data.items():
            if hasattr(hero, key):
                setattr(hero, key, value)

        playedHeroes.append(hero)
    return (playedHeroes)