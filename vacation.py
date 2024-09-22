def vacation_plan():
    # Define vacation activity options
    activities = [
        "1. Relaxing on the beach",
        "2. Exploring historical sites",
        "3. Adventure sports",
        "4. Visiting museums and art galleries",
        "5. Hiking in nature",
        "6. Enjoying city nightlife"
    ]
    
    # Define destination options
    destinations = [
        "1. Hawaii",
        "2. Rome",
        "3. New Zealand",
        "4. Paris",
        "5. Swiss Alps",
        "6. New York City"
    ]
    
    # Display activity options to the user
    print("Choose an activity for your vacation:")
    for activity in activities:
        print(activity)
    
    # Get user's choice for activity
    activity_choice = int(input("Enter the number corresponding to your choice of activity: "))
    
    # Display destination options to the user
    print("\nChoose a destination for your vacation:")
    for destination in destinations:
        print(destination)
    
    # Get user's choice for destination
    destination_choice = int(input("Enter the number corresponding to your choice of destination: "))
    
    # Validate user input
    if 1 <= activity_choice <= 6 and 1 <= destination_choice <= 6:
        # Display the user's vacation plan
        chosen_activity = activities[activity_choice - 1][3:]  # Remove number and dot
        chosen_destination = destinations[destination_choice - 1][3:]  # Remove number and dot
        print(f"\nYour vacation plan is to go to {chosen_destination} and enjoy {chosen_activity} with your family!")
    else:
        print("Invalid choice! Please run the program again and choose valid options.")

# Call the function to execute the plan
vacation_plan()
