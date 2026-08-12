movies = []
shows = []
seats = []
bookings = []
password = "madhusai"
while True:
    print("="*5,"Welcome to Movie Ticket Booking System","="*5)
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    main_choice = int(input("Enter Your Choice(1/2/3): "))
    if main_choice == 1:
        admin_pass = input("Enter Admin password: ").lower()
        if admin_pass == password:
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
                        add_movies = input("🎬 Enter Movie Name: ").capitalize()
                        if add_movies in movies:
                            print("Movie Already Exists.😑")
                        else:
                            print("="*16)
                            print("🎬 Available Movies")
                            print("="*16)
                            movies.append(add_movies)
                            shows.append([])
                            seats.append([])
                            for movie in movies:
                                idx = movies.index(movie)
                                print(idx,".",movie)
                            print(add_movies,"added Sucessfully.✅")
                        
                elif admin_choice==2:
                    print("="*16)
                    print("🎬 Available Movies")
                    print("="*16)
                    for movie in movies:
                        idx = movies.index(movie)
                        print(idx,".",movie)
                    movie_choice = int(input("🎬 Enter Movie No. to Add Show: "))
                    if 0<= movie_choice and movie_choice < len(movies):
                        print("Selected Movie:",movies[movie_choice])
                        add_shows = input("⏱️ Enter Show Timings(10:00AM): ").upper()
                        shows[movie_choice].append(add_shows)
                        for show in shows[movie_choice]:
                            print(show)
                        print(show,"added Sucessfully.✅")
                    else:
                        print("❌ Invalid Movie No.")
                    
                elif admin_choice==3:
                    while True:
                        print("1. Add Seat.")
                        print("2. Delete Seat.")
                        print("3. View Seats.")
                        print("4. Back.")
                        seats_choice = int(input("Enter your Choice(1/2/3/4): "))
                        if seats_choice == 1:
                            print("="*16)
                            print("🎬 Available Movies")
                            print("="*16)
                            for movie in movies:
                                idx = movies.index(movie)
                                print(idx,".",movie)
                            movie_choice = int(input("🎬 Enter Movie No. to Add Seat: "))
                            if 0<= movie_choice and movie_choice < len(movies):
                                print("Selected Movie:",movies[movie_choice])
                                while True:
                                    print("1. Add More Seats")
                                    print("2. Back to Seats Menu.")
                                    choice = int(input("Enter your Choice(1/2): "))
                                    if choice==1:
                                        add_seats = input("🔢 Enter Seat Number(A1/B1/C1): ").upper()
                                        if add_seats in seats[movie_choice]:
                                            print("❌ Seat already exists.")
                                        else:
                                            seats[movie_choice].append(add_seats)
                                            for seat in seats[movie_choice]:
                                                print(seat)
                                            print(seat,"added Sucessfully.✅")
                                    elif choice == 2:
                                        break
                                    else:
                                        print("❌ Invalid Choice.")
                            else:
                                print("❌ Invalid Movie No.")
                                
                        elif seats_choice == 2:
                            print("="*16)
                            print("Available Movies")
                            print("="*16)
                            for movie in movies:
                                idx = movies.index(movie)
                                print(idx,".",movie)
                            movie_choice = int(input("Enter Movie No. to Delete Seat: "))
                            if 0<=movie_choice and movie_choice<len(movies):
                                print("Selected Movie:",movies[movie_choice])
                                if len(seats[movie_choice]) > 0:
                                    print("="*16)
                                    print("Available Seats")
                                    print("="*16)
                                    for seat in seats[movie_choice]:
                                        print(seat)
                                    del_seat = input("⏱️ Enter Seat to Delete: ").upper()
                                    if del_seat in seats[movie_choice]:
                                        seats[movie_choice].remove(del_seat)
                                        print(del_seat,"Deleted Sucessfully.")
                                    else:
                                        print("❌ Invalid Seat")
                                else:
                                    print("😑 No Seats Available for this Movie.")
                                    
                        elif seats_choice == 3:
                            print("="*16)
                            print("Available Movies")
                            print("="*16)
                            for movie in movies:
                                idx = movies.index(movie)
                                print(idx,".",movie)
                            movie_choice = int(input("Enter Movie No. to View Seats: "))
                            if 0<=movie_choice and movie_choice<len(movies):
                                print("Selected Movie:",movies[movie_choice])
                                if len(seats[movie_choice])>0:
                                    print("="*16)
                                    print("Available Seats")
                                    print("="*16)
                                    for seat in seats[movie_choice]:
                                        print(seat)
                                else:
                                    print("="*20)
                                    print("No Seats Available.")
                                    print("="*20)
                                
                        elif seats_choice == 4:
                            print("Back")
                            break
                        else:
                            print("❌ Invalid Choice")
                        
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
                                shows.pop(del_movie)
                                seats.pop(del_movie)
                                print("Movie Deleted Successfully.✅")
                                print("Shows Deleted Successfully.✅")
                                print("Seats Deleted Successfully.✅")
                            else:
                                print("❌ Invalid Movie No.")
                        elif del_choice == 2:
                            print("="*16)
                            print("Available Movies")
                            print("="*16)
                            for movie in movies:
                                idx = movies.index(movie)
                                print(idx,".",movie)
                            movie_choice = int(input("Enter Movie No. to Delete Show: "))
                            if 0<=movie_choice and movie_choice<len(movies):
                                print("Selected Movie:",movies[movie_choice])
                                if len(shows[movie_choice]) > 0:
                                    print("="*16)
                                    print("Available Shows")
                                    print("="*16)
                                    for show in shows[movie_choice]:
                                        print(show)
                                    del_show = input("⏱️ Enter Show Time to Delete: ").upper()
                                    if del_show in shows[movie_choice]:
                                        shows[movie_choice].remove(del_show)
                                        print(del_show,"Deleted Sucessfully.✅")
                                    else:
                                        print("❌ Invalid Show Time")
                                else:
                                    print("😑 No Shows Available for this Movie.")
                                    
                        elif del_choice == 3:
                            print("Back to Admin Menu.")
                            break
                        else:
                            print("❌ Invalid Choice")
                        
                elif admin_choice==5:
                    if len(bookings)>0:
                        print("="*16)
                        print("Available Bookings")
                        print("="*16)
                        for booking in bookings:
                            print(*booking)
                    else:
                        print("="*20)
                        print("No Booking Available.")
                        print("="*20)
                    
                elif admin_choice == 6:
                    print("Back to Main Menu")
                    break
                else:
                    print("❌ Invalid Choice")
        else:
            print("❌ Invalid Password")       
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
                if len(movies)>0:
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
                    print("Available Movies")
                    print("="*16)
                    for movie in movies:
                        idx = movies.index(movie)
                        print(idx,".",movie)
                    movie_choice = int(input("Enter Movie No. to View Show: "))
                    if 0<= movie_choice and movie_choice < len(movies):
                        print("Selected Movie:",movies[movie_choice])
                        print("="*16)
                        print("Available Shows")
                        print("="*16)
                        for show in shows[movie_choice]:
                            print(show)
                        
                else:
                    print("="*20)
                    print("No Shows Available.")
                    print("="*20)
                    
            elif user_choice == 3:
                print("="*16)
                print("Available Movies")
                print("="*16)
                for movie in movies:
                    idx = movies.index(movie)
                    print(idx,".",movie)
                movie_choice = int(input("Enter Movie No. to Delete Show: "))
                if 0<=movie_choice and movie_choice<len(movies):
                    print("Selected Movie:",movies[movie_choice])
                    if len(seats[movie_choice])>0:
                        print("="*16)
                        print("Available Seats")
                        print("="*16)
                        for seat in seats[movie_choice]:
                            print(seat)
                    else:
                        print("="*20)
                        print("No Seats Available.")
                        print("="*20)    
                              
            elif user_choice == 4:
                print("="*16)
                print("Available Movies")
                print("="*16)
                for movie in movies:
                    idx = movies.index(movie)
                    print(idx,".",movie)
                movie_choice = int(input("🎬 Enter Movie No.: "))
                if 0<=movie_choice and movie_choice<len(movies):
                    print("Selected Movie:",movies[movie_choice])
                    if len(shows[movie_choice])>0:
                        print("="*16)
                        print("Available Shows.")
                        print("="*16)
                        for show in shows[movie_choice]:
                            print(show)
                    else:
                        print("❌ No Shows Available.")
                    if len(seats[movie_choice])>0:
                        print("="*16)
                        print("Available Seats.")
                        print("="*16)
                        for seat in seats[movie_choice]:
                            print(seat)
                    else:
                        print("❌ No Seats Available.")
                    show_choice = input("Select Show Timing(10:00 AM): ").upper()
                    while True:
                        print("1. Add More Seats")
                        print("2. Back to Seats Menu.")
                        choice = int(input("Enter your Choice(1/2): "))
                        if choice==1:
                            seat_choice = input("🔢 Enter Seat Number(A1/B1/C1): ").upper()
                            if seat_choice in seats[movie_choice]:
                                seats[movie_choice].remove(seat_choice)
                                bookings.append([movies[movie_choice],show_choice])
                                bookings.append(seat_choice)
                                print("Seat Added Sucessfully.✅")
                                print("Booking Sucessful.✅")
                            else:
                                print("Invalid Seat Choice.❌")
                        elif choice == 2:
                            break
                        else:
                            print("❌ Invalid Choice.")
                
            elif user_choice == 5:
                if len(bookings)>0:
                    print("="*16)
                    print("Available Bookings")
                    print("="*16)
                    for booking in bookings:
                        print(*booking)
                else:
                    print("No Booking Availbale.")
                
            elif user_choice == 6:
                print("Back to Main Menu")
                break
            else:
                print("❌ Invalid Choice")
                
    elif main_choice == 3:
        print("="*24)
        print("Thank You For Visiting.")
        print("="*24)
        break
    else:
        print("❌ Invalid Choice")