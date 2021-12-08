# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# RRoot,1.1.2020,Created starter script
# RRoot,1.1.2020,Added pseudo-code
# ELeggett,12.6.2021,Added starter code,
#                    debugged menu option 1
# ELeggett,12.7.2021,Completed assignment code,
#                    debugged menu options 2 and 3
#                    incorporated error handling
# ------------------------------------------------------------------------ #

# Error Handling  -------------------------------------------------------- #

class AlphaError(Exception):
    def __str__(self):
        return ("Invalid entry: only alphabetic characters in Product Name field.")


class NumError(Exception):
    def __str__(self):
        return ("Ivalid entry: only numeric characters in Product Price field.")


class MenuError(Exception):
    def __str__(self):
        return ("Invalid entry: please select a menu option 1-3.")


class GenError(Exception):
    def __str__(self):
        return ("Unspecified error: check your inputs and try again.")


# Data ------------------------------------------------------------------- #

strFileName = 'products.txt'
strFileOpen = open(strFileName, "a")
lstOfProductObjects = []


class Product:
    """Stores information about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price

    changelog:
        RRoot,1.1.2020,Created Class
        ELeggett,12.6.2021,Modified code to complete assignment
    """
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if value.isalpha() == True:
            self.__product_name = value
        else:
            raise AlphaError()

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if value.isnumeric() == True:
            self.__product_price = value
        else:
            raise NumError


# Processing  ------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data_from_file(file_name, list_of_rows): -> (a list of product objects)
        add_data(product_name, product_price, list_of_rows):
        save_data(file_name, list_of_rows):

    changelog:
        RRoot,1.1.2020,Created Class
        ELeggett,12.6.2021,Modified code to complete assignment
    """

    @staticmethod
    def read_data(file_name, list_of_rows):
        file = open(file_name, "r")
        for line in file:
            product_name, product_price = line.split(",")
            row = {"Product": product_name.strip(), "Price": product_price.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data(product_name, product_price, list_of_rows):
        """ Adds inputted data (product, price) to indicated list of dictionary rows

        :param product_name: (string) indicating product to be added:
        :param product_price: (float) indicating product price:
        :param list_of_rows: (list) being populated with data:
        :return: revised (list) of dictionary rows
        """
        row = {"Product": product_name.title(), "Price": product_price}
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def save_data(file_name, list_of_rows):
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Product"] + ", " + row["Price"] + "\n")
        file.close()
        return list_of_rows


# Presentation (Input/Output)  ------------------------------------------- #

class IO:
    """Collects information to process:

    methods:
        output_menu():
        menu_choice():
        input_product():
    changelog:
            RRoot,1.1.2020,Created Class
            ELeggett,12.7.2021,Modified code to complete assignment
    """

    @staticmethod
    def output_menu():
        """Displays a menu of options to the user
        """
        print("""
        MENU OF OPTIONS:\n
        1 - Display Current List
        2 - Add Data to List
        3 - Save List to File & Exit Program
        \n********************
        """)

    @staticmethod
    def menu_choice():
        """Saves user's menu choice for processing

        :return: user's menu choice
        """
        choice = input("Select a menu option [1 to 3]: ")
        return choice

    @staticmethod
    def print_list(list_of_rows):
        """Displays user's list of data for viewing

        :return: current list of data
        """
        print("\nCURRENT LIST OF ITEMS:\n** PRODUCT | PRICE **\n")
        for row in list_of_rows:
            print(row["Product"] + ", $" + row["Price"])
        print("\n********************")

    @staticmethod
    def input_product():
        """Saves user's product and price data for processing

        :return: product and price to add to list
        """
        product_name = input("\nInput an item to catalog: ")
        product_price = input("Input an approximate price: ")
        return product_name, product_price


# Main Body of Script  --------------------------------------------------- #

FileProcessor.read_data(strFileName, lstOfProductObjects)

while (True):
    IO.print_list(lstOfProductObjects)
    IO.output_menu()
    menu_choice = IO.menu_choice()

    if menu_choice == "1":
        IO.print_list(lstOfProductObjects)

    elif menu_choice == "2":
        try:
            (product_name, product_price) = IO.input_product()
            if product_name.isnumeric():
                raise AlphaError()
            elif product_price.isalpha():
                raise NumError()
            else:
                FileProcessor.add_data(product_name, product_price, lstOfProductObjects)
                print("\nData successfully added to list.")
        except:
            raise GenError()

    elif menu_choice == "3":
        try:
            FileProcessor.save_data(strFileName, lstOfProductObjects)
            print("\nData successfully written to file. Exiting program. Goodbye!")
        except:
            raise GenError()
        break

    else:
        raise MenuError()
