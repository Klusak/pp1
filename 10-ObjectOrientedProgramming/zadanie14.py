class Ebook():
    def __init__(self):
        self.is_open=False
        self.title="Burn the hell"
        self.author="P.S Herytiera"
        self.page_numbers=679
        self.current_page=463
        self.read=10
    def turn_on(self):
        self.is_open=True
    def turn_off(self):
        self.is_open=False
    def show_status(self):
        if self.is_open==True:
            print(f"Book {self.title} {self.author}, numbers of pages: {self.page_numbers}, current page: {self.current_page} is open")
        else:
            print(f"Book is close")
    def change_page(self):
        if self.is_open==True:
            print(f"You can go to the previous page or the next")
    def title(self,title):
        self.title=title
    def author(self,author):
        self.author=author
    def page_numbers(self,numbers):
        self.page_numbers=numbers
    def current_page(self,number):
        self.current_page=number
    def read(self,number):
        self.current_page+=number
book1=Ebook()
book1.show_status()
book1.turn_on()
book1.show_status()
book1.change_page()
book1.read(10)
        
    