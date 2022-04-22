#Begin Original Code

#List of subjects
subjects = ["physics", "calculus", "poetry", "history"]
#List of grades
grades = [98, 97, 85, 88]

#Creating 2D list combinign subjects and grades
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]
#Adding computer science class and grade
gradebook.append(["Computer Science", 100])
#Adding visual arts class and grade
gradebook.append(["Visual Arts", 93])
#Correcting grade in Visual Arts
gradebook[5][1] = 93+5
#Changing Poetry to pass/Fail
gradebook[2].remove(85)
gradebook[2].append("Pass")
#print(gradebook)

#Creating full gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)