'''
Movie Ticket Booking Problem Statement
-------------------------------------------------------------------------------------------------------------------------
-> Provide Admin Login Facility with username & password, then only admin can do all task
-> Provide User Registration & Login Facility with username & password, then only usercan do all task
-> User registration data(name, phone, address, username, password)
-> Assign unique ID to identify each records
-------------------------------------------------------------------------------------------------------------------------
	Admin Login
		Add list of movies
		Select Movie that is Avaliable
				Select a movie which shows is going on now. Ticket booking will be started only for this movie
		Buy a Ticket
				Admin can book ticket on ticket_counter ,  if seat is already booked show message "Seat already booked"
		Show Ticket (status of ticket)
				Show booked ticket status with seat_number,
		Cancel Ticket
				After cancellation of ticket, same seat number can be booked
		Logout
------------------------------------------------------------------------------------------------------------------------		
	User Login
		Buy a Ticket
				User can book ticket on ticket_counter, if seat is already booked show message "Seat already booked"
		Show Ticket (status of ticket)
				Show booked ticket status with seat_number, 
		Cancel Ticket
				After cancellation of ticket, show paid amount will be refund with 20% deduction
		Logout
	Exit
------------------------------------------------------------------------------------------------------------------------	
'''

