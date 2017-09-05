## Python Program for the board game Flutter ##
from math import floor

def is_red(colour_text):
    return colour_text in ["RED", "R"]

def is_blue(colour_text):
    return colour_text in ["BLUE", "BLU"]

def is_green(colour_text):
    return colour_text in ["GREEN", "GRE", "G"]

def is_yellow(colour_text):
    return colour_text in ["YELLOW", "YEL", "Y"]

def is_white(colour_text):
    return colour_text in ["WHITE", "WHI", "W"]

def is_black(colour_text):
    return colour_text in ["BLACK", "BLA", "BLK"]

class FlutterManager:

    share_price_red = 0
    share_price_blue = 0
    share_price_green = 0
    share_price_yellow = 0
    share_price_white = 0
    share_price_black = 0

    def initialise_shares(self):
        self.share_price_red = 100
        self.share_price_blue = 100
        self.share_price_green = 100
        self.share_price_yellow = 100
        self.share_price_white = 100
        self.share_price_black = 100

    def print_shares(self):
        print("===============================")
        print("Current Share Prices: ")
        print("Red", self.share_price_red)
        print("Blue", self.share_price_blue)
        print("Green", self.share_price_green)
        print("Yellow", self.share_price_yellow)
        print("White", self.share_price_white)
        print("Black", self.share_price_black)
        print("===============================")


    def print_shares_and_change(self, total_money, share_price, num_shares):
        change = total_money - (num_shares * share_price)
        print("Shares:", num_shares, "Change:", change)

    def share_price_for_colour(self, colour_choice):
        colour_choice = colour_choice.upper()

        if is_red(colour_choice):
            return self.share_price_red

        elif is_blue(colour_choice):
            return self.share_price_blue

        elif is_green(colour_choice):
            return self.share_price_green

        elif is_yellow(colour_choice):
            return self.share_price_yellow

        elif is_white(colour_choice):
            return self.share_price_white

        elif is_black(colour_choice):
            return self.share_price_black

        else:
            print("Colour not Recognised")
            return None

    def purchase_options_by_colour(self, total_money, colour_choice):
        share_price = self.share_price_for_colour(colour_choice)
        if share_price is None:
            return
        self.purchase_options(total_money, share_price)

    def purchase_options(self, total_money, share_price):
        max_shares = int(floor(total_money / share_price))
        change = total_money % share_price

        print("Purchasing Options:")

        for num_shares in range(1, max_shares + 1):
            self.print_shares_and_change(
                total_money,
                share_price,
                num_shares
            )

    def new_total_money_with_shares(self, total_money, colour_choice, share_quantity):
        share_price = self.share_price_for_colour(colour_choice)
        if share_price is None:
            return

        print("")
        print("*** £", share_quantity * share_price, "worth of shares sold. ***")
        print("")
        total_money = total_money + (share_quantity * share_price)

        return total_money

    def update_share_price(self, share_price, colour_choice):
        colour_choice = colour_choice.upper()

        if is_red(colour_choice):
            self.share_price_red = share_price

        elif is_blue(colour_choice):
            self.share_price_blue = share_price

        elif is_green(colour_choice):
            self.share_price_green = share_price

        elif is_yellow(colour_choice):
            self.share_price_yellow = share_price

        elif is_white(colour_choice):
            self.share_price_white = share_price

        elif is_black(colour_choice):
            self.share_price_black = share_price

        else:
            print("Colour not Recognised")
            return None


def validate_input(input):
    number_count = 0

    for letter in input:
        if letter.isdigit() == True:
            number_count = number_count + 1

    if number_count == len(input) and len(input) > 0:
        return int(input)

    else:
        return None


def read_integer(message):
    while True: #Loops Forever
        validated_input = validate_input(input(message))
        if validated_input is not None:
            break # Leaves Loop
        else:
            print("You muppet! Hook me up with the good s#!7")

    return validated_input

if __name__ == '__main__':
    flutter_manager = FlutterManager()
    flutter_manager.initialise_shares()
    flutter_manager.print_shares()

    quit = False
    while not quit:
        print("")
        print("----")
        print("Menu")
        print("----")
        print("1. Purchasing Options")
        print("2. Purchasing Options with shares")
        print("3. Initialise Shares")
        print("4. Print Shares")
        print("5. Update Share Prices")
        print("Q. Quit")

        choice = input()

        if choice == "1":
            total_money = read_integer(message="Your Money: ")
            colour_choice = input("Colour you want to buy: ")
            colour_choice = colour_choice.upper()
            flutter_manager.purchase_options_by_colour(
                total_money,
                colour_choice
            )


        elif choice == "q":

            quit = True

        elif choice == "3": # Initialise Shares
            flutter_manager.initialise_shares()
            flutter_manager.print_shares()

        elif choice == "4": # Print Shares
            flutter_manager.print_shares()

        elif choice == "2": # Purchasing Options with Shares
            # Ask for their total money
            total_money = read_integer(message="Your Money: ")
            # Ask for the number of shares they have
            share_quantity = read_integer(message="No. of Shares you want to sell: ")
            # Ask for the type of share they have
            colour_choice = input("Colour of shares you want to sell: ")
            # Ask for the type of shares they want to buy
            desired_colour_choice = input("Colour of Shares you want to buy: ")

            print("")
            print("-Stage 1-")
            print("Money: ", total_money)
            print("Shares being sold: ", colour_choice)
            print("Amount being sold: ", share_quantity)
            print("Shares being bought: ", desired_colour_choice)
            print("")

            # Compute the total money that their money and shares are worth
            total_money = flutter_manager.new_total_money_with_shares(
                total_money, colour_choice, share_quantity,
            )

            #print("-Stage 1-")
            #print("Money: ", total_money)
            #print("Share Colour: ", colour_choice)
            #print("Share Quantity: ", share_quantity)
            #print("Desired Shares: ", desired_colour_choice)

            # Print their options
            flutter_manager.purchase_options_by_colour(
                total_money, desired_colour_choice
            )

            print("")
            print("-Stage 2: Selling Shares-")
            print("New Money: ", total_money)
            print("Shares being sold: ", colour_choice)
            print("Amount being sold: ", share_quantity)
            print("Shares being bought: ", desired_colour_choice)
            print("")

        elif choice == "5":
            colour_choice = input("Share Colour you want to update: ")
            share_price = read_integer(message = "New Price: ")
            flutter_manager.update_share_price(share_price, colour_choice)

            flutter_manager.print_shares()