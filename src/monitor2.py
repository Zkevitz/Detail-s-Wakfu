from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
from logger import infoLogger, errorLogger
from calc import handle_spell, parseSpellInLine, handleShield
from Hero.GameHeroes import handleNewFight, NewHero

class MyHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file = Path(file_path)
        self.position = 0
        infoLogger.info(f"Initialisation du handler pour {self.file}")

        # Lecture initiale (ignore le contenu existant)
        if self.file.exists():
            with open(self.file, "r", encoding="utf-8") as f:
                f.seek(0, 2)
                self.position = f.tell()

    def process_file(self):
        """Lit le nouveau contenu du fichier depuis la dernière position connue."""
        if not self.file.exists():
            return

        with open(self.file, "r", encoding="utf-8") as f:
            f.seek(self.position)
            new_content = f.read()

            if not new_content:
                return  # Rien de nouveau

            allNewLine = new_content.split("\n")
            for l in allNewLine:
                if not l.strip():
                    continue
                if l.startswith(" INFO "):
                    print(l)
                    if "CREATION DU COMBAT" in l:
                        handleNewFight()
                        infoLogger.info("Nouveau combat détecté")
                    elif "eNh:1402" in l:
                        NewHero(l)
                    elif "lance le sort" in l:
                        parseSpellInLine(l)
                    elif "PV" in l:
                        handle_spell(l)
                    elif "Armure" in l:
                        handleShield(l)
                errorLogger.debug(f"Nouveau contenu : {l}")

            self.position = f.tell()

    def on_modified(self, event):
        """Quand le fichier log est modifié."""
        if Path(event.src_path).name == self.file.name:
            self.process_file()

    def on_created(self, event):
        """Quand le fichier log est recréé (après rotation)."""
        if Path(event.src_path).name == self.file.name:
            infoLogger.info(f"{self.file.name} recréé, réinitialisation du suivi")
            self.position = 0  # recommencer depuis le début du nouveau fichier
            self.process_file()

    def on_moved(self, event):
        """Quand le fichier log est déplacé (rotation)."""
        if Path(event.src_path).name == self.file.name:
            infoLogger.info(f"{self.file.name} déplacé vers {event.dest_path}")
            self.position = 0  # reset — le fichier d'origine n'existe plus

    def on_deleted(self, event):
        """Quand le fichier log est supprimé."""
        if Path(event.src_path).name == self.file.name:
            infoLogger.info(f"{self.file.name} supprimé")
            self.position = 0
            
file = "/Users/Zkevitz/AppData/Roaming/zaap/gamesLogs/wakfu/logs/wakfu.log"
#file = "/mnt/c/Users/Zkevitz/AppData/Roaming/zaap/gamesLogs/wakfu/logs/wakfu.log"
fileCheck = Path(file)
if not fileCheck.exists():
    infoLogger.info("le fichier n'existe pas")
    sys.exit()
import interface_support
event_handler = MyHandler(file)
observer = PollingObserver()
observer.schedule(event_handler, str(fileCheck.parent), recursive=False)
observer.start()
interface_support.main()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()