from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

dt_string = now.strftime("%Y%m%d_%H-%M-%S")

f = open(dt_string+".txt", "x")