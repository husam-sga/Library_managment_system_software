''' Library record software system designed using python programming and object oriented programming techniques by implementing classes'''

#Section One: importing necessary libraries:
import random
import names
import datetime
import radar
import os
import base64
from collections import Counter
import sys


#Section Two: Creating necessary functions to help generate book attributes' values and user attributes' values:
#2.1 Creating book titles:
books = []
def random_title():
      try:
         word1 = ['A Funny', 'The Goofy', 'A Kawaii', 'The Spooky', 'The Smart', 'The Cute', 'The Cruel', 'An Ugly', 'The Bad', 'A Hungry']
         word2 = ['Mouse', 'Cat', 'Dog', 'Bat', 'Turtle', 'Moose', 'Hedgehog', 'Monkey', 'Shark', 'Baby Shark']
         word3 = ['Flies', 'Rises', 'Sleeps', 'Runs' , 'Walks', 'Crumbles', 'Fights' , 'Swims', 'Travels', 'Hunts']
         rand1 = random.randint(0,9)
         rand2 = random.randint(0,9)
         rand3 = random.randint(0,9)
         title = word1[rand1] +' '+ word2[rand2] +' '+ word3[rand3]
         books.append(title)
         if books.count(title) == 1:
               return title
      except:
         if book.count(title) > 1:
             print('This book already exists, creating a new book...')
             random_title()



#2.2 Creating a publishers list:
def publishers():
  publishers = ['Valve', 'Sony', 'EA', 'Riley' , 'Husam Publishing' , 'The Brothers', ' The Brotherhood', 'Bandicoots', 'Cortex', 'Splinters']
  random_pub = random.randint(0,9)
  publisher = publishers[random_pub]
  return publisher

#2.3 Creating a years list:
def years():
  years = [1998, 1987, 1873, 2009, 2002, 2007, 2010, 1992, 1877, 2001]
  random_year = random.randint(0,9)
  global year1
  year1 = years[random_year]
  return year1


#2.4 Creating a random dates:
def random_date():
  date = str(radar.random_date(start = datetime.date(year=2010, month=1, day=1),stop = datetime.date(year=2022, month=12, day=30)))
  return date


#2-5 Creating random emails:
emails = []
def random_email():
      try:
         word1 = ['Funny', 'Goofy', 'Kawaii', 'Spooky', 'Smart', 'Cute', 'Cruel', 'Ugly', 'Bad', 'Hungry']
         word2 = ['Mouse', 'Cat', 'Dog', 'Bat', 'Turtle', 'Moose', 'Hedgehog', 'Monkey', 'Shark', 'Baby']
         word3 = ['123', '111', '578', '24' , '999', '6754', '1234' , '9999', '55', '1992']
         word4 = ['gmail', 'yahoo', 'hotmail', 'outlook' , 'husammail', 'birdmail', 'email' , 'homail', 'farmail', 'bibmail']
         rand1 = random.randint(0,9)
         rand2 = random.randint(0,9)
         rand3 = random.randint(0,9)
         rand4 = random.randint(0,9)
         email = word1[rand1] +'_'+ word2[rand2] +'_'+ word3[rand3]+'@'+ word4[rand4]+'.com'
         emails.append(email)
         if emails.count(email) == 1:
               return email
      except:
             print('This email already exists, create a new email.')
             random_email()

#2-6 Creating random street names:
streets = []
def random_street():
         word1 = ['Funny', 'Goofy', 'Kawaii', 'Spooky', 'Smart', 'Cute', 'Cruel', 'Ugly', 'Bad', 'Hungry']
         word2 = ['Mouse Street', 'Cat Street', 'Dog Street', 'Bat Street', 'Turtle Street', 'Moose Street', 'Hedgehog street', 'Monkey Street', 'Shark Street', 'Baby Street']
         rand1 = random.randint(0,9)
         rand2 = random.randint(0,9)
         street = word1[rand1] +' '+ word2[rand2]
         return street

#2-7 Creating random username:
usernames = []
def random_username():
         word1 = ['Funny', 'Goofy', 'Kawaii', 'Spooky', 'Smart', 'Cute', 'Cruel', 'Ugly', 'Bad', 'Hungry']
         word2 = ['Mouse', 'Cat', 'Dog', 'Bat', 'Turtle', 'Moose', 'Hedgehog', 'Monkey', 'Shark', 'Baby']
         word3 = ['123', '111', '578', '24' , '999', '6754', '1234' , '9999', '55', '1992']
         rand1 = random.randint(0,9)
         rand2 = random.randint(0,9)
         rand3 = random.randint(0,9)
         username = word1[rand1] +'_'+ word2[rand2] +word3[rand3]
         usernames.append(username)
         if usernames.count(username) == 1:
               return username
         else:
            print('This username already exists, creating a new username...')
            random_username()
               
  


#Section Three: Building up classes for the library record system:
#1- Creating the Books class:
class Books:
    
    #1-1 Creating a constructor with initial values for the book attributes:
    def __init__(self, book_id = 0 , title ='' , author = '', year = 0 , publisher ='' , available_copies = 1 , publication_date=''):
        self.book_id = base64.urlsafe_b64encode(os.urandom(3)).decode('ascii').upper()
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.available_copies = available_copies
        self.publication_date = publication_date

 
    #1-2 Setting and getting title using random_title() function:
    def set_title(self, title = '' ):
        self.title = random_title()
        
    def get_title(self):
        return self.title
    
    #1-3 Setting and getting author:
    def set_author(self, author = ''):
        self.author = names.get_full_name()
        
    def get_author(self):
        return self.author

    #1-4 Setting and getting year using years() function:
    def set_year(self, year = ''):
        self.year = years()
        
    def get_year(self):
        return self.year

    #1-5 Setting and getting publisher using publishers() function:
    def set_publisher(self,publisher = ''):
        self.publisher = publishers()
        
    def get_publisher(self):
        return self.publisher

    #1-6 Setting and getting available copies:
    def set_available_copies(self,available_copies = 1):
        self.available_copies = available_copies
        
    def get_available_copies(self):
        return self.available_copies

    #1-7 Setting and getting publication date using random_date() function:
    def set_date(self, publication_date = ''):
        self.publication_date = random_date()
        
    def get_date(self):
        return self.publication_date

        
      
                 



#2- Creating the BookList class:
        

class BookList(Books):
    #2-1 Defining a constructor to create new object from this class:
    def __init__(self):
        self.book_list = []
          
    #2-2 Storing books in the book list:
    def store_book(self, book):
        self.book_list.append(book)
        
    #2-3 Method to remove a book from the books list:
      
    def remove_book(self):
       #Checking if the book list is empty:
       if len(self.book_list) == 0:
               print('No book exists in the system yet. you will be redirected back to the main menu...')
               main()
       else:
        #Asking for the book title to remove:
        remove_book = input('Input the title of the book you would like removed or type "back" to go back to the main menu: ').title()
        #input validation:
        while True:
          #Looping through the book_list for the given book title and removing the book object when a match is found:
          for item in self.book_list:
            if remove_book == item.title:
               print('The book titled "',item.title,'"has been removed!')
               self.book_list.remove(item)
               #Prompting the user whether they want to take another action or terminate the system:
               finalize = input('Would there be anything else? (yes or no)').capitalize()
               while True:
                 if finalize not in ['Yes' , 'No']:
                       print('Error: Please enter either yes or no')
                       finalize = input('Would there be anything else? (yes or no)').capitalize()
                 else:
                       #System shuts if the answer is "No":
                       if finalize == 'No':
                          sys.exit()
                       else:
                          #Returning to the main menu when the answer is "Yes":
                          print('Being directed to the main menu...')
                          main()
            #Returning to the main menu when an input of "back" is given:
          if remove_book == 'Back':
              print('Being directed to the main menu ...')
              main()
            #The user is prompted to enter the correct input by showing them an error message: 
          else:
              remove_book = input('Error: Please enter a valid book title to remove or "back" to go back to the main menu: ').title()
       


               
               
    #2-4 Method to search through the books using title,author,publisher or publication date as keys:    
    def search_book(self):
          
        #Checking if the book list is empty:
        if len(self.book_list) == 0:
               print('No book exists in the system yet. you will be redirected back to the main menu...')
               main()
        else:
          print('Select one of the following to find a desired book:')
          print('1.Title. \n2.Author. \n3.Publisher. \n4.Publication Date.')
          search_method = input('Please input the numbers from 1 to 4 for the desired method: ')
          while True:
            if search_method not in ['1','2','3','4']:
                  search_method = input('Please input the number of the desired method (1 to 4): ')
            else:
                 search_method = int(search_method)
                 if search_method == 1:
                      book_title = input('What is the title of the book you are looking for? or type "back" to go back to the main menu: ').title()
                      while True:
                         for book in self.book_list:
                           if book_title == book.title:
                             print('\nBook details:')
                             print('\nID:',book.book_id,'\nTitle:',book.title,'\nAuthor:',book.author,'\nYear:',book.year,
                                '\nPublisher:',book.publisher,'\nAvailable copies:',book.available_copies,'\nPublication Date:',book.publication_date)

                             #Prompting the user whether they want to take another action or terminate the system:
                             finalize = input('Would there be anything else? (yes or no)').capitalize()
                             while True:
                                if finalize not in ['Yes' , 'No']:
                                    print('Error: Please enter either yes or no')
                                    finalize = input('Would there be anything else? (yes or no)').capitalize()
                                else:
                                 #System shuts if the answer is "No":
                                 if finalize == 'No':
                                      sys.exit()
                                 else:
                                     #Returning to the main menu when the answer is "Yes":
                                     print('Being directed to the main menu...')
                                     main()
                           #Returning to the main menu when an input of "back" is given:
                         if book_title == 'Back':
                                print('Being directed to the main menu ...')
                                main()
                                
                           #The user is prompted to enter the correct input by showing them an error message:
                         else:
                                book_title = input('Error: Please enter a valid book title to remove or "back" to go back to the main menu: ').title()



                      
                                
                           
                                    
                 elif search_method == 2:
                      book_author = input("What is the author's name of the book you are looking for? or type 'back' to go back to the main menu ").title()
                      while True:
                         for book in self.book_list:
                           if book_author == book.author:
                             print('\nBook details:')
                             print('\nID:',book.book_id,'\nTitle:',book.title,'\nAuthor:',book.author,'\nYear:',book.year,
                                '\nPublisher:',book.publisher,'\nAvailable copies:',book.available_copies,'\nPublication Date:',book.publication_date)

                             #Prompting the user whether they want to take another action or terminate the system:
                             finalize = input('Would there be anything else? (yes or no)').capitalize()
                             while True:
                                if finalize not in ['Yes' , 'No']:
                                    print('Error: Please enter either yes or no')
                                    finalize = input('Would there be anything else? (yes or no)').capitalize()
                                else:
                                 #System shuts if the answer is "No":
                                 if finalize == 'No':
                                      sys.exit()
                                 else:
                                     #Returning to the main menu when the answer is "Yes":
                                     print('Being directed to the main menu...')
                                     main()
                           
                           #Returning to the main menu when an input of "back" is given:
                         if book_author == 'Back':
                                print('Being directed to the main menu ...')
                                main()

                           #The user is prompted to enter the correct input by showing them an error message:
                         else:
                                book_author = input('Error: Please enter a valid book title to remove or "back" to go back to the main menu: ').title()

                                

                 elif search_method == 3:
                      book_publisher = input("What is the publisher of the book you are looking for? or type 'back' to go back to the main menu ").title()
                      while True:
                         for book in self.book_list:
                           if book_publisher == book.publisher:
                             print('\nBook details:')
                             print('\nID:',book.book_id,'\nTitle:',book.title,'\nAuthor:',book.author,'\nYear:',book.year,
                                '\nPublisher:',book.publisher,'\nAvailable copies:',book.available_copies,'\nPublication Date:',book.publication_date)
                             
                             #Prompting the user whether they want to take another action or terminate the system:
                             finalize = input('Would there be anything else? (yes or no)').capitalize()
                             while True:
                                if finalize not in ['Yes' , 'No']:
                                    print('Error: Please enter either yes or no')
                                    finalize = input('Would there be anything else? (yes or no)').capitalize()
                                else:
                                 #System shuts if the answer is "No":
                                 if finalize == 'No':
                                      sys.exit()
                                 else:
                                     #Returning to the main menu when the answer is "Yes":
                                     print('Being directed to the main menu...')
                                     main()
                                     
                           #Returning to the main menu when an input of "back" is given:
                         if book_publisher == 'Back':
                                print('Being directed to the main menu ...')
                                main()
                                
                           #The user is prompted to enter the correct input by showing them an error message:
                         else:
                                book_publisher = input('Error: Please enter a valid book title to remove or "back" to go back to the main menu: ').title()



                 elif search_method == 4:
                      book_date = input("What is the publication date of the book you are looking for? valid format for dates is yyyy-mm-dd or type 'back' to go back to the main menu ").title()
                      while True:
                         for book in self.book_list:
                           if book_date == book.publication_date:
                             print('\nBook details:')
                             print('\nID:',book.book_id,'\nTitle:',book.title,'\nAuthor:',book.author,'\nYear:',book.year,
                                '\nPublisher:',book.publisher,'\nAvailable copies:',book.available_copies,'\nPublication Date:',book.publication_date)

                             #Prompting the user whether they want to take another action or terminate the system:
                             finalize = input('Would there be anything else? (yes or no)').capitalize()
                             while True:
                                if finalize not in ['Yes' , 'No']:
                                    print('Error: Please enter either yes or no')
                                    finalize = input('Would there be anything else? (yes or no)').capitalize()
                                else:
                                 #System shuts if the answer is "No":
                                 if finalize == 'No':
                                      sys.exit()
                                 else:
                                     #Returning to the main menu when the answer is "Yes":
                                     print('Being directed to the main menu...')
                                     main()
                                     
                           #Returning to the main menu when an input of "back" is given:
                         if book_date == 'Back':
                                print('Being directed to the main menu ...')
                                main()

                           #The user is prompted to enter the correct input by showing them an error message:
                         else:
                                book_date = input('Error: Please enter a valid book title to remove or "back" to go back to the main menu: ').title()



                           
    #2-5 Method to display the number of books available in the book list:
    def number_of_books(self):
          
             book_num = len(self.book_list)
             print('The Library currently has', book_num, 'books in it.')
             finalize = input('Would there be anything else? (yes or no)').capitalize()
             while True:
                if finalize not in ['Yes' , 'No']:
                       print('Error: Please enter either yes or no')
                       finalize = input('Would there be anything else? (yes or no)').capitalize()
                else:
                  #System shuts if the answer is "No":
                  if finalize == 'No':
                       sys.exit()
                  else:
                      #Returning to the main menu when the answer is "Yes":
                      print('Being directed to the main menu...')
                      main()





    #EXTRA (1): Editing a book's title, author, year, publisher and available number of copies:
    def edit_book(self):
       #Validating if the book list is empty:
       if len(self.book_list) == 0:
               print('No book exists in the system yet. you will be redirected back to the main menu...')
               main()
       else:
       #Asking for the book's title we would like to edit:
         book_title = input("What is the title of the book you are trying to edit? or type 'back' to go back to the main menu ").title()
         while True:
          for book in self.book_list:
              if book_title == book.title:
                   #Displaying the book's details before editting:
                   print('\nThe Book Details are:')
                   print('\nID:',book.book_id,'\nTitle:',book.title,'\nAuthor:',book.author,'\nYear:',book.year,
                   '\nPublisher:',book.publisher,'\nAvailable copies:',book.available_copies,'\nPublication Date:',book.publication_date)

                   #Displaying the attributes which have been edited using the setters and the helping functions from section (2):
                   print('\nThe Book title has been edited to:')
                   book.set_title()
                   print(book.title,'\n')
                   
                   print('The Book author has been edited to:')
                   book.set_author()
                   print(book.author,'\n')
     
                   print('The Book year has been edited to:')
                   book.set_year()
                   print(book.year,'\n')
      
                   print('The Book publisher has been edited to:')
                   book.set_publisher()
                   print(book.publisher,'\n')
      
                   print('The Book available copies has been edited to:')
                   book.set_available_copies()
                   print(book.available_copies,'\n')
                  
                   #Prompting the user whether they want to take another action or terminate the system:
                   finalize = input('Would there be anything else? (yes or no)').capitalize()
                   while True:
                    if finalize not in ['Yes' , 'No']:
                      print('Error: Please enter either yes or no')
                      finalize = input('Would there be anything else? (yes or no)').capitalize()
                    else:
                     #System shuts if the answer is "No":
                     if finalize == 'No':
                         sys.exit()
                     else:
                      #Returning to the main menu when the answer is "Yes":
                      print('Being directed to the main menu...')
                      main()
                           
                  #Returning to the main menu when an input of "back" is given:
          if book_title == 'Back':
              print('Being directed to the main menu ...')
              main()

         #The user is prompted to enter the correct input by showing them an error message:

          else:
              book_title = input('Error: Please enter a valid book title to edit its book or "back" to go back to the main menu: ').title()
      
      


    #2-6 Method to remove a book from the book list without asking for an input (will be used in the loan class):
    def remove_book2(self, book):
        self.book_list.remove(book)



    #2-7 Method to show all the books currently available in the library:        
    def showbook(self):
         if len(self.book_list) == 0:
                 print('The library system has no books in it currently, please add some books using option (0) in the main menu!')
                 main()
         else:
           count = 1
           for book in self.book_list:
              print('\nBook', count, 'details:')
              print('\nID:',book.book_id,'\nTitle:',book.title,'\nAuthor:',book.author,'\nYear:',book.year,
                  '\nPublisher:',book.publisher,'\nAvailable copies:',book.available_copies,'\nPublication Date:',book.publication_date)
              count += 1
           #Giving the user an option to make another action or exit the library:
           finalize = input('Would there be anything else? (yes or no)').capitalize()
           while True:
             if finalize not in ['Yes' , 'No']:
               print('Error: Please enter either yes or no')
               finalize = input('Would there be anything else? (yes or no)').capitalize()
             else:
               #System shuts if the answer is "No":
               if finalize == 'No':
                   sys.exit()
               else:
                   #Returning to the main menu when the answer is "Yes":
                   print('Being directed to the main menu...')
                   main()
                   
    #2-8 Method to help iterate through the book list:
    def __getitem__(self, index):
        return self.book_list[index]
        

             
             
      


#3- Creating the Users class:

class Users:
    #1 Define a constructor to create a user with the following attributes:
    def __init__(self,username = '', firstname = '', surname = '', house_number = 0,
                 street_name = '', post_code = 00000, email_address = '', birth_date = ''):
        self.username = username
        self.firstname= firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.post_code = post_code
        self.email_address = email_address
        self.birth_Date = birth_date
    #2 Define different method to return the following attributes
    def get_username(self):
          return self.user_name
      
    def get_firstname(self):
          return self.firstname
      
    def get_surname(self):
          return self.surname
      
    def get_house_number(self):
          return self.house_number
      
    def get_street_name(self):
          return self.street_name
      
    def get_post_code(self):
          return self.post_code
      
    def get_email_address(self):
          return self.email_address
      
    def get_birth_date(self):
          return self.birth_date


    #3 Define different methods to edit the following attribute:
    def set_username(self,username = ''):
          self.username = random_username()
          
    def set_firstname(self,firstname = ''):
          self.firstname= names.get_first_name()
          
    def set_surname(self,surname = ''):
          self.surname = names.get_last_name()
          
    def set_house_number(self,house_number = ''):
          self.house_number = random.randint(1,100)
          
    def set_street_name(self,street_name = ''):
          self.street_name = random_street()
          
    def set_post_code(self,post_code = ''):
          self.post_code = random.randint(10000,15000)
          
    def set_email_address(self,email_address = ''):
          self.email_address = random_email()
          
    def set_birth_date(self,birth_date = ''):
          self.birth_date = random_date()



    
    
    
    
        







#4- Creating UserList class:
class UserList:

      #4-1 Defining a constructor to create new object from this class:
      def __init__(self):
        self.user_list = []

      #4-2 Method to add users to the users list:
      def  store_user(self, user):
        self.user_list.append(user)

      #4-3 Method to remove a user from the users list:
      def remove_user(self):
            
       #Checking if the user list is empty:
       if len(self.user_list) == 0:
               print('No user exists in the system. you will be redirected back to the main menu...')
               main()
       else:
        users_to_delete = []
        remove_user = input('Input the firstname of the user you would like removed or type "back" to go back to the main menu: ').title()
        
        #Validating the firstname input:
        while True:
          for user in self.user_list:
            if remove_user == user.firstname:
                users_to_delete.append(user)
                if len(users_to_delete) > 1:
                  delete_all = input('There are more than a user with the same firstname you entered, do you want to delete all? (yes/no):')
                  while True:
                    if delete_all not in ['yes','no']:
                         delete_all = input('Error: Invalid input, please type in yes or no, do you want to delete all? (yes/no):')

                    else:
                        if delete_all == 'yes':
                              for item in users_to_delete:
                                    print('The user with the firstname "',item.firstname,'" has been removed')
                                    self.user_list.remove(item)
                                    #Prompting the user whether they want to take another action or terminate the system:
                                    finalize = input('Would there be anything else? (yes or no)').capitalize()
                                    while True:
                                       if finalize not in ['Yes' , 'No']:
                                             print('Error: Please enter either yes or no')
                                             finalize = input('Would there be anything else? (yes or no)').capitalize()
                                       else:
                                          #System shuts if the answer is "No":
                                          if finalize == 'No':
                                             sys.exit()
                                          else:
                                             #Returning to the main menu when the answer is "Yes":
                                             print('Being directed to the main menu...')
                                             main()
                        else:
                              print('You chose not to delete the users, returning back to the main menu ...')
                              main()
                else:
                      for item in users_to_delete:
                        print('The user with the firstname "',item.firstname,'" has been removed')
                        self.user_list.remove(user)
                        #Prompting the user whether they want to take another action or terminate the system:
                        finalize = input('Would there be anything else? (yes or no)').capitalize()
                        while True:
                          if finalize not in ['Yes' , 'No']:
                               print('Error: Please enter either yes or no')
                               finalize = input('Would there be anything else? (yes or no)').capitalize()
                          else:
                               #System shuts if the answer is "No":
                               if finalize == 'No':
                                  sys.exit()
                               else:
                                  #Returning to the main menu when the answer is "Yes":
                                  print('Being directed to the main menu...')
                                  main()

                                  
            #Returning to the main menu when an input of "back" is given:                  
          if remove_user == 'Back':
              print('Being directed to the main menu...')
              main()

            #The user is prompted to enter the correct input by showing them an error message:
          else:      
              remove_user = input('Error: Please enter a valid firstname to remove or "back" to go back to the main menu: ').title()
              
            

                  
             


      
                        
                                  
                            
                            
                            
            
      #4-4 Method to check how many users are in the users list:
      def active_user(self):
            
            print ('There are',len(self.user_list),'users in the system currently.')
            #Prompting the user whether they want to take another action or terminate the system: 
            finalize = input('Would there be anything else? (yes or no)').capitalize()
            while True:
               if finalize not in ['Yes' , 'No']:
                   print('Error: Please enter either yes or no')
                   finalize = input('Would there be anything else? (yes or no)').capitalize()
               else:
                   #System shuts if the answer is "No":
                   if finalize == 'No':
                     sys.exit()
                   else:
                     #Returning to the main menu when the answer is "Yes":
                     print('Being directed to the main menu...')
                     main()



      #4-5 Method to return all of the user's details after entering their username:
      def user_details(self):

          user_name = input('Please input the username you would like their details displayed or type "Back" to go back to the main menu: ')
          #Validating the username input:
          while True:
            #Looping through the self.user_list to find a username match:
            for user in self.user_list:
              #When a match is found, the details of that user get displayed:
              if user_name == user.username:
                   print('\nUser details:')
                   print('\nUsername:',user.username,'\nFirstname:',user.firstname,'\nSurname:',user.surname,'\nHouse Number:',user.house_number,
                              '\nStreet Name:',user.street_name,'\nPost Code:',user.post_code,'\nEmail Address:',user.email_address,'\nBirth Date:',user.birth_date)
                   
                   #Prompting the user whether they want to take another action or terminate the system:         
                   finalize = input('Would there be anything else? (yes or no)').capitalize()
                   while True:
                     if finalize not in ['Yes' , 'No']:
                          print('Error: Please enter either yes or no')
                          finalize = input('Would there be anything else? (yes or no)').capitalize()
                     else:
                         #System shuts if the answer is "No":
                         if finalize == 'No':
                               sys.exit()
                         else:
                               #Returning to the main menu when the answer is "Yes":
                               print('Being directed to the main menu...')
                               main()
              #User gets directed back to the main menu when "Back" input is entered:
            if user_name == 'Back':
                   print('Being directed to the main menu ...')
                   main()
              #In case of any other invalid input the user is prompt to enter a valid input, either "back" or a valid username:
            else:
                   user_name = input('Error: Please enter a username to show its details or "back" to go back to the main menu: ')

          
      #EXTRA (2): Editing a user's first name, surname, house number, street name, and post code:
      def edit_user(self):
         #Validating if the user list is empty:
         if len(self.user_list) == 0:
               print('No user exists in the system yet. you will be redirected back to the main menu...')
               main()
         else:
          #Asking for the user's firstname we would like to edit:
          user_name = input("What is the username you are trying to edit? or type 'Back' to go back to the main menu ")
          while True:
           for user in self.user_list:
              if user_name == user.username:
                   #Displaying the user's details before editting:
                   print('\nThe User Details are:')
                   print('\nUsername:',user.username,'\nFirstname:',user.firstname,'\nSurname:',user.surname,'\nHouse Number:',user.house_number,
                  '\nStreet Name:',user.street_name,'\nPost Code:',user.post_code,'\nEmail Address:',user.email_address,'\nBirth Date:',user.birth_date)

                   #Displaying the attributes which have been edited using the setters and the helping functions from section (2):
                   print('\nThe firstname has been edited to:\n')
                   user.set_firstname()
                   print(user.firstname,'\n')
                   
                   print('The surname has been edited to:\n')
                   user.set_surname()
                   print(user.surname,'\n')
     
                   print('The house number has been edited to:\n')
                   user.set_house_number()
                   print(user.house_number,'\n')
      
                   print('The street name has been edited to:\n')
                   user.set_street_name()
                   print(user.street_name,'\n')
      
                   print('The post code has been edited to:\n')
                   user.set_post_code()
                   print(user.post_code,'\n')
                  
                   #Prompting the user whether they want to take another action or terminate the system:
                   finalize = input('Would there be anything else? (yes or no)').capitalize()
                   while True:
                    if finalize not in ['Yes' , 'No']:
                      print('Error: Please enter either yes or no')
                      finalize = input('Would there be anything else? (yes or no)').capitalize()
                    else:
                     #System shuts if the answer is "No":
                     if finalize == 'No':
                         sys.exit()
                     else:
                      #Returning to the main menu when the answer is "Yes":
                      print('Being directed to the main menu...')
                      main()
                           
                  #Returning to the main menu when an input of "back" is given:
         if user_name == 'Back':
              print('Being directed to the main menu ...')
              main()

         #The user is prompted to enter the correct input by showing them an error message:
         else:
              user_name = input('Error: Please enter a username to edit its user or "Back" to go back to the main menu: ')
      

      

      #4-6 Method to show the details of all users who are currently in the system:
      def showuser(self):
         if len(self.user_list) == 0:
                 print('The library system has no users in it currently, please add some users using option (1) in the main menu!')
                 main()
         else:
           count = 1
           for user in self.user_list:
              print('\nUser', count,'details: ')
              print('\nUsername:',user.username,'\nFirstname:',user.firstname,'\nSurname:',user.surname,'\nHouse Number:',user.house_number,
                  '\nStreet Name:',user.street_name,'\nPost Code:',user.post_code,'\nEmail Address:',user.email_address,'\nBirth Date:',user.birth_date)
              count += 1

           #Prompting the user whether they want to take another action or terminate the system:
           finalize = input('Would there be anything else? (yes or no)').capitalize()
           while True:
               if finalize not in ['Yes' , 'No']:
                  print('Error: Please enter either yes or no')
                  finalize = input('Would there be anything else? (yes or no)').capitalize()
               else:
                  #System shuts if the answer is "No":
                  if finalize == 'No':
                      sys.exit()
                  else:
                      #Returning to the main menu when the answer is "Yes":
                      print('Being directed to the main menu...')
                      main()




      #4-7 Method to help iterate through the user list:
      def __getitem__(self, index):
        return self.user_list[index]
                    

            
            





#5- Creating Loans class:

#This global variable will help returning loaned books to the book list:
global archive
archive = []

class Loan():
      #5-1 Defining a constructor to create new object from this class:
      def __init__(self):
            self.loan_list = []
            self.book_list = book_list
            self.user_list = user_list
      #5-2 Method for borrowing a book:
      def borrow_book(self):
            #Asking for the title of the book to borrow:
            pair = []
            book = input('what is the title of the book you would like to borrow? or type "Back" to go back to the main menu: ').title()
            #input validation:
            while True:
              for item in self.book_list:
                if book == item.title:
                      #Declaring a variable 'item1' for later use when we choose to remove the book from the book list and append it to the loan list:
                      item1 = item
                      #Asking for the username to have the book assigned to it:
                      user = input('Who should this book be assigned to? please enter a username or type "Back" to go back to the main menu: ')
                      #input validation:
                      while True:
                        for item2 in self.user_list:
                          if user == item2.username:
                                  #Borrowing a book (adding to the loan list) and removing the book from the book list:
                                   borrow_date = datetime.datetime.now()
                                   pair.append(user)
                                   pair.append(book)
                                   pair.append(borrow_date)
                                   self.loan_list.append(pair)
                                   self.book_list.remove_book2(item1)
                                   archive.append(item)
                                   
                                   print('The book titled "',book,'" has been borrowed by the user with the username: ', user,'.')
                                   finalize = input('Would there be anything else? (yes or no)').capitalize()
                                   while True:
                                      if finalize not in ['Yes' , 'No']:
                                         print('Error: Please enter either yes or no')
                                         finalize = input('Would there be anything else? (yes or no)').capitalize()
                                      else:
                                         #System shuts if the answer is "No":
                                         if finalize == 'No':
                                             sys.exit()
                                         else:
                                              #Returning to the main menu when the answer is "Yes":
                                              print('Being directed to the main menu...')
                                              main()

                                              
                          #Returning to the main menu when an input of "back" is given:              
                        if user == 'Back':
                              print('Being directed to the main menu...')
                              main()

                          #The user is prompted to enter the correct input by showing them an error message:   
                        else:
                              user = input('Error: Please enter a valid username to remove or "Back" to go back to the main menu: ')
                   
                #action when user chooses to return to the main menu:                 
              if book == 'Back':
                    print('Being directed to the main menu...')
                    main()

              else:
                    book = input('Error: Please enter a valid book title to borrow or "Back" to go back to the main menu.').title()

                    
                     
      #5-3 Method for returning a borrowed book:
      def return_book(self):
        
        if len(self.loan_list) == 0:
               print('No user has borrowed a book yet. you will be redirected back to the main menu...')
               main()
        else:
            #Asking for the title of the book to be returned:
            book_title = input('what is the title of the book you would like to return? or type "back" to go back to the main menu: ').title()
            #input validation:
            while True:
              for loan in self.loan_list:
                #Checking if the input book title is present in the loan_list:
                if book_title == loan[1]:
                         print('The book titled' ,loan[1], 'is indeed borrowed, let us identify you first to complete the return process.')
                         #Asking for the username who has borrowed the book:
                         user_name = input('To whom was the book assigned to? please enter a username or "back" to go back to the main menu: ')
                         #Declaring a variable 'loan1' for later use when we choose to remove the book from the loan list and append it to the book list:
                         loan1 = loan
                         #input validation
                         while True:
                            for user in self.loan_list:
                               if user_name == user[0]:
                                    #Returning the book to the books list and removing it from the loan list:
                                    self.loan_list.remove(loan1)
                                    for item in archive:
                                      if item.title == book_title:
                                       self.book_list.store_book(item)
                                    print('The book titled "',book_title,'" has been returned successfully.')

                                    #Prompting the user whether they want to take another action or terminate the system:
                                    finalize = input('Would there be anything else? (yes or no)').capitalize()
                                    while True:
                                        if finalize not in ['Yes' , 'No']:
                                           print('Error: Please enter either yes or no')
                                           finalize = input('Would there be anything else? (yes or no)').capitalize()
                                        else:
                                           #System shuts if the answer is "No":
                                           if finalize == 'No':
                                              sys.exit()
                                           else:
                                              #Returning to the main menu when the answer is "Yes":
                                              print('Being directed to the main menu...')
                                              main()



                               #action when user chooses to return to the main menu:  
                            if user_name == 'Back':
                                 print('Being directed to the main menu...')
                                 main()

                               #The user is prompted to enter the correct input by showing them an error message:
                            else:
                                 user_name = input('Error: Please enter a valid username to remove or "back" to go back to the main menu: ')
                   
                #Returning to the main menu when an input of "back" is given:                 
              if book == 'Back':
                    print('Being directed to the main menu...')
                    main()
                    
                #The user is prompted to enter the correct input by showing them an error message:
              else:
                    book = input('Error: Please enter a valid book title to return or "back" to go back to the main menu.').title()
                                   
       
             
                                  
            
      #5-4 Method for number of borrowed books:
      def number_of_borrowed_books(self):

        if len(self.loan_list) == 0:
               print('No user has borrowed a book yet. you will be redirected back to the main menu...')
               main()
        else:
            users = []
            #Looping through the loan_list and appending the usernames to the users list:
            for item in self.loan_list:
                 users.append(item[0])
                 #Counting the number of occurance per user and displaying it:
            print('The following users are borrowing the specificed number of books: \n')
            print(Counter(users))

            #Prompting the user whether they want to take another action or terminate the system:
            finalize = input('\nWould there be anything else? (yes or no)').capitalize()
            while True:
                   if finalize not in ['Yes' , 'No']:
                          print('Error: Please enter either yes or no')
                          finalize = input('Would there be anything else? (yes or no)').capitalize()
                   else:
                      #System shuts if the answer is "No":
                      if finalize == 'No':
                         sys.exit()
                      else:
                         #Returning to the main menu when the answer is "Yes":
                         print('Being directed to the main menu...')
                         main()


               
            
            
      #5-5 Method for borrowed books that need to be returned:
      def overdue_book(self):
           if len(self.loan_list) == 0:
               print('No user has borrowed a book yet. you will be redirected back to the main menu...')
               main()
           else:
             overdue = []
             #Setting an overdue timer of 5 minutes for experimental purposes:
             due = datetime.timedelta(minutes = 5)
             #Checking if the current date is equal to the overdue date:
             for item in self.loan_list:
               if datetime.datetime.now() == item[2] + due:
                  overdue.append(item)
             
               #Returning to the main menu when no book is overdue yet:
               else:
                     print('No book is overdue yet, you still have time, you are sent back to the main menu...')
                     main()

            
             #Displaying overdue books and their details:
             if len(overdue) != 0:
               print('These books are overdue and should be returned: ')
               for item in overdue:
                print('The book titled:',item[1],' which has been borrowed on the date:',item[2],'is overdue and borrowed by the username:',item[0])
               #Prompting the user whether they want to take another action or terminate the system:
                finalize = input('Would there be anything else? (yes or no)').capitalize()
                while True:
                  if finalize not in ['Yes' , 'No']:
                     print('Error: Please enter either yes or no')
                     finalize = input('Would there be anything else? (yes or no)').capitalize()
                  else:
                     #System shuts if the answer is "No":
                     if finalize == 'No':
                        sys.exit()
                     else:
                        #Returning to the main menu when the answer is "Yes":
                        print('Being directed to the main menu...')
                        main()
             #Returning to the main menu when no book is overdue yet:
             else:
                     print('No book is overdue yet, you still have time, you are sent back to the main menu...')
                     main()


          
      #5-6 Method to help iterate through the loan list:
      def __getitem__(self, index):
         return self.loan_list[index]

            


   

#Section Four: Creating book objects, user objects, a book list,
#a user list, a loan list objects, and a main function to run the system:
      
#4.1 Function to create new books:
def create_book():
      book = Books()
      book.set_title()
      book.set_author()
      book.set_year()
      book.set_publisher()
      book.set_available_copies()
      book.set_date()
      return book

#4.2 Function to create new users:
def create_user():
      user = Users()
      user.set_username()
      user.set_firstname()
      user.set_surname()
      user.set_street_name()
      user.set_post_code()
      user.set_email_address()
      user.set_birth_date()
      return user

#4.3 Function to create a new book and add it to the book list:
def add_books():
   book = create_book()
   book_list.store_book(book)
   print('A new book has been created and added to the book list successfully!! \n You will be sent back to the main menu...')
   main()
   
   
#4.4 Function to create a new user and add it to the user list:
def add_users():
   user = create_user()
   user_list.store_user(user)
   print('A new user has been created and added to the user list successfully!! \n You will be sent back to the main menu...')
   main()
      
  

#4.5 Creating book list, user list, and loan list objects:
 
book_list = BookList()

user_list = UserList()

loan_list = Loan()



#4.6 Creating the main function to run the library system:
def main():


      print('\nDear user, welcome to the Online library of Husam.\nPlease choose from the option menu below: ')
      
      print(""" ======LIBRARY MENU=======
   0. To create a book and add it to the book list.
   1. To create a user and add it to the user list.
   2. To Display the current books in the library.
   3. To Display the current users in the library.
   4. Search for a book using: title, author, publisher, or publication date.
   5. Remove a book using: title.
   6. Display total number of books in the library.
   7. Extra: Edit a book's details using: book title.
   8. Remove a user from the system using: firstname.
   9. Display the number of the users in the system.
   10. Display a user's details using: username.
   11. Extra: Edit a user's details using: username.
   12. Borrow a book.
   13 Return a book.
   14. Display number of books a user is borrowing.
   15. Display overdue books that need to be returned.
   16. Exit the system.
                  
                  """)
      choice=input("How may we serve you today? Please choose a number between 0 and 16: \n")
      while True:
              if choice not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14', '15', '16']:
                 print('Error: Invalid input! Please type in only a number between 0 and 16: ')
                 choice = input('\nHow may we serve you today? Please choose a number between 0 and 16: \n')
                 
              else:
                  


                  if choice == '0':
                        add_books()
                        
                  elif choice == '1':
                        add_users()

                  elif choice == '2':
                        print('The Library currently has the following books in it: \n')
                        book_list.showbook()

                  elif choice == '3':
                        print('The Library currently has the following users in it: \n')
                        user_list.showuser()
                  
                  elif choice == '4':
                        book_list.search_book()
                        
                  elif choice == '5':
                        book_list.remove_book()
                        
                  elif choice == '6':
                        book_list.number_of_books()

                  elif choice == '7':
                        book_list.edit_book()     

                  elif choice == '8':
                        user_list.remove_user()
                        
                  elif choice == '9':
                        user_list.active_user()
 
                  elif choice == '10':
                        user_list.user_details()

                  elif choice == '11':
                        user_list.edit_user()
                        
                  elif choice == '12':
                        loan_list.borrow_book()

                  elif choice == '13':
                        loan_list.return_book()

                  elif choice == '14':
                        loan_list.number_of_borrowed_books()

                  elif choice == '15':
                        loan_list.overdue_book()

                        
                  elif choice == '16':
                        sys.exit()

                  break
                        
      



                   
main()
      
