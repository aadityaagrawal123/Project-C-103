import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Dell/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        file_name = os.path.basename(event.src_path)
        print("Hello!","A file named","'",file_name,"'","with the path","'",event.src_path,"'","has been created...")

    def on_deleted(self, event):
        file_name = os.path.basename(event.src_path)
        print("Oh No!","A file named","'",file_name,"'","having the path","'",event.src_path,"'","has been deleted by someone...")

    def on_modified(self, event):
        file_name = os.path.basename(event.src_path)
        print("Looks like a file named","'",file_name,"'","having the path","'",event.src_path,"'","has been modified...")

    def on_moved(self, event):
        file_name = os.path.basename(event.src_path)
        print("Found That a file named","'",file_name,"'","having the path","'",event.src_path,"'","has been moved to another location...")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive= True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("The Program is running....",end='\r')
except KeyboardInterrupt:
        print("The program has been stopped!")
        observer.stop()