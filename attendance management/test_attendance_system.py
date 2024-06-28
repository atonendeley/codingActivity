'''
This module provides a framework for creating, organising
and running automated tests to verify code functionality.

'''
import unittest
import os
from attendance_records import AttendanceManager
from data_access import DataAccess


class TestAttendanceManager(unittest.TestCase):
    '''
    This tests attendance

    '''
    def setUp(self):
        # Using a temporary file for testing
        self.data_access = DataAccess('test_students.xlsx')
        self.attendance_manager = AttendanceManager(self.data_access)

    def tearDown(self):
        os.remove('test_students.xlsx')  # Clean up the test file after each test

    def test_add_student(self):
        '''
        This test addition of students

        '''
        # Arrange
        student_id = '1'
        name = 'John Doe'
        # Act
        self.attendance_manager.add_student(student_id, name)
        # Assert
        students = self.attendance_manager.get_all_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], name)

    def test_record_attendance(self):
        '''
        This tests record for students
        '''
        # Arrange
        self.attendance_manager.add_student('1', 'John Doe')
        # Act
        self.attendance_manager.record_attendance('1', '2024-05-19', True)
        # Assert
        students = self.attendance_manager.get_all_students()
        self.assertEqual(len(students[0]['attendance']), 1)
        self.assertEqual(students[0]['attendance'][0]['date'], '2024-05-19')
        self.assertTrue(students[0]['attendance'][0]['present'])

    def test_update_student(self):
        '''
        This tests students update
        '''
        # Arrange
        self.attendance_manager.add_student('1', 'John Doe')
        # Act
        self.attendance_manager.update_student('1', 'John Smith')      
        # Assert
        students = self.attendance_manager.get_all_students()
        self.assertEqual(students[0]['name'], 'John Smith')

    def test_view_attendance(self):
        '''
        This tests view of students attendance        
        '''
        # Arrange
        self.attendance_manager.add_student('1', 'John Doe')
        self.attendance_manager.record_attendance('1', '2024-05-19', True)
        # Act
        attendance = self.attendance_manager.view_attendance('1')        
        # Assert
        self.assertEqual(len(attendance), 1)
        self.assertEqual(attendance[0]['date'], '2024-05-19')
        self.assertTrue(attendance[0]['present'])

    def test_get_all_students(self):
        '''
        Test retrieving all student records        
        '''
        # Arrange
        self.attendance_manager.add_student('1', 'John Doe')
        self.attendance_manager.add_student('2', 'Jane Doe')
        # Act
        students = self.attendance_manager.get_all_students()
        # Assert
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]['name'], 'John Doe')
        self.assertEqual(students[1]['name'], 'Jane Doe')


if __name__ == '__main__':
    unittest.main()
