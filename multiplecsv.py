import glob
import xml.etree.ElementTree as ET
import csv

filename = glob.glob('./CSE141SP17/L1706081358.xml')

substringFile = ''
for xml_file in filename:
    substringFile = xml_file.split('/')[2].split('.')[0]

tree = ET.parse('./CSE141SP17/L1706081358.xml')
root = tree.getroot()
question_list = []

# Store question number in array
for questionNum in root.iter('p'):
    index = questionNum.get('idx')
    question_list.append(substringFile + "_Q" + index)

# write clicker ID, each question, and answers to csv
with open(substringFile + '.csv', 'w') as writeFile:
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
