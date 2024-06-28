'''
Statement for reading and writing CSV files

'''
import csv


class DataAccess:
    '''
    Class for handling data access operations
    '''
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        '''
        Read data from the CSV file
        '''
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                data = []
                for row in reader:
                    data.append({
                        'id': row['id'],
                        'name': row['name'],
                        'attendance': eval(row['attendance']) if row['attendance'] else []  # Convert string back to list
                    })
                return data
        except FileNotFoundError:
            return []

    def write_data(self, data):
        '''
        Writes data to the CSV file
        '''
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'attendance'])
            writer.writeheader()
            for student in data:
                attendance = str(student['attendance'])  # Convert list to string
                writer.writerow({'id': student['id'], 
                                 'name': student['name'], 
                                 'attendance': attendance})
