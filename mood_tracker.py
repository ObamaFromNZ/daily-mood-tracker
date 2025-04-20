import csv
from datetime import datetime

#Welcome + Mood Stuff
print('Welcome to your Daily Mood Tracker\n')
mood = input('How are you feeling today? (e.g., happy, tired, anxious):\n>')
note = input('Want to a quick note? (yes/no)\n>')
if note.lower().strip()=='yes':
    note = input('What was on your mind?')
    print('Thank you for sharing your day... I hope this simple reflection was beneficial to you. Take care')
    print('Your mood has been logged successfully to mood_log.csv.')
else:
    note = ""
    print('Your mood has been logged successfully to mood_log.csv.')

#Saving Mood (For Tracking)
with open("mood_log.csv", 'a', newline='') as file:
    date = datetime.now().strftime('%d-%m-%y')
    writer = csv.writer(file)
    writer.writerow([date, mood, note])
