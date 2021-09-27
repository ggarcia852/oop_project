class ParkingGarage:
    cars_in_garage = []
    unpaid_tickets = []
    available_spaces = 10
    
    def __init__(self, available_spaces, cars_in_garage, unpaid_ticekts):
        self.available_spaces = available_spaces
        self.cars_in_garage = cars_in_garage
        self.unpaid_tickets = unpaid_ticekts
        
    def take_ticket(self): 
        if self.available_spaces > 0:
            car = input("Please enter your license plate number: ")
            self.cars_in_garage.append(car)
            self.unpaid_tickets.append(car)
            self.available_spaces -= 1
        else:
            print("There are no spaces available")    
        
    
    def pay_ticket(self):
        selection = input("Please enter your license plate number pay for your ticket ").lower()
        if selection in self.unpaid_tickets:
            payment = input("Please enter 'pay' to pay for your ticket ").lower()
            if payment == 'pay': 
                self.unpaid_tickets.remove(selection)
                print("You have paid for your ticket and may now exit the garage")
            else:
                print("Pleae pay for your ticket by entering 'pay'")
        else:
            print("That does not match any cars in the garage, please try again.")

    def view_cars(self):
        for car in self.cars_in_garage:
            print(car)
            
    def exit_garage(self):
        exit = input("Please enter your license plate number: ")
        if exit not in self.cars_in_garage:
            print("That is not a valid license plate number, please try again.")  
        elif exit in self.unpaid_tickets:
            print("Please pay for your ticket before exiting")
        elif exit in self.cars_in_garage and exit not in self.unpaid_tickets:
            print("Thanks for parking with us, have a nice day!")
            self.available_spaces += 1
            self.cars_in_garage.remove(exit)
        
    
        
        
    
def run():
    
    my_car = ParkingGarage
    
    while True:
        
        action = input("What would you like to do? \n Enter 'take' to take a ticket \n Enter 'pay' to pay for your ticket \n Enter 'view' to see cars in garage \n Enter 'exit' to exit the garage ").lower()
        if action == "take":
            my_car.take_ticket(my_car)

        elif action == "pay":
            my_car.pay_ticket(my_car)

        elif action == "view":
            my_car.view_cars(my_car)
            
        elif action == "exit":
            my_car.exit_garage(my_car)

        else:
            print("That is not a valid resonse, please try again.")

        
run()