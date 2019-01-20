import xml.etree.ElementTree as ET
import csv

tree = ET.parse('lec01.xml')
root = tree.getroot()

# write question number, clicker ID, and answers to csv
with open('clickerresponses.csv', 'w') as r:
    writer = csv.writer(r)
    writer.writerow(['Question', 'Clicker ID', 'Final Response'])   # csv header

    # traverse each question (p block)
    for question in root.iter('p'):
        idx = question.get('idx')

        # traverse each student (v block)
        for student in question.iter('v'):
            clickerID = student.get('id')
            answer = student.get('ans')

            # write each row
            writer.writerow([idx, clickerID, answer])
            print idx, ",", clickerID, ",", answer
