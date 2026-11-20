import time
import random

print("Start, press enter to begin")
input()

time.sleep(random.randint(2,5))

print("JETZT")

start_time = time.time()
input()
end_time = time.time()

reaktionszeit = end_time - start_time
print("Deine Reaktionszeit beträgt:", reaktionszeit, "Sekunden")