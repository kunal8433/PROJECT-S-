import json
import random
import webbrowser
from datetime import datetime

DATA_FILE = "phone_data.json"

def save_phone_details():
    print("\n--- Enter your phone details ---")
    model = input("Phone model : ")
    imei = input("IMEI number : ")
    email = input("Recovery email : ")
    emergency = input("Emergency contact number : ")

    data = {
        "model": model,
        "imei": imei,
        "email": email,
        "emergency_contact": emergency,
        "saved_on": str(datetime.now())
    }

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("\n✅ Phone details saved successfully!")


def show_phone_details():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        print("\n--- Saved Phone Details ---")
        print("Model :", data["model"])
        print("IMEI :", data["imei"])
        print("Email :", data["email"])
        print("Emergency Contact :", data["emergency_contact"])
        print("Saved on :", data["saved_on"])

    except FileNotFoundError:
        print("\n❌ No phone data found. Please save details first.")


def open_find_my_device():
    print("\nOpening Google Find My Device...")
    webbrowser.open("https://www.google.com/android/find")


def live_location_simulation():
    print("\n--- Live Location (Simulation Only) ---")

    # Random location near India (demo purpose)
    latitude = round(random.uniform(20.0, 30.0), 6)
    longitude = round(random.uniform(70.0, 85.0), 6)

    print("Latitude :", latitude)
    print("Longitude:", longitude)

    map_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    print("\nOpening map...")
    webbrowser.open(map_link)


def main_menu():
    while True:
        print("\n==============================")
        print(" Lost Phone Recovery Assistant")
        print("==============================")
        print("1. Save phone details")
        print("2. View saved details")
        print("3. Open Google Find My Device")
        print("4. Live location (simulation)")
        print("5. Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            save_phone_details()

        elif choice == "2":
            show_phone_details()

        elif choice == "3":
            open_find_my_device()

        elif choice == "4":
            live_location_simulation()

        elif choice == "5":
            print("\nGood bye Kunal 👋")
            break

        else:
            print("\n❌ Invalid choice")


if __name__ == "__main__":
    main_menu()
