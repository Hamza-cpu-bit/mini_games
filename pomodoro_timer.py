import time

def pomodoro_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    print(f"\n⏳ Timer set for {minutes}m {seconds}s\n")

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"⏱ {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up!")

if __name__ == "__main__":
    try:
        minutes = int(input("Enter minutes: ") or 0)
        seconds = int(input("Enter seconds: ") or 0)
        pomodoro_timer(minutes, seconds)
    except ValueError:
        print("❌ Please enter valid numbers.")
