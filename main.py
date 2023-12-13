import os
import csv

# TO DO: Make it so that you dont only need to track hours but other kinds of statistics
# such as assignments turned in or smthing

activities = []

def getActivityNames(activities):
    activityNames = []
    for activity in activities:
        activityNames.append(activity.name)
    return activityNames

def getActivityDetails(activities):
    string = ""
    for activity in activities:
        string += f"\t- Activity name: {activity.name}, {activity.action} {activity.result}.\n"
    return string

def activityWithName(name):
    for activity in activities:
        if activity.name == name:
            return activity

class Activity():
    def __init__(self, name):
        self.name = name
        self.action = ""
        self.result = 0
    def addToResult(self, result):
        self.result += result

def initializeActivities(dataPath):

    if not os.path.isdir(dataPath):
        print("Data path does not exist")
    else:
        # Loop through each file in the directory
        for filename in os.listdir(dataPath):
            # Check if the file is a CSV file
            if filename.endswith(".csv"):
                file_path = os.path.join(dataPath, filename)
                
                # Read the CSV file
                with open(file_path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    
                    # Process each row in the CSV file
                    rowInd = 0
                    for row in reader:
                        # First row is the dates so do not include 
                        if rowInd != 0:
                            # Check if activity exists in activities
                            if row[0] not in getActivityNames(activities):
                                # Create activity and add to list
                                newActivity = Activity(row[0])
                                newActivity.action = row[-2]
                                activities.append(newActivity)

                        rowInd += 1

def addUpStats(dataPath):
    if not os.path.isdir(dataPath):
        print("Data path does not exist")
    else:
        # Loop through each file in the directory
        for filename in os.listdir(dataPath):
            # Check if the file is a CSV file
            if filename.endswith(".csv"):
                file_path = os.path.join(dataPath, filename)
                
                # Read the CSV file
                with open(file_path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    
                    # Process each row in the CSV file
                    for row in reader:
                        # print(f'Activity name = {row[0]}')
                        # Check if activity exists in activities
                        if row[0] in getActivityNames(activities):
                            # add the hours to the activity
                            activityWithName(row[0]).addToResult(float(row[-1]))

if __name__ == "__main__":

    dataPath = "D:/Coding/Time-Tracking/Data"

    initializeActivities(dataPath)
    addUpStats(dataPath)

    print("The following is your time tracking details since the date: November 5th, 2023")
    print(getActivityDetails(activities))
    