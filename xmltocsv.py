import xml.etree.ElementTree as ET
import csv

tree = ET.parse('lec01.xml')
root = tree.getroot()
question_list = []

# Store question number in array
for questionNum in root.iter('p'):
    index = questionNum.get('idx')
    question_list.append(index)

print question_list

# write clicker ID, each question, and answers to csv
with open('clickerresponses.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(['Clicker ID'] + question_list)   # csv header

    question = root.find('p')

    # Lists the students' clicker ID's
    clicker_list = []
    for student in question.iter('v'):
        clickerID = student.get('id')
        clicker_list.append(clickerID)

    for clicker in clicker_list:
        answers_list = [clicker]
        for student in root.iter('v'):
            remote = student.get('id')

            if clicker == remote:
                ans = student.get('ans')
                answers_list.append(ans)

        writer.writerow(answers_list)
        print answers_list

print clicker_list
print len(clicker_list)

