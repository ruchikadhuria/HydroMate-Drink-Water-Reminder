import time
from plyer import notification

def water_reminder(interval_minutes, max_reminders):
    count = 0
    print("💧 Water Reminder Started!")
    
    try:
        while count < max_reminders:
            notification.notify(
                title="💧 Hydration Reminder",
                message="It's time to drink some water and stay hydrated!",
                timeout=10
            )
            count += 1
            print(f"Reminder {count} sent.")
            time.sleep(interval_minutes * 60)

        print("✅ All reminders completed for today.")
    except KeyboardInterrupt:
        print("\n❌ Water reminder stopped by user.")

if __name__ == "__main__":
    interval = int(input("Enter reminder interval (in minutes): "))
    reminders = int(input("Enter number of reminders: "))
    water_reminder(interval, reminders)
