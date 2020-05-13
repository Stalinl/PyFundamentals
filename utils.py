person1 = {
  "name": "XYZ",
  "age": 30,
  "country": "ABC"
}


# When '*' is mentioned, the param become Dictionary
# Call this method: save_user(id = 1, name = "Stalin")
def save_user(**users):
    print(users)


# When '*' is mentioned, the param become Tuple
# Call this method: multiply(2, 3, 4)
def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


def lbs_to_kg(weight: float) -> float:
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


def myfunc():
    x = 300

    def myinnerfunc(num):
        return (x * num)
    return myinnerfunc(5)

