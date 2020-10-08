# the list "students" is already defined
# students = [["Jane", "B"], ["Kate", "B"], ["Alex", "C"], ["Elsa", "A"], ["Max", "B"], ["Chris", "A"]]

new = [person[0] for person in students if person[1] == "A"]
print(new)
