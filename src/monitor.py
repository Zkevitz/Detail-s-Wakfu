from statistics import multimode
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
import time
from pathlib import Path
from logger import infoLogger, errorLogger
from calc import handle_spell
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
        if Path(event.src_path).name == self.file.name:
            if self.file.exists():
                with open(self.file, "r") as f:  
                    f.seek(self.position)
                    new_content = f.read()
                    #print(f"[[new_content before cut : {new_content}]]")
                    if new_content and "(combat)" in new_content:
                        new_content = new_content.split("[Information (combat)]")
                        #print(f"[[new_content after cut : {new_content}]]")
                        for line in new_content:
                            handle_spell(line)
                        errorLogger.debug("Nouveau contenu :", new_content)
                    self.position = f.tell()


file = "/mnt/c/Users/Zkevitz/AppData/Roaming/zaap/gamesLogs/wakfu/logs/wakfu_chat.log"
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
