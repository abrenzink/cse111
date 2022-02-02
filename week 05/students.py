import csv

def main():

    I_NUM_INDEX = 0
    STUDENT_NAME_INDEX = 1
    
    number_keys = read_dict("students.csv", I_NUM_INDEX)
    name_keys = read_dict("students.csv", STUDENT_NAME_INDEX)

    student_dict = dict(zip(number_keys, name_keys))
  
    i_num = input("Enter the I-number: ")

    if i_num in student_dict:
        name = student_dict[i_num]

        print(name)

    else:
        print("No such student")

def read_dict(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)


        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary


if __name__ == "__main__":
    main()