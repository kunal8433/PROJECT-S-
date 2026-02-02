import json
import webbrowser
from datetime import datetime

DATA_FILE = "devices.json"


def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_device():
    print("\n--- Add Device (My / Mother / Family) ---")
    owner = input("Owner name (Me / Mother etc): ")
    model = input("Phone model: ")
    imei = input("IMEI: ")

    data = load_data()

    data.append({
        "owner": owner,
        "model": model,
        "imei": imei,
        "saved_on": str(datetime.now())
    })

    save_data(data)
    print("✅ Device added successfully")


def show_devices():
    data = load_data()

    if not data:
        print("❌ No devices saved")
        return

    print("\n--- Saved Devices ---")
    for i, d in enumerate(data, start=1):
        print(f"{i}. {d['owner']} | {d['model']} | {d['imei']}")


def find_device_official():
    print("\nOpening Google Find My Device (official & legal)...")
    webbrowser.open("https://www.google.com/android/find")


def main():
    while True:
        print("\n==============================")
        print(" Lost Phone Recovery Assistant")
        print("==============================")
        print("1. Add device (Me / Mother)")
        print("2. Show saved devices")
        print("3. Find device (official Google tool)")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_device()
        elif ch == "2":
            show_devices()
        elif ch == "3":
            find_device_official()
        elif ch == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
