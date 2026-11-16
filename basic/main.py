my_list = []
old_list = []
running = True

while running == True:
    print()
    print("1. add")
    print("2. remove")
    print("3. show list")
    print("4. undo")
    print("5. exit")
    choice = input("choose: ")

    if choice == "1":
        item = input("item to add: ")
        old_list = my_list.copy()
        my_list.append(item)

    elif choice == "2":
        number = 0
        for item in my_list:
            print(number, item)
            number = number + 1
        index = int(input("index to remove: "))
        if index < len(my_list):
            old_list = my_list.copy()
            my_list.pop(index)
        else:
            print("not a valid index")

    elif choice == "3":
        number = 0
        for item in my_list:
            print(number, item)
            number = number + 1

    elif choice == "4":
        my_list = old_list.copy()

    elif choice == "5":
        running = False

    else:
        print("not an option")