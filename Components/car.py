class Car:
    def __init__(self,company,model,year):
        self.company = company
        self.model = model
        self.year = year
    def get_details(self):
        details = str(self.year) + ' ' + self.company + ' ' + self.model
        return details
