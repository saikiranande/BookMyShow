x = 10
Booked_seat = 0
price_of_ticket = 0
total_income = 0
rows = int(input('Enter the rows : '))
row_seats = int(input('Enter the row seats : '))
total_seats = rows*row_seats
Booked_ticket_person = [[None for j in range(row_seats)]for i in range(rows)]

class Seatsview:
    @staticmethod
    def show_the_seats():
        seats_view = {}
        for i in range(rows):
            seats = {}
            for j in range(row_seats):
                seats[str(j+1)]='S'
            seats_view[str(i)] = seats
        return seats_view

    @staticmethod
    def find_percentage():
        percentage = (Booked_seat/total_seats)*100
        return percentage

class_call=Seatsview
table_of_seats = class_call.show_the_seats()

while x != 0:
    print('1. Show_the_seat \n2. buy_ticket ',
        '\n3. statistics \n4. Show booked Tickets User Info \n0 Exit')
    x = int(input('select option -'))
    if x == 1:
        if row_seats < 10:
            for seat in range(row_seats):
                print(seat,end = ' ')
            print(row_seats)
        else:
            for seat in range(10):
                print(seat,end =' ')
            for seat in range(10,row_seats):
                print(seat,end = ' ')
            print(row_seats)
        if row_seats < 10:
            for num in table_of_seats.keys():
                print(int(num)+1, end = ' ')
                for no in table_of_seats[num].values():
                    print(no,end = ' ')
                print()
        else:
            count_num = 0
            for num in table_of_seats.keys():
                if int(list(table_of_seats.keys())[count_num]) < 9:
                    print(int(num)+1, end = ' ')
                else:
                    print(int(num)+1, end = ' ')
                count_key = 0
                for no in table_of_seats[num].values():
                    if int(list(table_of_seats[num].keys())[count_key]) <=10:
                        print(no,end = ' ')
                    else:
                        print(no,end = ' ')
                        count_key += 1
                    count_num += 1
                print()
            print('Vacant seats =', total_seats-Booked_seat)
            print()

    elif x == 2:
        Row_num = int(input('Enter the row number -\n'))
        Column_num = int(input('Enter the column number -\n'))
        if Row_num in range(1,rows+1) and Column_num in range(1,row_seats+1):
            if table_of_seats[str(Row_num-1)][str(Column_num)] == 'S':
                if total_seats <= 60:
                    price_of_ticket = 10
                elif Row_num <=int(rows/2):
                    price_of_ticket = 10
                else:
                    price_of_ticket = 8
                print('price_of_ticket - ', '$', price_of_ticket)
                conform = input('yes for booking and no for Stop booking - ')
                person_details = {}
                if conform == 'yes':
                    person_details['Name'] = input('Enter Name - ')
                    person_details['Gender'] = input('Enter Gender - ')
                    person_details['Age'] = input('Enter Age - ')
                    person_details['Phone_No'] = input('Enter Phone number - ')
                    person_details['Ticket_price'] = price_of_ticket
                    table_of_seats[str(Row_num-1)][str(Column_num )] = 'B'
                    Booked_seat += 1
                    total_income = total_seats * price_of_ticket
                else:
                    continue
                Booked_ticket_person[Row_num-1][Column_num-1] = person_details
                print('Booked Successfully')
            else: 
                print('This seat already booked by some one')
        else:
            print()
            print('Invalid Input'.centre(10,'*'))
        print()
    elif x == 3:
        print('Number of purchased Tickets -', Booked_seat)
        print('Percentage -', class_call.find_percentage)
        print('Current income -','$', price_of_ticket)
        print('total_income -','$',total_income )

    elif x == 4:
        Enter_row = int(input('Enter Row number - \n'))
        Enter_column = int(input('Enter Column number - \n'))
        if Enter_row in range(1, rows+1) and Enter_column in range(1, row_seats+1):
            if table_of_seats[str(Enter_row-1)][str(Enter_column)] == 'B':
                person = Booked_ticket_person[Enter_row - 1][Enter_column - 1]
                print('Name - ', person['Name'])
                print('Gender - ', person['Gender'])
                print('Age - ', person['Age'])
                print('Phone number - ', person['Phone_No'])
                print('Ticket Price - ', '$', person['Ticket_price'])
            else:
                print()
                print('Vacant seat')
        else:
            print()
            print('Invalid Input'.center(10,'*'))
        print()

    else:
        print()
        print('Invalid Input'.center(10,'*'))
        print()
        