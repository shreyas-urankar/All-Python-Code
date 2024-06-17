# Write a class train which has methods to book a ticket, get status (number of seats) and get fare information of train running under Indian railways.
from random import randint

class Train:
    def __init__(self, trainNo) -> None:
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}.")

    def status(self):
        print(f"Your status for train no: {self.trainNo} is booked.")

    def getFare(self, fro, to):
        fare = randint(222, 5555)
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {fare}")

# Example usage
print("-------------Welcome to Indian Railways.------------------")
t = Train(123)
t.book("Pune Jn.", "Banglore Jn.")
t.status()
t.getFare("Pune Jn.", "Banglore Jn.")
