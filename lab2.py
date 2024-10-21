
def main():
    print("ET0735 (devOps for AIoT) - lab 2 - Introduction to python")
    display_main_menu()
    num_list=get_user_input()

def display_main_menu():
        print("Enter some numbers separated by commas: \n")

def get_user_input():

    str_list=input("enter value:")
    print("user_input ")
    split_list= str_list.split(",")
    fsplit_list = [float(value) for value in split_list]
    print(fsplit_list)
    return fsplit_list


def calc_average():
    print("calc_average")
    return 0.0

def find_min_max():
    print("code here")
    return [0.0,0.0]

def sort_temperature():
        print("code here")
        return []

def calc_median_temperature():
        print("code here")
        return 0.0

if __name__ == "__main__":
    main()
        