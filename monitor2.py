#from statistics import multimode
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
import time
from pathlib import Path
from logger import infoLogger, errorLogger
from calc import handle_spell, parseSpellInLine, handleShield
from GameHeroes import handleNewFight, NewHero#, handleEndFight
lastBytesRead = 0
class MyHandler(FileSystemEventHandler):
    def __init__(self, file):
        infoLogger.info("Initialisation du handler")
        self.file = Path(file)
        self.position = 0
        with open(self.file, "r") as f:
            f.seek(self.position)
            new_content = f.read()
            self.position = f.tell()

    def on_any_event(self, event):
        """
        Cette méthode est appelée pour tous les événements :
        - modified, created, moved, deleted
        """
        #from interface_support import MultiMode
        if Path(event.src_path).name == self.file.name:
            if self.file.exists():
                with open(self.file, "r") as f:  
                    f.seek(self.position)
                    new_content = f.read()
                    allNewLine = new_content.split("\n")
                    for l in allNewLine :
                        if l.startswith(' INFO ') :
                            if "CREATION DU COMBAT" in l:
                                handleNewFight()
                                infoLogger.info("Nouveau combat")
                            elif "eNh:1402" in l :
                                NewHero(l)
                            elif "lance le sort" in l :
                                parseSpellInLine(l)
                            elif "PV" in l :
                                handle_spell(l)
                            elif "Armure" in l :
                                handleShield(l)
                            #elif "FIN DU COMBAT" in l:
                            #    handleEndFight()
                            #    infoLogger.info("Fin du combat")
                        errorLogger.debug("Nouveau contenu :", l)
                    self.position = f.tell()


file = "/mnt/c/Users/Zkevitz/AppData/Roaming/zaap/gamesLogs/wakfu/logs/wakfu.log"
fileCheck = Path(file)
if not fileCheck.exists():
    infoLogger.info("le fichier n'existe pas")
    exit()
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