from collections import defaultdict
import time

last_triggered = defaultdict(float)

def can_trigger(identifier, cooldown=300):
    now = time.time()
    if now - last_triggered[identifier] > cooldown:
        last_triggered[identifier] = now
        return True
    return False
