"""
Fuente: https://www.programiz.com/python-programming/datetime/timestamp-datetime
"""

from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

# print("dt_object =", dt_object)

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)
# print("timestamp =", timestamp)

# Diferencia entre date y timestamp

timestamp = 1607025879
message_date = datetime.fromtimestamp(int(timestamp)).date()
result = datetime.now().date() - message_date
print(result.days)
