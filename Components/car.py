class Car:
    def __init__(self,company: str,model: str,year: str):
        self.company = company
        self.model = model
        self.year = year
    def get_details(self)-> str:
        details = str(self.year) + ' ' + self.company + ' ' + self.model
        return details
