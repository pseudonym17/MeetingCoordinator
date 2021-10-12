"""
Meeting Coordinator

This program will use a database to store group member availabities
"""
import sqlite3

# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create the tables if they aren't already created
cursor.execute("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS hours (id INTEGER PRIMARY KEY AUTOINCREMENT, day TEXT, hour INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS member_has_availability (member_id INTEGER, hour_id INTEGER)")

# Returns the member id given the member name
def get_member_id(name):
	value = (name, )
	cursor.execute("SELECT id FROM members WHERE name == ?", value)
	results = cursor.fetchall()
	return int(results[0][0])

# Gets the hour id from the given day and hour
def get_hour_id(day, hour):
	values = (day, hour)
	cursor.execute("SELECT id FROM hours WHERE day == ? AND hour == ?", values)
	results = cursor.fetchall()
	if results:
		return int(results[0][0])
	else:
		return 0

def get_member_name(id):
	values = (id, )
	cursor.execute("SELECT name FROM members WHERE id == ?", values)
	results = cursor.fetchall()
	return results[0][0]

def get_day(id):
	values = (id, )
	cursor.execute("SELECT day FROM hours WHERE id == ?", values)
	results = cursor.fetchall()
	return results[0][0]

def get_hour(id):
	values = (id, )
	cursor.execute("SELECT hour FROM hours WHERE id == ?", values)
	results = cursor.fetchall()
	return results[0][0]

def is_new_row(name, time_id):
	values = (name, time_id)
	cursor.execute("SELECT * FROM member_has_availability WHERE member_id == ? AND hour_id == ?", values)
	results = cursor.fetchall()
	if results:
		return False
	return True


choice = None
while choice != "8":
	print("1) Display Members")
	print("2) Add Member")
	print("3) Delete Member")
	print("4) Add Hour of Availability")
	print("5) Display Member Hours")
	print("6) Display Group Availability")
	print("7) DELETE All Data")
	print("8) Quit")
	choice = input("> ")
	print()
	if choice == "1":
        # Display Members
		cursor.execute("SELECT * FROM members ORDER BY name")
		print("{:>10}  {:>10}".format("Group Member", "ID"))
		for record in cursor.fetchall():
			print("{:>10}  {:>10}".format(record[1], record[0]))
	elif choice == "2":
        # Add New Member
		try:
			name = input("Name: ")
			id = 0
			values = (name, )
			cursor.execute("INSERT INTO members (name) VALUES (?)", values)
			connection.commit()
		except ValueError:
			print("Invalid input!")
	elif choice == "3":
        # Delete Member
		print("Deleting Member...")
		name = input("Name: ")
		values = (name, )
		id = get_member_id(name)
		id_value = (id, )
		cursor.execute("DELETE FROM members WHERE name = ?", values)
		connection.commit()
		
		#TODO Delete any rows with that member from the availability table
		cursor.execute("DELETE FROM member_has_availability WHERE member_id = ?", id_value)
		connection.commit()

	elif choice == "4":
        # Add Hour of Availability
		print("Add Hour of Availability For Member")
		name = input("Name: ")
		day = input("Day of Week: ")
		hour = input("Enter hour from 8am to 7pm: ")
		values = (day, hour)
		# Stop duplicate time slots from being added to table
		time_id = get_hour_id(day, hour)
		if time_id == 0:
			cursor.execute("INSERT INTO hours (day, hour) VALUES (?,?)", values)
		connection.commit()

		# Also connect the hour to the member
		member_id = get_member_id(name)
		hour_id = get_hour_id(day, hour)
		value_set = (member_id, hour_id)
		if is_new_row(member_id, hour_id):
			cursor.execute("INSERT INTO member_has_availability VALUES (?,?)", value_set)
		connection.commit()

	elif choice == "5":
		# Display Member Times
		cursor.execute("SELECT * FROM member_has_availability")
		member_times = []
		for record in cursor.fetchall():
			line = (get_member_name(record[0]), get_day(record[1]), get_hour(record[1]))
			member_times.append(line)
		
		print("{:>10}  {:>10}  {:>10}".format("Member", "Day", "Hour"))
		for line in member_times:
			print("{:>10}  {:>10}  {:>10}".format(line[0], line[1], line[2]))
	elif choice == "6":
		# Display Times that all members have in common
		# Count Members
		# Count number of instances of an hour_id if >= number of members!
		cursor.execute("SELECT count(id) FROM members")
		mcount = cursor.fetchone()[0]
		values = (mcount, )
		
		cursor.execute("SELECT day, hour FROM member_has_availability JOIN hours ON member_has_availability.hour_id = hours.id GROUP BY hour_id HAVING count(hour_id) == ?", values)

		print("All Members are Available at the Following Times:")
		print("{:>10}  {:>10}".format("Day", "Hour"))
		for record in cursor.fetchall():
			print("{:>10}  {:>10}".format(record[0], record[1]))
	# Remove the tables 
	elif choice == "7":
		print("Clearing the database...")
		print("Emptying tables...")
		print("Ready to start fresh!")
		cursor.execute("DROP TABLE members")
		cursor.execute("DROP TABLE hours")
		cursor.execute("DROP TABLE member_has_availability")

	print()

# Close the database connection before exiting
connection.close()