# W.I.P.
def add_member():
    global mem_list
    name = str(input("Enter the name of the member: "))
    mem_number = 0
    for x in mem_list:
        if (name == x[1]):
            print(name, "is already a member")
            return
        else:
            if (x[0] > mem_number):
                mem_number = x[0]
    mem_number += 1
    new_mem = [ mem_number, name ]
    mem_list.append(new_mem)
    #print(mem_list)

def remove_member():
    global mem_list
    global checkout_list
    name = str(input("Enter the name of the member: "))
    mem_num = 0
    for x in mem_list:
        if (name == x[1]):
            mem_num = x[0]
    if (mem_num == 0):
        print(name, "is not a member!")
        return
    has_outstanding_checkout = False
    for x in checkout_list:
        if (mem_num == x[0]):
            has_outstanding_checkout = True
            break
    if (has_outstanding_checkout):
        print("Member cannot be removed while he has outstanding checkouts")
    else:
        for x in mem_list:
            if (mem_num == x[0]):
                mem_list.remove(x)
                break
    print(mem_list)
    
def query_member():
    global mem_list
    global book_list
    global checkout_list
    name = str(input("Enter the name of the member: "))
    mem_num = 0
    for x in mem_list:
        if (name == x[1]):
            mem_num = x[0]
    if (mem_num == 0):
        print(name, "is not a member!")
    else:
        count = 0
        for x in checkout_list:
            if (mem_num == x[0]):
                for y in book_list:
                    if (x[1] == y[0]):
                        print(name, "has checked out", y[1])
                count += 1
        print(name, "has a total of", count, "books checked out")

def add_book():
    global book_list
    name = str(input("Enter the name of the book: "))
    book_number = 0
    for x in book_list:
        if (name == x[1]):
            x[2] += 1
            return
        else:
            if (x[0] > book_number):
                book_number = x[0]
    book_number += 1
    book_copies = 1
    new_book = [book_number, name, book_copies]
    book_list.append(new_book)
    #print(book_list)
    
def remove_book():
    global book_list
    global checkout_list
    name = str(input("Enter the name of the book: "))
    book_num = 0
    for x in book_list:
        if (name == x[1]):
            book_num = x[0]
            library_copies = x[2]
    if (book_num == 0):
        print(name, "is not in the catalog!")
        return
    for x in checkout_list:
        if (book_num == x[1]):
            library_copies -= 1
    if (library_copies <= 0):
        print("Library has no copy to delete.  Please return a copy first.")
    else:
        for x in book_list:
            if (book_num == x[0]):
                if (x[2] > 1):
                    x[2] -= 1
                else:
                    book_list.remove(x)
                break
    print(book_list)

def query_book():
    global mem_list
    global book_list
    global checkout_list
    name = str(input("Enter the name of the book: "))
    book_num = 0
    for x in book_list:
        if (name == x[1]):
            book_num = x[0]
            book_copies = x[2]
    if (book_num == 0):
        print(name, "is not in the catalog!")
    else:
        count = 0
        for x in checkout_list:
            if (book_num == x[1]):
                for y in mem_list:
                    if (x[0] == y[0]):
                        print(y[1], "has checked out", name)
        print("The library catalog has a total of", book_copies, "copy of", name)
    
    
def checkout_a_book():
    global mem_list
    global book_list
    global checkout_list
    mem_name = str(input("Enter the name of the member: "))
    mem_num = 0
    for x in mem_list:
        if (mem_name == x[1]):
            mem_num = int(x[0])
    if (mem_num == 0):
        print(mem_name, "is not a member!")
        return
    book_name = str(input("Enter the name of the book: "))
    book_num = 0
    for x in book_list:
        if (book_name == x[1]):
            book_num = int(x[0])
            book_copies = int(x[2])
    if (book_num == 0):
        print(book_name, "is not in the library!")
        return
    count = 0
    for x in checkout_list:
        if (book_num == x[1]):
            count += 1
    if (count == book_copies):
        print("Sorry all copies of", book_name, "have been checked out")
    else:
        co_list = [mem_num, book_num]
        checkout_list.append(co_list)
    #print(checkout_list)
    #print(mem_num, book_num, book_copies)
    
def return_a_book():
    global mem_list
    global book_list
    global checkout_list
    mem_name = str(input("Enter the name of the member: "))
    mem_num = 0
    for x in mem_list:
        if (mem_name == x[1]):
            mem_num = int(x[0])
    if (mem_num == 0):
        print(mem_name, "is not a member!")
        return
    book_name = str(input("Enter the name of the book: "))
    book_num = 0
    for x in book_list:
        if (book_name == x[1]):
            book_num = int(x[0])
    if (book_num == 0):
        print(book_name, "is not in the library!")
        return
    for x in checkout_list:
        if (mem_num == x[0] and book_num == x[1]):
            checkout_list.remove(x)
            break
    #print(checkout_list)
    
    
def read_mem_list():
    global mem_list
    memfile = open("members.txt", "a")
    memfile.close()
    memfile = open("members.txt", "r")
    for line in memfile:
        line = line.strip()
        line = line.split(',')
        mem_number = int(line[0])
        mem_name = line[1]
        new_mem = [mem_number, mem_name]
        mem_list.append(new_mem)
    memfile.close()
    #print("At end of read:", mem_list, len(mem_list))
    
def read_book_list():
    global book_list
    bookfile = open("books.txt", "a")
    bookfile.close()
    bookfile = open("books.txt", "r")
    for line in bookfile:
        line = line.strip()
        line = line.split(',')
        book_number = int(line[0])
        book_name = line[1]
        book_copies = int(line[2])
        new_mem = [book_number, book_name, book_copies]
        book_list.append(new_mem)
    bookfile.close()
    #print("At end of read:", book_list, len(book_list))
    
def read_checkout_list():
    global checkout_list
    checkoutfile = open("checkout.txt", "a")
    checkoutfile.close()
    checkoutfile = open("checkout.txt", "r")
    for line in checkoutfile:
        line = line.strip()
        line = line.split(',')
        member_number = int(line[0])
        book_number = int(line[1])
        new_mem = [member_number, book_number]
        checkout_list.append(new_mem)
    checkoutfile.close()
    
def write_checkout_list():
    global checkout_list
    if (len(checkout_list) != 0):
        checkoutfile = open("checkout.txt", "w")
        for x in checkout_list:
            checkoutfile.write(str(x[0])+",")
            checkoutfile.write(str(x[1]))
            checkoutfile.write('\n')
        checkoutfile.close()
        #print(mem_list)
    
def write_mem_list():
    global mem_list
    memfile = open("members.txt", "w")
    for x in mem_list:
        memfile.write(str(x[0])+",")
        memfile.write(x[1])
        memfile.write('\n')
    memfile.close()
    #print(mem_list)

def write_book_list():
    global book_list
    if (len(book_list) != 0):
        bookfile = open("books.txt", "w")
        for x in book_list:
            bookfile.write(str(x[0])+",")
            bookfile.write(x[1]+",")
            bookfile.write(str(x[2]))
            bookfile.write('\n')
        bookfile.close()
        #print(mem_list)
            
def main():
    while (True):
        print("1.  Add a member")
        print("2.  Remove a member")
        print("3.  Query a member")
        print("4.  Add a book")
        print("5.  Remove a book")
        print("6.  Query a book")
        print("7.  Checkout a book")
        print("8.  Return a book")
        print("9.  Exit this menu")
        choice = int(input("Choose an operation (1-9): "))
        if (choice == 1):
            #add a member
            add_member()
            None
        elif (choice == 2):
            remove_member()
            None
        elif (choice == 3):
            query_member()
            None
        elif (choice == 4):
            add_book()
            None
        elif (choice == 5):
            remove_book()
            None
        elif (choice == 6):
            query_book()
            None
        elif (choice == 7):
            checkout_a_book()
            None
        elif (choice == 8):
            return_a_book()
            None
        elif (choice == 9):
            #exit the menu
            break;
        else:
            print("Invalid choice.  Please try again.")
            print("\n\n")

mem_list = []
book_list = []
checkout_list = []
read_mem_list()
read_book_list()
read_checkout_list()
main()
write_mem_list()
write_book_list()
write_checkout_list()
