import time
import platform
import os

def play_sound():
    os_name = platform.system()

    if os_name == "Windows":
        import winsound
        frequency = 1000  # Hz
        duration = 800    # ms
        winsound.Beep(frequency, duration)

    elif os_name == "Darwin":  # macOS
        os.system('say "Time\'s up!"')

    elif os_name == "Linux":
        # Check if beep is available
        if os.system("which beep > /dev/null") == 0:
            os.system("beep -f 1000 -l 500")
        else:
            print("🔔 Time's up! (Install 'beep' for actual sound)")
    else:
        print("🔔 Time's up!")

def pomodoro_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    print(f"\n⏳ Timer set for {minutes}m {seconds}s\n")

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"⏱ {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\n⏰ Time's up!")
    play_sound()

if __name__ == "__main__":
    try:
        minutes = int(input("Enter minutes: ") or 0)
        seconds = int(input("Enter seconds: ") or 0)
        pomodoro_timer(minutes, seconds)
    except ValueError:
        print("❌ Please enter valid numbers.")
