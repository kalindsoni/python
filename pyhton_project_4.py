data = ()
dataset = []

def option():
    print("\nSelect an option:")
    for item in data:
        print(item)

def input_data():

    size = int(input("enter size of array: "))
    for i in range(size):
        value = int(input(f"Enter data value {i + 1}: "))
        dataset.append(value)

    for j in dataset:
        print(j, end=" ")
    print("\nData input complete.\n")

def display_data_summary():
        print("data summary: \n")

        sum_value()
        minimum_value()
        maximum_value()
        avg_value()

def minimum_value():
    j = dataset[0]
    for i in dataset:
        if i < j:
            j = i

    print(f"- minimum value is: {j}")
    return j

def maximum_value():
    j = dataset[0]
    for i in dataset:
        if i > j:
            j = i

    print(f"- maximum value: {j}")
    return j

def sum_value():
    k = 0
    for i in dataset:
        k += 1
    print(f"- total element: {k}")
    return k

def avg_value():
    sum = 0
    for i in dataset:
        sum += i

    j = 0
    for i in dataset:
        j += 1

    avg = sum / j
    print(f"- average value: {avg}")
    return avg


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def filter_data():
    if len(dataset) == 0:
        print("enter data first! ")
        return
    thershould = int(input("enter your thershould valueto filter out data above: "))
    filteredata = list(filter(lambda x:x >= thershould, dataset))
    print(F"filtered data(values >= {thershould}): ")
    print(*filteredata, sep=",")

def short_data():
    if len(dataset) == 0:
        print("please enter data first!")
        return
    print("choising sorting an option: ")
    print("\n1. ascending")
    print("\n2. descending")

    choice = int(input("enter your choice: "))
    if choice == 1:
        dataset.sort()
        print("\n sorted data in ascending order: ")
        print(*dataset, sep=",")

    elif choice == 2:
        dataset.sort(reverse = True)
        print("\nsorted dataset in desending order.")
        print(*dataset, sep=",")

def display_statistics():
    minimum = dataset[0]
    maximum = dataset[0]
    total = 0
    count = 0

    for i in dataset:
        if i < minimum:
            minimum = i

        if i > maximum:
            maximum = i

        total += i
        count += i

        average = total / count

        return maximum, minimum, total, average

while True:

        print("1. input data"),
        print("2. display data summary (built-in function)"),
        print("3. calculate factorial (recursion)"),
        print("4. filter data by threshold (lambda function)"),
        print("5. sort data "),
        print("6. display dataset statistics (return multiple)"),
        print("7. exit program")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                input_data()

            case 2:
                display_data_summary()

            case 3:
                num = int(input("enter your number: "))
                result = factorial(num)
                print(f"factorial of {num} is = {result}")

            case 4:
                filter_data()

            case 5:
                short_data()

            case 6:
                minimum, maximum, total, average = display_statistics()

                print("\n dataset statistics:")
                print(f"-minimum value: {minimum}")
                print(f"-maximum value: {maximum}")
                print(f"-sum of all value: {total}")
                print(f"-average value : {average}")

            case 7:
                print("Thankyou For using the data Analyzer and Tranformer program. goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")