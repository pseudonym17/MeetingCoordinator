# Overview

By creating this program I am learning to use databases in a program. Previously I had only used databases in MySQL. Now I know how to create, edit, and query my databases within a program so that the data is being used for a purpose.

My program allows a group of members to add their names to the group. Then these members can enter which hours throughout the week they are available for meeting as a group. The members and their available hours are stored into different tables with a table to link the connections between the members and their individual availabilities. Then a search can be performed to find all times that every member of the group has in common to find the best meeting times for the group. There are options the user can run through to add members, delete members, add availabilities, and view data.

My purpose for writing this software is that I have often worked in groups where schedules are limited and it is a struggle to find times to meet. This program offers a solution to this problem by organizing many schedules. I also wanted to gain more experience working with databases and sqlite.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

I am using a database to contain member data and times that members have available.

I have a member table which contains the names and ids of the group members. I have a hour table which contains days and hours and gives an id to each time slot. Lastly, I have a table which is a linking table between the two previous tables. This table contains the id of a member and the id of the time slot which that member has available.

# Development Environment

Replit.com was used to develop the software.

Python is the language the software is written in.
Sqlite is the language used to query, and edit the database.

# Useful Websites

* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [SQLite Python](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)
* [w3resource](https://www.w3resource.com/sqlite/index.php)

# Future Work

* I would like to eventually create an app to access the database so I can have a more user-friendly interface and design.
* I would like to add some error handling for the user input.
* I would like add more details to the database, such as more information on the members and more.