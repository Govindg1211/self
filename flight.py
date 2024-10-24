import random

# Class to represent a Flight
class Flight:
    def __init__(self, from_location, to_location, timing):
        self.from_location = from_location  # Departure location
        self.to_location = to_location        # Destination location
        self.timing = timing                  # Preferred timing
        self.flight_number = self.generate_flight_number()  # Generate a unique flight number

    def generate_flight_number(self):
        """Generate a unique flight number."""
        return f"FL{random.randint(1000, 9999)}"  # Flight number format: FLXXXX

    def display_flight_details(self):
        """Display the flight details."""
        return {
            "From": self.from_location,
            "To": self.to_location,
            "Timing": self.timing,
            "Flight Number": self.flight_number
        }

# Class to represent the Airport Management System
class AirportManagementSystem:
    def __init__(self):
        self.flights = []  # List to store flights

    def book_flight(self):
        """Method to book a flight based on user input."""
        print("\n--- Book a Flight ---")
        
        # Ask user for travel details
        from_location = input("Where would you like to fly from? ")
        to_location = input("Where would you like to go? ")
        timing = input("What timing would suit you? ")

        # Create a new flight instance
        new_flight = Flight(from_location, to_location, timing)
        
        # Store the flight in the list
        self.flights.append(new_flight)
        
        # Display flight details
        print("\nFlight booked successfully!")
        flight_details = new_flight.display_flight_details()
        for key, value in flight_details.items():
            print(f"{key}: {value}")

    def view_flights(self):
        """Method to view all booked flights."""
        print("\n--- View All Flights ---")
        
        if not self.flights:
            print("No flights booked yet.")
            return
        
        for index, flight in enumerate(self.flights):
            print(f"\nFlight {index + 1}:")
            details = flight.display_flight_details()
            for key, value in details.items():
                print(f"{key}: {value}")

    def run(self):
        """Main loop to run the airport management system."""
        while True:
            print("\n--- Airport Management System Menu ---")
            print("1. Book a Flight")
            print("2. View All Flights")
            print("3. Exit")

            choice = input("Please choose an option (1-3): ")

            if choice == '1':
                self.book_flight()
            elif choice == '2':
                self.view_flights()
            elif choice == '3':
                print("Thank you for using the Airport Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Main execution
if __name__ == "__main__":
    airport_system = AirportManagementSystem()  # Create an instance of the Airport Management System
    airport_system.run()                        # Start the system