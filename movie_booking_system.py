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
                print("Manage Seats")
                
            elif admin_choice==4:
                while True:
                    print("1. Delete Movie.")
                    print("2. Delete Shows.")
                    print("3. Back to Admin Menu")
                    del_choice = int(input("Enter your Choice(1/2/3): "))
                    if del_choice == 1:
                        del_movie = input("Enter Movie Name to Delete: ")
                        if del_movie in movies:
                            movies.remove(del_movie)
                            print(del_movie,"Movie Deleted Sucessfully.")
                        else:
                            print("Movie Not Found.")
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
                print("Select Seats")
                
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
        print("*"*5,"Thank You For Visiting.","*"*5)
        break
    else:
        print("Invalid Choice")