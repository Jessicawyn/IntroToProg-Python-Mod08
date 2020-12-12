# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# jcarnes,12.06.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
menu_option = None
product_to_add = None
price_to_add = None


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        to_string: returns the product_name and product_price as string separated by comma
        __str__: returns the product_name and product_price as string separated by comma
        __doc__: returns the class information of the Product Class
        is_float: returns a True/False for if the value can be converted to a float
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        jcarnes,12.6.2020,Modified code to complete assignment 8
    """
    # DONE: Add Code to the Product class
    #

    # Constructor
    # -- Constructor --
    def __init__(self, product_name, product_price):
        """Sets Product Name and Product Price for new object"""
        # Attributes
        try:
            self.__product_name = product_name
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception('Issue setting initial values: \n\n' + str(e))

    # -- Properties --
    # product_name
    @property  # DON'T USE NAME for this directive!
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() is False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # product_price
    @property  # DON'T USE NAME for this directive!
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price)  # Title case

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        if Product.is_float(value):
            self.__product_price = value
        else:
            raise Exception("Value must be a number")

    @staticmethod
    def is_float(value):
        """Tests to see if the value entered is convertible to a float
        :param value: (str) from user input
        :return: Boolean True or False"""
        try:
            float(value)
            return True
        except ValueError:
            return False

    # -- Methods --
    def to_string(self):
        """Returns the object as a string"""
        return self.product_name + "," + str(self.product_price)

    def __str__(self):
        """Returns the object as a string"""
        return self.product_name + "," + str(self.product_price)

    def __doc__(self):
        """Information on the Product class"""
        return 'This class holds product and price data'


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        jcarnes,12.06.2020,Modified code to complete assignment 8
    """
    # DONE: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """This function reads data from a text file and adds the contents to a list of Product objects.
        If the file doesn't exist then the file is created and the list is empty.
        :param file_name: text file containing products and prices
        :return: list_of_rows containing Product objects
        """
        list_of_rows = []
        try:
            f = open(file_name, 'r')
            for line in f:
                product, price = line.split(",")
                list_of_rows.append(Product(product, price.strip()))
        except:
            f = open(file_name, 'w')
        f.close()
        return list_of_rows

    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """This function takes a list containing Product objects and writes the list to a text file

        :param file_name: text file to write to
        :param list_of_rows: list containing Product objects
        :return: str success status
        """
        f = open(file_name, 'w')
        for obj in list_of_rows:
            f.write(obj.product_name + ',' + obj.product_price + '\n')
        f.close()
        return 'Success'
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    # DONE: Add docstring
    """Display information to a user and receive user input:

    methods:
        print_menu()
        input_menu_choic()
        display_current_data(list_of_rows): -> a list of Product objects
        get_product_data()

    changelog: (When,Who,What)
        jcarnes,12.06.2020,Created IO Class
    """

    # DONE: Add code to show menu to user
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Display Current Data
        2) Add Product to List
        3) Save Data to File & Exit Program      
        ''')
        print()  # Add an extra line for looks

    # DONE: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string containing the user's choice
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # DONE: Add code to show the current data from the file to user
    @staticmethod
    def display_current_data(list_of_rows):
        """ Prints Product objects in the list to the user
        :param list_of_rows: list containing Product objects
        """
        if list_of_rows == []:
            print('\nThe product list is currently empty!')
        else:
            print('\nCurrent Products and Prices in List:')
            for obj in list_of_rows:
                print(obj.product_name + ', ' + obj.product_price)

    # DONE: Add code to get product data from user
    @staticmethod
    def get_product_data():
        """ Get product and price information from user then create new Product object
        :param: None
        :return: product object"""
        try:
            item = input('Please enter a product: ').strip()
            price = input('Please enter a price: ').strip()
            product_obj = Product(item, price)
        except Exception as e:
            print(e)

        return product_obj
    # Presentation (Input/Output)  -------------------------------------------- #

    # Main Body of Script  ---------------------------------------------------- #
    # DONE: Add Data Code to the Main body
    # Load data from file into a list of product objects when script starts
    # Show user a menu of options
    # Get user's menu option choice
        # Show user current data in the list of product objects
        # Let user add data to the list of product objects
        # let user save current data to file and exit program

    # Main Body of Script  ---------------------------------------------------- #


try:
    # Load data from file into a list of product objects
    list_of_objects = FileProcessor.read_data_from_file(strFileName)

    # Show user a menu of options
    # Get user's menu option choice
    while menu_option != '3':
        IO.print_menu()
        menu_option = IO.input_menu_choice()
        if menu_option == '1':  # Display current data
            IO.display_current_data(list_of_objects)
        elif menu_option == '2':  # Add product to list
            list_of_objects.append(IO.get_product_data())
        elif menu_option == '3':
            FileProcessor.write_data_to_file(strFileName, list_of_objects)
            break
        else:
            continue
except Exception as e:
    print(e)
