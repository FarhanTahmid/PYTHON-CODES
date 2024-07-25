#Disaster Information
def get_disaster_data(location):
    disaster_data = {
                        "Dhaka" : {"Earthquake": {"Magnitude": 5.5, "Date": "14-08-2023", "Location": "Dhaka" }},
                        "Sunamganj" : {"Flood": {"Magnitude": "Severe Flash Flood" , "Date": "20-06-2022", "Location": "Sunamganj" }},
                        "Chittagong": {"Cyclone": {"Magnitude": "Category-5", "Date": "14-05-2023", "Location": "Chittsgong"}}
    }

    return disaster_data.get (location, "None Found")

#Safety Tips
def get_safety_tips(disaster_type):
    safety_tips = { "Earthquake": ["Cover your head and neck with your arms", "If a sturdy table or desk is nearby, crawl underneath it for shelter","If no shelter is nearby, crawl next to an interior wall (away from windows)"],
                    "Flood" : ["Monitor weather updates and evacuation routes", " Never walk or drive through flooded areas","Prepare essentials and have an evacuation plan"],
                    "Cyclone" : ["Reinforce doors, windows, and outdoor items", "Know shelters, follow orders, and relocate if needed", "Pack water, food, first aid, and important documents" ]

    }

    return safety_tips.get(disaster_type, "None Found.")

#Command-Line
def main():
    while True:
        print("Disaster Management System")
        print("1. Retrieve Disaster Data for a Location")
        print("2. Get Safety Tips for a Disaster Type")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            location = input("Enter the location (city name): ")
            disaster_info = get_disaster_data(location)
            print(disaster_info)

        elif choice == "2":
            disaster_type = input("Enter the disaster type: ")
            tips = get_safety_tips(disaster_type)
            print("\nSafety Tips:")
            for tip in tips:
                print("- " + tip)

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
