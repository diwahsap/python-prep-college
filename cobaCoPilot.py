# program to calculate days between two dates in the format dd/mm/yyyy
def main():
    print("This program calculates the number of days between two dates.")
    print()
    # get the start and end dates from the user
    start_date = input("Enter the starting date (dd/mm/yyyy): ")
    end_date = input("Enter the ending date (dd/mm/yyyy): ")
    # convert the dates to numbers
    start_date = start_date.split("/")
    end_date = end_date.split("/")
    start_date = [int(start_date[0]), int(start_date[1]), int(start_date[2])]
    end_date = [int(end_date[0]), int(end_date[1]), int(end_date[2])]
    # calculate the number of days between the dates
    days = (end_date[2] - start_date[2]) * 365
    days += (end_date[1] - start_date[1]) * 30
    days += (end_date[0] - start_date[0])
    # display the result
    print("The number of days between the dates is", days)
main()