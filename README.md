# Library_managment_system_software
Developing a software using python for library management
## Project Description (Scenario):
You are asked to build a system by using object oriented programming concepts. It should be possible to create objects from your implemented Python classes. Each class should contain information about different parts of the system. The objects should be created from the classes and interact with each other to achieve the correct functionality of the system. There are several Python classes to be written. The system should include the following Python classes as minimum: Books, BookList, Users, UserList and Loans.

## System Components:
1- Books class: Define a Python class with methods to do the following:

Each record should have include the following attributes:     
1.1 Randomly generated book ID, title, author, year, publisher, number of available copies and publication date.    
1.2 Define different methods to set each of the following book attributes, one method per attribute:    
title, author, year, publisher, number of available copies and publication date.
1.3 Define  different methods to return each the following book attribute, one method per attribute:    
title, author, year, publisher, number of copies, available number of copies and publication attribute.


2- BookList: Define a Python class with methods to do the following:

2.1 Define a method to store a collection (e.g., dictionary). The collection should store book instances that are created from the Book object.   
2.2 Define a method to search through the collection and find a book by one of the following data: title, author, publisher OR publication date.    
2.3 Define a method to remove a book from the collection. The book should be specified by its title.    
2.4 Define a method to return the total number of books stored in the collection.    

3- Users: Define a Python class with functions to do the following:  

3.1 Define a constructor to create a user with the following attributes:   
username, firstname, surname, house number, street name, postcode, email address, and date of birth.   
3.2 Define different method to return the following attributes: username, firstname, surname, house number, street name, postcode, email address, and date of birth. You should have one method per attribute.     
3.3 Define different methods to edit the following attribute: firstname, surname, email address, and date of birth. You should have one method per attribute. 


4- UserList: Define a Python class with functions to do the following:


4.1 A method to store a collection (e.g., dictionary) of user instances that are created with the class Users.  
4.2 A method to remove a user from the collection by giving the user’s first name. This operation must inform program users if there are two or more users with same first name.    
4.3 A method to count the number of users in the system. This should be based on the number of user object in the collection.    
4.4 A method to return a user’s detail by the username.   


5- Loans: Define a Python class with methods to do the following:


5.1 A method for a user to borrow a book. This method should have appropriate features to assign a book to a user. The information could be stored in an appropriate data structure for further processing.   
5.2 A method for a user to return a book. This method should un-assign a book previously assigned to a user.   
5.3 A method to count and return the total number of books a user is currently borrowing.    
5.4 A method to print out all the overdue books along with the users’ username and first name. The username and first name of the user should be retrieved through the appropriate methods in the User class.   


## Table of Content (Files):
1-system source file (system_source_code.py)
