import time
import platform
import os
import subprocess

def install_beep():
    try:
        print("🔧 Installing 'beep'...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "beep"], check=True)
        print("✅ 'beep' installed successfully.")
    except subprocess.CalledProcessError:
        print("❌ Failed to install 'beep'. Please install it manually.")

def play_sound():
    os_name = platform.system()

    if os_name == "Windows":
        import winsound
        winsound.Beep(1000, 800)

    elif os_name == "Darwin":  # macOS
        os.system('say "Time\'s up!"')

    elif os_name == "Linux":
        if os.system("which beep > /dev/null") != 0:
            install_beep()
        os.system("beep -f 1000 -l 500")

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
