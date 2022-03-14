from flask import request, render_template, redirect, flash, session
from flask.helpers import url_for
from ssis.models.student import Student
from ssis.models.course import Course
from ssis.models.college import College
from . import student
from math import ceil
from .utils import (add_student_to_db,
    update_student_record,
    save_image, 
    delete_image, 
    check_page_limit,
    check_limit_validity)

current_page = 1
student_limit = 5

@student.route('/students', methods=['GET', 'POST'])
def students() -> str:
    global student_limit

    min_page = request.args.get('min_page')
    max_page = request.args.get('max_page')
    page_limit = check_page_limit(min_page, max_page)
    student_count = str(Student().get_total())
    entered_limit = request.args.get('limit-field')
    if entered_limit == student_count:
        page_limit = 'min-and-max'
    try:
        student_limit = check_limit_validity(int(entered_limit), int(student_count))
    except:
        student_limit = student_limit
    students = Student().get_all(current_page, student_limit)
    courses = Course().get_all(paginate=False)
    colleges = College().get_all(paginate=False)
    return render_template('/student/students.html',
        data = [students,courses,colleges],
        datacount = student_count,
        student_limit = student_limit,
        limit = page_limit)



@student.route('/students/next', methods=['GET', 'POST'])
def next() -> str:
    global current_page
    student_count = Student().get_total()
    current_page += 1
    limit_page = ceil(student_count/student_limit)
    max_page_reached = current_page == limit_page

    if not max_page_reached:
        return redirect(url_for('student.students', page_num=current_page))
    else:
        return redirect(url_for('student.students', page_num=current_page, max_page=True))



@student.route('/students/prev', methods=['GET', 'POST'])
def prev() -> str:
    global current_page
    min_page_reached = current_page == 1

    if not min_page_reached:
        current_page -= 1
        return redirect(url_for('student.students', page_num=current_page))
    else:
        current_page = 1
        return redirect(url_for('student.students', page_num=current_page, min_page=True))



@student.route('/students/search', methods=['GET', 'POST'])
def search() -> str:
    if request.method == 'POST':

        user_input = request.form.get('user-input')
        field = request.form.get('field')

        if field == 'select':
            result = Student().search(keyword=user_input)
        elif field == 'id':
            result = Student().search(keyword=user_input, field='id')
        elif field == 'first':
            result = Student().search(keyword=user_input, field='firstname')
        elif field == 'middle':
            result = Student().search(keyword=user_input, field='middlename')
        elif field == 'last':
            result = Student().search(keyword=user_input, field='lastname')
        elif field == 'gender':
            result = Student().search(keyword=user_input, field='gender')
        elif field == 'year':
            result = Student().search(keyword=user_input, field='year')
        elif field == 'course':
            result = Student().search(keyword=user_input, field='course')
        else:
            result = []

        if len(result) != 0:
            return render_template('/student/students.html', 
                                    data=[result],
                                    datacount = str(len(result)),
                                    student_limit = '5',
                                   )
        else:
            flash(f'No student found', 'info')
            return render_template('/student/students.html', 
                                    data=[result],
                                    datacount = str(len(result)),
                                    student_limit = '5',
                                   )
    else:
        return redirect(url_for('student.students'))



@student.route('/students/add', methods=['GET', 'POST'])
def add() -> str:
    if request.method == 'POST':
        image = request.files['selected-image']
        try:
            cloud_link = save_image(image)
        except Exception as e:
            print("Can't save image")
            print(e)
        
        student = {
            'id': request.form.get('student-id'),
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course'),
            'photo': cloud_link
        }
        added = add_student_to_db(student)
        if added:
            flash(f'{student["firstname"]} is added succesfully!', 'success')
        else:
            flash(f'{student["firstname"]} cannot be added. Make sure the ID is unique.', 'info')
        return redirect(url_for('student.students'))
    else:
        courses = Course().get_all(paginate=False)
        colleges = College().get_all(paginate=False)
        return render_template('/student/form.html', 
                                data = [[],courses,colleges])



@student.route('/students/update/<string:id>', methods=['GET', 'POST'])
def update(id: str) -> str:
    if request.method == 'POST':
        image = request.files['selected-image'+id]
        cloud_link = ''
        try:
            cloud_link = save_image(image)
        except Exception as e:
            print("Can't save image")
            print(e)
        
        if cloud_link:
            student = {
            'id': id,
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course'),
            'photo' : cloud_link
            }
            update_student_record(student)
        else:
            student = {
            'id': id,
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course'),
            'photo' : cloud_link
            }
            update_student_record(student)

        flash(f"{student['firstname']}'s data has been changed succesfully!", 'info')
        return redirect(url_for('student.students'))
    else:
        return redirect(url_for('student.students'))



@student.route('/students/delete/<string:id>')
def delete(id: str) -> str:
    data = Student().get_student(id)
    delete_image(id)
    Student().delete(id)
    flash(f'{data[0]} deleted from the database.', 'info')
    return redirect(url_for('student.students'))


