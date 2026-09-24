from vehicles.vehicle import Vehicle

print("Mo Auto Watch")
print("Vehicle Monitoring System")

car1 = Vehicle("MAW001", "Car 01", "Lagos", 6.5244, 3.3792, 65, "Moving")
car2 = Vehicle("MAW002", "Car 02", "Abuja", 9.0765, 7.3986, 0, "Parked")
car3 = Vehicle("MAW003", "Car 03", "Benue", 7.3369, 9.0031, 72, "Moving")
car4 = Vehicle("MAW004", "Car 04", "Kaduna", 10.5105, 7.4165, 0, "Offline")
car5 = Vehicle("MAW005", "Car 05", "Kano", 12.0022, 8.5920, 48, "Moving")
car6 = Vehicle("MAW006", "Car 06", "Lagos", 6.5244, 3.3792, 55, "Moving")
car7 = Vehicle("MAW007", "Car 07", "Abuja", 9.0765, 7.3986, 0, "Parked") 

vehicles = [
    Vehicle("MAW001", "Car 01", "Lagos", 6.5244, 3.3792, 65, "Moving"),
    Vehicle("MAW002", "Car 02", "Abuja", 9.0765, 7.3986, 0, "Parked"),
    Vehicle("MAW003", "Car 03", "Benue", 7.3369, 9.0031, 72, "Moving"),
    Vehicle("MAW004", "Car 04", "Kaduna", 10.5105, 7.4165, 0, "Offline"),
    Vehicle("MAW005", "Car 05", "Kano", 12.0022, 8.5920, 48, "Moving"),
    Vehicle("MAW006", "Car 06", "Lagos", 6.5244, 3.3792, 55, "Moving"),
    Vehicle("MAW007", "Car 07", "Abuja", 9.0765, 7.3986, 0, "Parked")
]

for car in vehicles:
    print(
        f"{car.vehicle_id} | {car.name} | "
        f"{car.location} | {car.latitude}, {car.longitude} | "
        f"{car.speed} km/h | {car.status}"
    )