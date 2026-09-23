class Person:
  def __init__(self,name,tag):
    self.name = name
    self.__tag = tag
    
  @property
  def tag(self):
    return self.__tag
   
  def info(self):
    print(f"Name: {self.name}")
    print(f"Tag: {self.tag}")
    
class Member(Person):
  def __init__(self,name,tag):
    super().__init__(name,tag)
    
  def info(self):
    print(f"Name: {self.name}")
    print(f"Member Tag: {self.tag}")
    print("Role: Library Member")
    
class Librarian(Person):
  def __init__(self,name,tag):
      super().__init__(name,tag)
      
  def info(self):
    print(f"Name: {self.name}")
    print(f"Librarian Tag: {self.tag}")
    print("Role: Librarian")
    
class Book:
  def __init__(self,title,book_id,author,status):
    self.title = title
    self.book_id = book_id
    self.author = author
    self.__Status = status
    
  @property
  def status(self):
    return self.__Status
  
  @status.setter
  def status(self, value):
    if value in ["Available", "Borrowed"]:
      self.__Status = value
    
  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Book ID: {self.book_id}")
    print(f"author: {self.author}")
    print(f"status: {self.status}")
      
title = input("Enter the title of the book: ")
book_id = input("Enter the book ID: ")
author = input("Enter the author of the book: ")
status = "Available"
c1 = Book(title,book_id,author,status)
c1.display_info()
