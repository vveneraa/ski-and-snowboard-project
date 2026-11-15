# pt1 first draft
class equipment:
    """
    stores information about one ski or snowboard.

    inputs:
        name - name of the equipment
        equipment_type - ski or snowboard
        price - rental price per day
    """

    def __init__(self, name, equipment_type, price):
        self.name = name
        self.equipment_type = equipment_type
        self.price = price
        self.available = True

    def display(self):
        """displays the equipment information."""
        print(self.name, "-", self.equipment_type, "- $", self.price, "per day")


class customer:
    """
    stores customer information.

    input:
        name - customer's name
    """

    def __init__(self, name):
        self.name = name
        self.equipment = None


class rental_shop:
    """
    manages equipment and customer rentals.
    """

    def __init__(self):
        self.equipment_list = []

    def add_equipment(self, equipment):
        """adds an equipment object to the shop."""
        self.equipment_list.append(equipment)

    def show_equipment(self):
        """displays all equipment and availability."""
        for equipment in self.equipment_list:
            equipment.display()

            if equipment.available:
                print("Available")
            else:
                print("Rented")

    def rent_equipment(self, customer, equipment):
        """
        rents equipment to a customer.

        returns:
            true if successful
            false if unavailable or customer already has a rental
        """
        if equipment.available and customer.equipment is None:
            equipment.available = False
            customer.equipment = equipment
            print("Rental Successful!")
            return True
        else:
            print("Rental Not Available.")
            return False

    def return_equipment(self, customer):
        """
        returns a customer's rented equipment.

        returns:
            true if successful
            false if the customer has no rental
        """
        if customer.equipment is not None:
            customer.equipment.available = True
            customer.equipment = None
            print("Equipment Returned!")
            return True
        else:
            print("No Equipment to Return.")
            return False

# main program
shop = rental_shop()

ski = equipment("Basic Skis", "Ski", 25)
snowboard = equipment("Basic Snowboard", "Snowboard", 30)

shop.add_equipment(ski)
shop.add_equipment(snowboard)

customer = customer("John")

shop.show_equipment()
shop.rent_equipment(customer, ski)
shop.show_equipment()
shop.return_equipment(customer)
shop.show_equipment()