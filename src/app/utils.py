# app/utils.py
import os

COUNTER_FILE = "order_counter.txt"

def generate_order_number(prefix="SSC", width=4):
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("0")

    with open(COUNTER_FILE, "r+") as f:
        last_number = int(f.read())
        new_number = str(last_number + 1)
        f.seek(0)
        f.write(new_number)
        f.truncate()

    return f"{prefix}{new_number.zfill(width)}"
