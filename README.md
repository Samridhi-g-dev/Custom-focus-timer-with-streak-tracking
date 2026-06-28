# ⏳Custom Focus Timer with Streak-Tracking

A lightweight, terminal-based Pomodoro and focus timer written in Python. It helps you lock into your work, customize your session lengths, track your total focus hours, and calculate your daily streak to keep your momentum alive.  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Features

* **Flexible Durations**: Choose from classic presets (25, 45, 60 minutes) or set a custom time tailored to your workflow.  
* **Audio Alerts**: Uses system beeps (\`winsound\`) to notify you exactly when a session starts and finishes.  
* **Streak Tracking**: Automatically calculates your current daily focus streak based on consecutive days of logged work.  
* **Local Data Logging**: Saves your history safely to a local JSON file—no external databases or internet required.  
* **Integrated Breaks**: Promptly offers a quick 5-minute cooldown break right after completing a focus session. 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Getting started:

\#\#\# Prerequisites

1. **Operating System:** Windows (Required for the \`winsound\` audio notifications).   
2. **Python:** Python 3.x installed.

\#\#\# Installing & Running

1. Clone or download this repository to your local machine.  
2. Open your terminal/command prompt and navigate to the project directory.  
3. Run the script using Python: 

\`\`\`bash  
python [timer.py](http://timer.py)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# How to Use?

When you launch the script, you'll be greeted with a simple interactive menu:  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Welcome to Focus Timer\!  
Select an option:  
1\. Start Focus Session   
2\. Start Break   
3\. View Stats   
4\. Exit   
Enter choice (1-4):  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- **Select 1** to start working. You can give your session a custom label (e.g., "Coding", "Reading") and pick your duration.  
- **Select 3** at any time to view your dashboard, which displays:  
* Today's total focus time and session count.  
* All-time accumulated focus hours.  
* Your current daily streak.

# Data Storage

Your progress is automatically saved to a file named sessions.json in the same directory. The data is structured as an array of objects, looking like this:   
\[  
  {  
    "date": "2026-06-01",  
    "time": "14:30:00",  
    "duration": 25,  
    "label": "Coding"  
  }  
\]  
⚠️ Note: Do not manually edit or corrupt the sessions.json file, or your stats history might reset\! 

