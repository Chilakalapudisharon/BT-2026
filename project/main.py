from transport_manager import TransportManager
import utils

def main():
    manager = TransportManager()

    # Seed data for demonstration
    manager.register_bus("B01", 40, "BUS-101")
    manager.register_driver("D01", "John Doe", "DL-99482")
    manager.create_route("R01", "Downtown", "ACE Campus", 12.5)

    while True:
        print("\n=== ACE TRANSPORTATION PORTAL ===")
        print("1. Register a Bus")
        print("2. Register a Driver")
        print("3. Create a Route")
        print("4. Register a Student & Assign Route")
        print("5. Assign Driver to Vehicle")
        print("6. View System Summary")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            v_id = input("Enter Vehicle ID: ")
            cap = utils.get_positive_int("Enter Capacity: ")
            b_num = input("Enter Bus Number: ")
            success, msg = manager.register_bus(v_id, cap, b_num)
            print(msg)

        elif choice == "2":
            d_id = input("Enter Driver ID: ")
            name = input("Enter Driver Name: ")
            lic = input("Enter License Number: ")
            success, msg = manager.register_driver(d_id, name, lic)
            print(msg)

        elif choice == "3":
            r_id = input("Enter Route ID: ")
            start = input("Enter Starting Point: ")
            end = input("Enter End Destination: ")
            dist = utils.get_positive_float("Enter Distance (km): ")
            success, msg = manager.create_route(r_id, start, end, dist)
            print(msg)

        elif choice == "4":
            s_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            stop = input("Enter Pickup Stop Name: ")
            manager.register_student(s_id, name, stop)
            
            print("\nAvailable Routes:")
            for r in manager.routes.values(): print(r)
            r_id = input("Enter Route ID to assign: ")
            success, msg = manager.assign_student_to_route(s_id, r_id)
            print(msg)

        elif choice == "5":
            d_id = input("Enter Driver ID: ")
            v_id = input("Enter Vehicle ID: ")
            success, msg = manager.assign_driver_to_vehicle(d_id, v_id)
            print(msg)

        elif choice == "6":
            print("\n--- SYSTEM SUMMARY ---")
            print("\n[Vehicles]")
            for v in manager.vehicles.values(): print(v)
            print("\n[Drivers]")
            for d in manager.drivers.values(): print(d)
            print("\n[Routes]")
            for r in manager.routes.values(): print(r)
            print("\n[Students]")
            for s in manager.students.values(): print(s)

        elif choice == "7":
            print("Exiting ACE Transportation Portal. Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

        input("\nPress Enter to return to menu...")
        utils.clear_screen()

if __name__ == "__main__":
    main()