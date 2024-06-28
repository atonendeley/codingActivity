'''
This is for documenting attendance_records
'''


class AttendanceManager:
    '''
    Class to manage attendance records

    '''

    def __init__(self, data_access):
        self.data_access = data_access

    def add_student(self, student_id, name):
        '''
        Adds a student to the attendance records

        '''
        students = self.data_access.read_data()
        students.append({'id': student_id, 'name': name, 'attendance': []})
        self.data_access.write_data(students)

    def record_attendance(self, student_id, date, present):
        '''
        Records attendance for a student on a specific date

        '''
        students = self.data_access.read_data()
        for student in students:
            if student['id'] == student_id:
                student['attendance'].append({'date': date, 'present': present})
                break
        self.data_access.write_data(students)

    def update_student(self, student_id, new_name):
        '''
        Updates the name of a student identified by student_id
        '''
        students = self.data_access.read_data()
        for student in students:
            if student['id'] == student_id:
                student['name'] = new_name
                break
        self.data_access.write_data(students)

    def view_attendance(self, student_id):
        '''
        Retrieves attendance records for the student identified by student_id

        '''
        students = self.data_access.read_data()
        for student in students:
            if student['id'] == student_id:
                return student['attendance']
        return []

    def get_all_students(self):
        '''
        Retrieves all student records
        '''
        return self.data_access.read_data()
