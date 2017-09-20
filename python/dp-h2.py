import sys
import time
from datetime import datetime, timedelta

class Timer(object):
    def __init__ (self):
        now = datetime.now()
        self._inital = now
        self.start = now
        self.stop = None
        self._last_lap = None
        self.laps = []

    @property
    def total_elapsed(self):
        elapse = (datetime.now() - self._inital)
        return elapse.seconds + elapse.microseconds / 1000000.0
    @property
    def current(self):
        lp = (self.stop - self.start) if self.stop else (datetime.now() - self.start)
        return lp.seconds + lp.microseconds / 1000000.0

    def stop_now(self):
        self.stop = datetime.now()
        return self.current

    def start_now(self):
        self.stop = None
        self.start = datetime.now()
        return self.current

    def record_lap(self):
        now = datetime.now()
        if self._last_lap:
            lp = now -self._last_lap
        elif self.stop:
            lp = self.stop - now
        else:
            lp = now - self.start
        self.laps.append(lp)
        self._last_lap = now
