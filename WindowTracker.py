import time
import sqlite3
import pygetwindow as gw
import re

class WindowTracker:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
        self.pattern = r'[^-|]*$'
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS window_activity
                           (timestamp TEXT, window_title TEXT, window_detailed_title TEXT)''')
        self.conn.commit()
    
    def track_window_activity(self):
        while True:
            a = gw.getActiveWindowTitle()
            a = a or ''
            b = re.search(self.pattern, a).group().strip()
            
            current_timestamp = time.strftime("%Y-%m-%dT%H-%M-%S")
            
            self.c.execute("INSERT INTO window_activity VALUES (?, ?, ?)", (current_timestamp, b, a))
            self.conn.commit()
            
            time.sleep(2)
if __name__ == "__main__":
    tracker = WindowTracker('window_tracking.db')
    tracker.create_table()
    tracker.track_window_activity()
