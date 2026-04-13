"""
Pomodoro Timer - Stay focused and productive!
Features: Work/break cycles, task tracking, statistics, and notifications
"""

import time
import sys
from datetime import datetime, timedelta
from typing import List, Dict
import json


class PomodoroTimer:
    """Advanced Pomodoro timer with task tracking and statistics."""

    def __init__(self):
        self.work_duration = 25 * 60  # 25 minutes
        self.short_break = 5 * 60  # 5 minutes
        self.long_break = 15 * 60  # 15 minutes
        self.pomodoros_until_long_break = 4

        self.current_pomodoro = 0
        self.tasks: List[Dict] = []
        self.completed_sessions: List[Dict] = []
        self.stats_file = Path("pomodoro_stats.json")

        self.load_stats()

    def load_stats(self):
        """Load previous statistics from file."""
        if self.stats_file.exists():
            try:
                with open(self.stats_file, 'r') as f:
                    data = json.load(f)
                    self.completed_sessions = data.get('sessions', [])
            except Exception:
                pass

    def save_stats(self):
        """Save statistics to file."""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump({
                    'sessions': self.completed_sessions,
                    'last_updated': datetime.now().isoformat()
                }, f, indent=2)
        except Exception as e:
            print(f"⚠️ Could not save stats: {e}")

    def add_task(self, task_name: str, estimated_pomodoros: int = 1):
        """Add a new task to the list."""
        self.tasks.append({
            'name': task_name,
            'estimated': estimated_pomodoros,
            'completed': 0,
            'done': False
        })
        print(f"✅ Added task: {task_name} ({estimated_pomodoros} pomodoros)")

    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\n📋 No tasks yet. Add some to get started!")
            return

        print("\n📋 TASKS")
        print("=" * 50)
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task['done'] else " "
            progress = f"{task['completed']}/{task['estimated']}"
            print(f"{i}. [{status}] {task['name']} - {progress} pomodoros")

    def countdown(self, seconds: int, label: str):
        """Display countdown timer with progress bar."""
        start_time = time.time()
        end_time = start_time + seconds

        try:
            while time.time() < end_time:
                remaining = int(end_time - time.time())
                mins, secs = divmod(remaining, 60)

                # Progress bar
                progress = 1 - (remaining / seconds)
                bar_length = 30
                filled = int(bar_length * progress)
                bar = "█" * filled + "░" * (bar_length - filled)

                # Display
                sys.stdout.write(f"\r{label}: {mins:02d}:{secs:02d} [{bar}] {int(progress * 100)}%")
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write(f"\r{label}: COMPLETE! {'█' * 30} 100%\n")
            sys.stdout.flush()
            return True

        except KeyboardInterrupt:
            print("\n\n⏸️ Timer paused. Press Enter to continue or 'q' to quit...")
            choice = input().strip().lower()
            if choice == 'q':
                return False
            # Resume from where we left off
            remaining_time = int(end_time - time.time())
            if remaining_time > 0:
                return self.countdown(remaining_time, label)
            return True

    def ring_bell(self):
        """Audio notification (terminal bell)."""
        for _ in range(3):
            print('\a', end='', flush=True)
            time.sleep(0.3)

    def start_pomodoro(self, task_index: int = None):
        """Start a work session."""
        self.current_pomodoro += 1

        task_name = "Focus Session"
        if task_index is not None and 0 <= task_index < len(self.tasks):
            task_name = self.tasks[task_index]['name']

        print(f"\n🍅 Pomodoro #{self.current_pomodoro}: {task_name}")
        print("=" * 50)
        print(f"Work for {self.work_duration // 60} minutes. Stay focused!")

        start_time = datetime.now()
        completed = self.countdown(self.work_duration, "⏱️ WORK")

        if completed:
            self.ring_bell()
            print("\n🎉 Great work! Time for a break.")

            # Update task progress
            if task_index is not None and 0 <= task_index < len(self.tasks):
                self.tasks[task_index]['completed'] += 1
                if self.tasks[task_index]['completed'] >= self.tasks[task_index]['estimated']:
                    self.tasks[task_index]['done'] = True
                    print(f"✨ Task completed: {self.tasks[task_index]['name']}")

            # Save session
            self.completed_sessions.append({
                'date': start_time.isoformat(),
                'task': task_name,
                'duration': self.work_duration,
                'type': 'work'
            })
            self.save_stats()

            # Determine break type
            if self.current_pomodoro % self.pomodoros_until_long_break == 0:
                self.start_break(long_break=True)
            else:
                self.start_break(long_break=False)

    def start_break(self, long_break: bool = False):
        """Start a break session."""
        duration = self.long_break if long_break else self.short_break
        break_type = "LONG BREAK" if long_break else "SHORT BREAK"

        print(f"\n☕ {break_type}")
        print("=" * 50)
        print(f"Relax for {duration // 60} minutes.")

        self.countdown(duration, f"⏱️ {break_type}")
        self.ring_bell()
        print("\n✅ Break complete! Ready for another pomodoro?")

    def show_statistics(self):
        """Display productivity statistics."""
        if not self.completed_sessions:
            print("\n📊 No sessions yet. Start working to see stats!")
            return

        print("\n📊 PRODUCTIVITY STATISTICS")
        print("=" * 50)

        # Today's stats
        today = datetime.now().date()
        today_sessions = [
            s for s in self.completed_sessions
            if datetime.fromisoformat(s['date']).date() == today
        ]

        print(f"Today: {len(today_sessions)} pomodoros")
        print(f"Total: {len(self.completed_sessions)} pomodoros")
        print(f"Total focus time: {len(self.completed_sessions) * 25} minutes")

        # This week
        week_start = datetime.now() - timedelta(days=datetime.now().weekday())
        week_sessions = [
            s for s in self.completed_sessions
            if datetime.fromisoformat(s['date']) >= week_start
        ]
        print(f"This week: {len(week_sessions)} pomodoros")

        # Task breakdown
        if self.tasks:
            print("\n📋 Task Progress:")
            for task in self.tasks:
                status = "✓" if task['done'] else "○"
                print(f"  {status} {task['name']}: {task['completed']}/{task['estimated']}")

    def custom_settings(self):
        """Allow user to customize timer durations."""
        print("\n⚙️ CUSTOM SETTINGS")
        print("=" * 50)
        print(f"Current work duration: {self.work_duration // 60} minutes")
        print(f"Current short break: {self.short_break // 60} minutes")
        print(f"Current long break: {self.long_break // 60} minutes")

        try:
            work = input("\nWork duration in minutes (Enter to keep current): ").strip()
            if work:
                self.work_duration = int(work) * 60

            short = input("Short break in minutes (Enter to keep current): ").strip()
            if short:
                self.short_break = int(short) * 60

            long = input("Long break in minutes (Enter to keep current): ").strip()
            if long:
                self.long_break = int(long) * 60

            print("\n✅ Settings updated!")

        except ValueError:
            print("❌ Invalid input. Settings unchanged.")


def main():
    """Main program loop."""
    timer = PomodoroTimer()

    print("""
    ╔═══════════════════════════════════════╗
    ║      🍅 POMODORO TIMER 🍅            ║
    ║   Stay Focused. Get Things Done.     ║
    ╚═══════════════════════════════════════╝
    """)

    while True:
        print("\n" + "=" * 50)
        print("1. Start Pomodoro")
        print("2. Add Task")
        print("3. View Tasks")
        print("4. View Statistics")
        print("5. Custom Settings")
        print("6. Exit")
        print("=" * 50)

        choice = input("\nChoose option (1-6): ").strip()

        if choice == "1":
            timer.list_tasks()
            if timer.tasks:
                task_num = input("\nSelect task number (or Enter for untracked session): ").strip()
                if task_num:
                    try:
                        timer.start_pomodoro(int(task_num) - 1)
                    except (ValueError, IndexError):
                        print("❌ Invalid task number")
                else:
                    timer.start_pomodoro()
            else:
                timer.start_pomodoro()

        elif choice == "2":
            task_name = input("\nTask name: ").strip()
            if task_name:
                try:
                    est = input("Estimated pomodoros (default 1): ").strip()
                    estimated = int(est) if est else 1
                    timer.add_task(task_name, estimated)
                except ValueError:
                    print("❌ Invalid number")

        elif choice == "3":
            timer.list_tasks()

        elif choice == "4":
            timer.show_statistics()

        elif choice == "5":
            timer.custom_settings()

        elif choice == "6":
            print("\n🍅 Stay productive! Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
