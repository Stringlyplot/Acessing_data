def read_file(file_data):
    with open(file_data, "r") as file:
        data = file.readlines()
        print("HERE >>>>", data)
        return data
user_data = read_file("input.txt")
def data_format(format):
    for x in format:
        
        pass