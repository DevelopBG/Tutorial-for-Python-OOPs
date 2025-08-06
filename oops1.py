class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
    
    def travel(self, destination):
        print(f"employee is now traveling to {destination}")


# creating of an object or instance
sam = employee()
destination = 'europe'
travel_plan = sam.travel(destination)
# print(sam.salary)
print(type(sam))




# here we are defining the attribute outside of the class
sam.id = 123


