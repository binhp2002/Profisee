BeSpoked Bikes Sales Tracking application


Overview:
This is a simple applciation that should allow user to track commission and determine quarterly bonus. SalesService_test.py file will contain tests for edge cases of functions inside service.py file.


How to run the application:
Go to your terminal or console then navigate to the "Profisee" directory then run the client.py file. To run tests for edge cases and to make sure the changes in the code don't break anything, navigate to the SalesService_test.py and run it.


Explaination on why I chose Python for this exercise instead of other languages:
Python has a built in, serverless SQL database system called sqlite3. Using sqlite3 would allow me to get start on the projetc faster as I don't have to establish a server to run the application on like with other SQL database system (according to the pdf, hosting a server seems to be an optional requirement but if I have more time, I will use other SQL database system as sqlite has a lot of limitations). 
Also although sqlite3 doesn't allow multiple connections and can't handle a great amount of data like others, I determine that at least for this exercise, those 2 limitations are not as detrimental so sqlite3 is sufficient.


Issue to resolve (Prioritize mandatory requirements, optional requirements will visit if have time):
1) How to find and calculate quarterly salesperson commission to display => email Mr.Cabrera and Mr.Mize for more detail on what is needed to calculate
2) How to reference other entities in Sales (this is important as it will allow me to display list of sales and create a sale) => email Mr.Cabrera and Mr.Mize to elaborate more on Sales entities requirements
3) Optional: Filter by date range on when display a list of sales
4) Optional: Host in Azure


What I believe I have complete:
1) Display a list of salespersons
2) Update a salesperson
3) Display a list of products
4) Update a product
5) Display a list fo Customers
6) Display a list of sales
7) Create a sale


What I was not able to complete and might have done given more time
1) No proper GUI => Make a proper GUI using Tkinter or Kivy (ideal is to move the application away from being console based)

2) Display a list of sales and create a sale functionalities are a little messy => at first, because Sales entities store id that can be used to reference other entities like Products, Salesperson, Customer (using FOREIGN KEY and REFERENCES help to connect different entity to each other by referencing an attribute, like id, of a different entity), I was thiking of creating and using 3 getter methods called get_saleperson_by_id(), get_product_by_id(), and get_customer_by_id() to access and collect the data of the entry that I need and display those data on a table but then I realized given more time, I could have optimized it further by just making a helper function where inside that helper function, I would use INNER JOIN to find the correspond data in a different entity base on the same id value then access the data of another entity that way

3) Improve and/or find a better way to make sure there is no duplicate entry in products and salespersons => currently I am using UNIQUE() to make sure the name and id of each entry are unique from each other and technically it work. Problem is once it see that there is a duplication in entry, the application will exit and we have to run the appliation again which is not ideal. A possible way to fix this is by using try except to catch the error when it occur so we will not exit out of the applicaiton.

4) No functionality to calculate quarterly salesperson commission to display => so far I have manage to find a way to calculate a saleperson commision but a problem with trying to calculate the commision quarterly is figuring out which data entries are within 3 months from each other given the date string => given more time, a possible way that I thought of is to use JULIANDAY() to find the different between the date of 2 entries then if the difference is within 3 month then I will included it in the report else the entry will not be included. Also since there are going to be different salesperson in the sales entity, will have to figure out a way to filter by salesperson name to find his/her commision within 3 months span

5) SalesService class in service.py has too many functions inside, making it hard to read => Split the code into multiple smaller file, with each file representing a class/entity for ease of reading and adding more functionality instead of having them all in service.py file and plan more carefully before writing the code given more time

6) Not enough unit or integration test in SalesService_test.py => make more tests for edge cases to reduce manual test whenever adding/modify functions in the code


Further Improvement that I could have done given more time (not necessarily a requirement):
1) Use more robust database system like MySQL or mongoDB (MySQL and mongoDB allow for multiple connection with server like Azure and can handle greater volume of data)
2) When display a list of something, instead of printing it out like right now, I could make a it print a proper table using pandas library (less lines)


Interesting I realized:
1) With name and id of an entity being 2 most important attributes in defining a record using UNIQUE to wrap name and id like this: UNIQUE(name, id) would prevent an entry from being duplicate as it will make sure that no record have the same name and id
2) Although sqlite3 doesn't have the abilty to make a proper table with gridline but that can be accomplish if you use pandas as well
3) Using FOREIGN KEY and REFERENCES allows me make reference an entity inside of another entities. Could be useful in Sales entity
