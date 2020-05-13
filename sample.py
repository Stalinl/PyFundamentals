import utils as util
import platform
import datetime

globalVar: str = "WELCOME"
max_numb = util.find_max([23, 45, 100, 56])
lbs = util.kg_to_lbs(63)

print(platform.system())

# Tuple
x = ('AAA', 'BBB', 'CCC')
y = list(x)  # change Tuple to list

dic = {
    "Name": "Stalin",
    "Age": 30,
    "IsMale": True
}

for key, val in dic.items():
    print(key, val)


# Class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f'-> {self.fname}, {self.lname}')


class Student(Person):
    def __init__(self, fname, lname, graduation_year: int = 2015):
        super().__init__(fname, lname)
        self.graduation_year = graduation_year

    def welcome_stud(self):
        print(f"{globalVar} {self.fname} {self.lname} to the class of {self.graduation_year}")

    def raise_error(self):
        raise NotImplementedError()


stud = Student("Stalin", util.person1["name"])
stud.print_name()
stud.welcome_stud()

# Exception Handling
try:
    # x = 5
    print(x)
    raise ArithmeticError()
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Date Time
x = datetime.datetime.now()
print(x.strftime("%d-%m-%Y %I:%M:%S:%f %p"))
print(x.strftime("%c"))

################################################# Sql Server
# import pyodbc as repo
# con = repo.connect("Driver={SQL Server Native Client 11.0};"
#     "Server=(localdb)\MSSQLLocalDB;"
#     "Database=SandSaleMaster;"
#     "Trusted_Connection=yes;")

# cur = con.cursor()
# result = cur.execute("select * from [dbo].[Trucks]")
# for itm in result:
#     print(itm)

################################################# Machine Learning
# import numpy
# import matplotlib.pyplot as plt
# speed = [32,111,138,28,59,77,97]
# mean = numpy.mean(speed)
# median = numpy.median(speed)
# standard_deviation = numpy.std(speed)
# variance = numpy.var(speed)
# percentile = numpy.percentile(speed, 75)

# x = numpy.random.uniform(0.0, 5.0, 250)

# plt.hist(x, 5)
# plt.show()
################################################# Prediction
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # Age of car
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # Speed

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x):
#   return slope * x + intercept

# speed = myfunc(10) # Predict 10 year old car's speed
# print(speed)
