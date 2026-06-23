import time
import json
import os
from datetime import datetime, date, timedelta
import winsound

# Settings
SESSIONS_FILE = "sessions.json"
FOCUS_MIN = 25
BREAK_MIN = 5

# ── Load sessions from disk (returns empty list if none yet) ──
def load_sessions():
    if os.path.exists(SESSIONS_FILE):
        try:
            with open(SESSIONS_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except (json.JSONDecodeError, IOError):
            # Corrupt file or read error — fall through to return empty list
            pass
    # No file or invalid contents -> return empty list
    return []

# ── Save sessions to disk (appends new session) ──
def save_sessions(duration_min, session_name):
    sessions = load_sessions()
    sessions.append({
        "date": str(date.today()),
        "time": datetime.now().strftime("%H:%M:%S"),
        "duration": duration_min,
        "label": str(session_name)
    })
    try:
        with open(SESSIONS_FILE, "w") as f:
            json.dump(sessions, f, indent=2)
    except IOError:
        print(" Warning: could not save sessions to disk.")

def pick_duration():
    print("\n  How long?")
    print("  [1] 25 min  [2] 45 min  [3] 60 min  [4] Custom")
    choice = input("  → ").strip()
    if choice == "1": return 25
    elif choice == "2": return 45
    elif choice == "3": return 60
    elif choice == "4":
        while True:
            try:
                mins = int(input("  Minutes (1–180): "))
                if 1 <= mins <= 180: return mins
                print("  Must be 1–180.")
            except ValueError:
                print("  Enter a number.")
    return 25


def timer(min, tag):
    winsound.Beep(1000, 500)  # Start sound
    total_sec = min * 60
    print(f"\n Session {tag} starts now! ({min} min)\n")
    for remaining in range(total_sec, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"\r {mins:02d}:{secs:02d} down", end="", flush=True)
        time.sleep(1)
    print(f"\n Session {tag} completed! \n")
    winsound.Beep(1000, 500)  # End sound
    

# STATS
def show_stats():
    sessions = load_sessions()
    if not sessions:
        print("\n No sessions recorded yet. Lock in!\n")
        return
    
    today = str(date.today())
    today_sessions = [s for s in sessions if s["date"] == today]
    today_focus = sum(s["duration"] for s in today_sessions)
    total_focus = sum(s["duration"] for s in sessions)

    streak = 0
    check_date = date.today()
    dates_done = set(s["date"] for s in sessions)
    while str(check_date) in dates_done:
        streak += 1
        check_date -= timedelta(days=1)

    print("\n" + "─" * 32)
    print(" YOUR FOCUS STATS")
    print("─" * 32)
    print(f" Today: {len(today_sessions)} sessions ({today_focus} min)")
    print(f" All Time: {total_focus // 60}hr {total_focus % 60}min")
    print(f" Current Streak: {streak} day(s)")
    print("─" * 32 + "\n")


def main():
    print("\n Welcome to Focus Timer! \n")
    while True:
        print(" Select an option:")
        print(" 1. Start Focus Session")
        print(" 2. Start Break")
        print(" 3. View Stats")
        print(" 4. Exit")
        choice = input(" Enter choice (1-4): ").strip()

        if choice == "1":
            name = input("\n  Name this session (Enter to skip): ").strip()
            if name == "": name = "Focus"
            duration = pick_duration()
            input(f"\n Press Enter to start a {duration}-minute focus session...")
            timer(duration, name)
            save_sessions(duration, name)
            print(f"  Saved: {duration} min of '{name}'. Great work!")
            brk = input("\n Great job! Time for a break? (y/n)\n")
            if brk == "y": timer(BREAK_MIN, "Break")
        elif choice == "2":
            timer(BREAK_MIN, "BREAK")
        elif choice == "3":
            show_stats()
        elif choice == "4":
            print("\n See you soon! Stay focused! \n")
            break
        else:
            print("\n Invalid choice. Try again. \n")


main()

          
        

    
