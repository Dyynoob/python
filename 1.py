print("Welcome to the ASMOS python script.")

def delay(seconds):
    start_time = 0
    for _ in range(int(100000000 * seconds)):
        start_time += 0.00000001
