movies = []
shows = []
seats = []
bookings = []
while True:
    print("="*5,"Welcome to Movie Ticket Booking System","="*5)
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    main_choice = int(input("Enter Your Choice(1/2/3): "))
    if main_choice == 1:
        while True:
            print("="*7,"ADMIN MENU","="*7)
            print("1. Add Movies")
            print("2. Add Shows")
            print("3. Manage Seats")
            print("4. Delete Movies/Shows")
            print("5. View Booking")
            print("6. Back to Main Menu")
            admin_choice = int(input("Enter your choice Admin(1/2/3/4/5/6): "))
            
            if admin_choice==1:
                    add_movies = input("Enter Movie Name: ")
                    print("="*16)
                    print("Available Movies")
                    print("="*16)
                    movies.append(add_movies)
                    for movie in movies:
                        idx = movies.index(movie)
                        print(idx,".",movie)
                    print(add_movies,"added Sucessfully.")
                    
            elif admin_choice==2:
                add_shows = input("Enter Show Timings: ")
                shows.append(add_shows)
                for show in shows:
                    print(show)
                print(show,"added Sucessfully.")
                print("Add Shows")
                
            elif admin_choice==3:
                while True:
                    print("1. Add Seat.")
                    print("2. Delete Seat.")
                    print("3. View Seats.")
                    print("4. Back.")
                    seats_choice = int(input("Enter your Choice(1/2/3/4): "))
                    if seats_choice == 1:
                        add_seats = input("Enter Seat Number: ")
                        if add_seats in seats:
                            print("Seat Already Exists.")
                        else:
                            seats.append(add_seats)
                            for seat in seats:
                                print(seat,end=",")
                            print(add_seats,"added Sucessfully.")
                    elif seats_choice == 2:
                        print("="*16)
                        print("Available Seats")
                        print("="*16)
                        print(seats)
                        del_seat = input("Enter Seat to Delete: ")
                        if del_seat in seats:
                            seats.remove(del_seat)
                            print("Seat Deleted Successfully.")
                        else:
                            print("Invalid Seat")
                    elif seats_choice == 3:
                        n = len(seats)
                        if n>0:
                            print("="*16)
                            print("Available Seats")
                            print("="*16)
                            for seat in seats:
                                print(seat)
                        else:
                            print("="*20)
                            print("No Seats Available.")
                            print("="*20)
                    elif seats_choice == 4:
                        print("Back")
                        break
                    else:
                        print("Invalid Choice")
                    
                print("Manage Seats")
                
            elif admin_choice==4:
                while True:
                    print("1. Delete Movie.")
                    print("2. Delete Shows.")
                    print("3. Back to Admin Menu.")
                    del_choice = int(input("Enter your Choice(1/2/3): "))
                    if del_choice == 1:
                        print("="*16)
                        print("Available Movies")
                        print("="*16)
                        for movie in movies:
                            idx = movies.index(movie)
                            print(idx,".",movie)
                        del_movie = int(input("Enter Movie No. to Delete: "))
                        if 0<= del_movie and del_movie < len(movies):
                            movies.pop(del_movie)
                            print("Movie Deleted Successfully.")
                        else:
                            print("Invalid Movie No.")
                    elif del_choice == 2:
                        del_show = input("Enter Show Time to Delete: ")
                        if del_show in shows:
                            shows.remove(del_show)
                            print(del_show,"Deleted Sucessfully.")
                    elif del_choice == 3:
                        print("Back to Admin Menu.")
                        break
                    else:
                        print("Invalid Choice")
                    
            elif admin_choice==5:
                print("View Booking")
                
            elif admin_choice == 6:
                print("Back to Main Menu")
                break
            else:
                print("Invalid Choice")
                
    elif main_choice == 2:
        while True:
            print("="*7,"USER MENU","="*7)
            print("1. View Movies")
            print("2. View Showtimes")
            print("3. Select Seats")
            print("4. Book Tickets")
            print("5. View Booking")
            print("6. Back to Main Menu")
            user_choice = int(input("Enter your choice User(1/2/3/4/5/6): "))
            
            if user_choice == 1:
                n = len(movies)
                if n>0:
                    print("="*16)
                    print("Available Movies")
                    print("="*16)
                    for movie in movies:
                        idx = movies.index(movie)
                        print(idx,".",movie)
                else:
                    print("="*20)
                    print("No Movies Available.")
                    print("="*20)
                    
            elif user_choice == 2:
                n = len(shows)
                if n>0:
                    print("="*16)
                    print("Available Shows")
                    print("="*16)
                    for show in shows:
                        print(show)
                else:
                    print("="*20)
                    print("No Shows Available.")
                    print("="*20)
                    
            elif user_choice == 3:
                n = len(seats)
                if n>0:
                    print("="*16)
                    print("Available Seats")
                    print("="*16)
                    for seat in seats:
                        print(seat)
                else:
                    print("="*20)
                    print("No Seats Available.")
                    print("="*20)                
            elif user_choice == 4:
                print("Book Tickets")
                
            elif user_choice == 5:
                print("View Booking")
                
            elif user_choice == 6:
                print("Back to Main Menu")
                break
            else:
                print("Invalid Choice")
                
    elif main_choice == 3:
        print("="*24)
        print("Thank You For Visiting.")
        print("="*24)
        break
    else:
        print("Invalid Choice")