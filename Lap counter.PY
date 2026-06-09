lap_count = 0

print("Lap Counter Started")
print("Press ENTER to record a lap, or type 'stop' to finish.\n")

while True:
    user_input = input("Lap event: ")

    if user_input.lower() == "stop":
        break

    lap_count += 1
    print(f"Lap {lap_count} recorded!")

print(f"\nTotal laps: {lap_count}")

