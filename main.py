import time

def microwave(power, duration):
    print("Microwave started.")
    print("Power: {}%".format(power))
    print("Duration: {} seconds".format(duration))

    # Convert duration from seconds to milliseconds
    duration_ms = duration * 1000

    # Calculate time intervals for power levels
    interval = duration_ms // power

    # Simulate microwave operation
    for i in range(power, 0, -10):
        print("Power: {}%".format(i))
        time.sleep(interval / 1000)

    # Simulate end of operation
    print("Microwave finished.")

# Usage: Call the function with desired power and duration
microwave(power=50, duration=30)
