from threading import Thread
import lookup_drive_change
from ctypes import windll
import string

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


def read_dir():

    drives = get_drives()
    for drive in drives:
        t = Thread(target=lookup_drive_change.lookup(drive+':\\'))
        # t.daemon = True
        t.start()