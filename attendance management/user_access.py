'''
This section holds record for attendance and data access

'''
from attendance_records import AttendanceManager
from data_access import DataAccess


def main():
    '''
    Main function to demonstrate the usage 
    of the attendance management system

    '''
    data_access = DataAccess('students.xlsx')
    attendance_manager = AttendanceManager(data_access)
    # Example usage
    attendance_manager.add_student('1', 'John Doe')
    attendance_manager.record_attendance('1', '2024-05-19', True)
    attendance_manager.update_student('1', 'John Smith')
    print(attendance_manager.get_all_students())
    print(attendance_manager.view_attendance('1'))


if __name__ == "__main__":
    main()
