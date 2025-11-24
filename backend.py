'''class Category:
    def __init__(self):
        self.item_list = []
        
class fontpack:
    from tkinter import Tk
    from tkinter.font import families
    root = Tk()
    font_family_list = families()
    def __init__(self):
        self.font_family = "Arial"
        self.font_size = "10"
        self.font_data = self.font_family + " " + self.font_size
    
    @staticmethod
    def font_family_list():
        from tkinter import Tk
        from tkinter.font import families
        root = Tk()
        family_list = families()
        for index, family in enumerate(family_list):
            print(index+1, family)


class numeric_value:
    def __init__(self):
        self.value = 10
    
    def add(self):
        self.add = 1
        self.value += self.add

    def subtract(self):
        self.sub = 1
        self.value -= self.sub

class details:
    value = None
    def inserter(data):
        details.value = data

class price:
    amount = None
    @staticmethod
    def insert(value):
        try:
            try:
                value = int(value)
            except:
                value = float(value)
            finally:
                price.amount = value
        except:
            return "Invalid Amount"

class mail:
    sender_mail = ""
    receiver_mail = ""
    # def sender(email):
    #     if email
'''
from GET_path import path
def insert_data(category, detail, price): # Writing Data got from user in a local file
    if not price.isdigit(): # Checking Price Value Format Error
        return "Price Error"
    from time import localtime, strftime # Getting Date
    date = strftime("%A %d/%m/%y %B %Y", localtime())
    # Items
    Item = {"category" : category,
            "detail" : detail,
            "price" : price,
            "date" : date}
    # if    # TO be worked
    with open(path()+"Storage.txt", 'a') as file: # Writing in file
        file.write(f"{Item["date"]},{Item["category"]},{Item["detail"]},{Item["price"]}\n")
    sorter(get_data())

def get_data(want = ""): # Getting / Reading Data from file
    with open(path()+"Storage.txt", 'r') as file:
        row = file.read().split("\n")[0:-1] # reads data and separate lines and get them in list form
        if want == "date":
            data = row[-1]
            return data[0]
        else:
            data = row
            return data

def sorter(database): # Sorter (in month then day)
    months = []
    mon1 = None
    for row in database:
        if not ':' in row:
            # It takes month of current and next receit if they dont match then the next month is add in list
            mon2 = row.split(",")[0].split(" ")[2]
            if mon1 != mon2:
                months.append(mon2)
            mon1 = mon2
    i = 0
    for ind,month in enumerate(months):
        while i < len(database):
            if not ':' in database[i]:
                # Check if month is in the receit if yes then adds adn month iteration moves to next month
                if database[i].split(" ")[2] == month: 
                    database.insert(i, months[ind]+":")
                    i += 1 # This is since we are adding an element so the position of current elements and onwards moves 1 further.
                    break
            i += 1
    with open(path()+'Storage.txt', 'w') as file:
        file.write("\n".join(database)+"\n")

# def show(base):
#     for i in base:
#         print(i)

class Price:
    def sumlist(entlist):
        total = 0
        for item in entlist:
            total += float(item)
        return total

    def get(data):
        '''Extracts the prices according to month in list form.'''
        price_list = []
        for line in data:
            line = line.split(',')
            try:# Adds prices to the last month added in newlist
                price_list[-1].append(line[3])
            except IndexError:# Gets months and create a inlist with month as 1st item
                if line[0].strip() != "": # To ignore empty lines
                    price_list.append(line)
        print(price_list, end="\n\n")
        finale = []
        for i in range(len(price_list)):
            total = Price.sumlist(price_list[i][1:])
            finale.append([price_list[i][0], total])
        print(finale)
        return finale

if __name__ == "__main__":
    Price.get(get_data())
    pass