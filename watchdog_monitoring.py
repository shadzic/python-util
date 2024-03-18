# Watchdog tutorial: https://thepythoncorner.com/posts/2019-01-13-how-to-create-a-watchdog-in-python-to-look-for-filesystem-changes/

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time

def create_event_handler():
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    return my_event_handler


def on_created(event):
    print(f"hey, {event.src_path} has been created!")

def create_observer(dir:str="data/"):
    my_event_handler = create_event_handler()
    my_observer = Observer()
    my_observer.schedule(my_event_handler, dir, recursive=False)
    return my_observer


my_observer = create_observer()
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
