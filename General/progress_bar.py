from rich.progress import track
import time

range_progress = 20
for n in track(range(range_progress), description="Processing..."):
    time.sleep(1)
    continue