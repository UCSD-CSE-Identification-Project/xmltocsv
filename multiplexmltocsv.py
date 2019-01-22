import glob
import xml.etree.ElementTree as ET
import csv

filenames = glob.glob('./CSE141FA17/*.xml')

# write question number, clicker ID, and answers to csv
with open('cse141fa17clicker.csv', 'a') as r:
    writer = csv.writer(r)
    writer.writerow(['Question', 'Clicker ID', 'Final Response'])   # csv header

    # parse each xml file
    for filename in filenames:
        print filename
        tree = ET.parse(filename)
        root = tree.getroot()

        # traverse each question (p block)
        for question in root.iter('p'):
            idx = question.get('idx')

            # traverse each student (v block)
            for student in question.iter('v'):
                clickerID = student.get('id')
                answer = student.get('ans')

                # write each row
                writer.writerow([idx, clickerID, answer])
