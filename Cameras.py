import sqlite3

connection = sqlite3.connect('Cameras.sqlite3')

cursor = connection.cursor()

cineCameras = [
                ('RED', 'Komodo', 'S35'), 
                ('Arri', 'Alexa', 'LF'),
                ('BlackMagic Design', 'Ursa 12K', 'S35') ]
cursor.execute(
    ''' DROP TABLE IF EXISTS Cameras''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Cameras (Brand TEXT, Model TEXT, Format TEXT)''')
cursor.executemany('INSERT INTO Cameras VALUES (?,?,?)', cineCameras)
cursor.execute("SELECT * FROM cameras")

camerasList = cursor.fetchall()
print(camerasList)

connection.commit()
connection.close()
