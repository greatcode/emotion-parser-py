from threading import Timer
import time

class Repository:

  def __init__(self):
    self._delay = 1.0
    self._timers = []

  def save(self, emotions):
    TIMEOUT_THRESHOLD_MS = 3.0
    delay = self._delay * (len(self._timers) + 1)

    if (delay > TIMEOUT_THRESHOLD_MS):
      def simulateTimeout():
        self._timers.pop(0)
        raise Exception('Database timeout')

      t = Timer(delay, simulateTimeout)
      t.start()
      self._timers.append(t)
      return

    def simulateSuccess():
      self._timers.pop(0)
      print('done')

    t = Timer(delay, simulateSuccess)
    t.start()
    self._timers.append(t)



class Parser:

  def parsePhrases(self, text):
    time.sleep(1.0)
    return []

  def detectEmotion(self, phrase):
    time.sleep(1.0)
    return []


