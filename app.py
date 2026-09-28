from flask import Flask, render_template
from vehicles.vehicle import Vehicle

app = Flask(__name__)

vehicles = [
    Vehicle("MAW001", "Car 01", "Lagos", 6.5244, 3.3792, 65, "Moving"),
    Vehicle("MAW002", "Car 02", "Abuja", 9.0765, 7.3986, 0, "Parked"),
    Vehicle("MAW003", "Car 03", "Benue", 7.3369, 9.0031, 72, "Moving"),
    Vehicle("MAW004", "Car 04", "Kaduna", 10.5105, 7.4165, 0, "Offline"),
    Vehicle("MAW005", "Car 05", "Kano", 12.0022, 8.5920, 48, "Moving"),
    Vehicle("MAW006", "Car 06", "Lagos", 6.5244, 3.3792, 55, "Moving"),
    Vehicle("MAW007", "Car 07", "Abuja", 9.0765, 7.3986, 0, "Parked")
]
@app.route("/")
def home():
    return render_template("index.html", vehicles=vehicles)

if __name__ == "__main__":
    app.run(debug=True)