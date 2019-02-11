import glob
import xml.etree.ElementTree as ET
import csv

filenames = sorted(glob.glob('./CSE141FA17/*.xml'))
images = sorted(glob.glob('./CSE141FA17Images/*Q*.jpg'))
print filenames
print images

# print ./CSE141FA17Images/*Q*.jpg

question_list = []      # List to store the question numbers

# Parse each xml file
for filename in filenames:
    tree = ET.parse(filename)
    root = tree.getroot()

    # Store question number in list
    for questionNum in root.iter('p'):
        index = questionNum.get('idx')
        question_list.append(index)

print question_list
print len(question_list)

# Write question number, clicker ID, and answers to csv
with open('cse141fa17clicker.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(['Clicker ID'] + question_list)   # csv header

    clicker_list = []       # List to store the clicker ID's
    for filename in filenames:
        tree = ET.parse(filename)
        root = tree.getroot()

        question = root.find('p')

        # Lists the students' clicker ID's
        for student in question.iter('v'):
            clickerID = student.get('id')
            if clickerID not in clicker_list:
                clicker_list.append(clickerID)

    for clicker in clicker_list:
        answers_list = [clicker]

        for filename in filenames:
            tree = ET.parse(filename)
            root = tree.getroot()

            for student in root.iter('v'):
                remote = student.get('id')

                if clicker == remote:
                    ans = student.get('ans')
                    answers_list.append(ans)

        writer.writerow(answers_list)
        # print answers_list



print clicker_list
print len(clicker_list)
