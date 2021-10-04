from flask import request, render_template, redirect, flash
from flask.helpers import url_for
from models.student import Student
from models.course import Course
from models.college import College
from config import app
from SSIShelper import (
    admin_found, 
    verified, 
    save_image,
    add_student_to_db, 
    update_student_record,
    add_course_to_db, 
    update_course_record,
    add_college_to_db, 
    update_college_record)



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        redirect(url_for('homepage'))
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/homepage', methods=['GET', 'POST'])
@app.route('/students', methods=['GET', 'POST'])
def homepage():
    username = request.form.get('username')
    password = request.form.get('password')
    students = Student().get_all()
    courses = Course().get_all()
    colleges = College().get_all()

    if request.method == 'POST ':
        if admin_found(username, password):
            return render_template('students.html', data = [students,courses,colleges])
        else:
            return redirect(url_for('login'))
    else:
        return render_template('students.html', data = [students,courses,colleges])


@app.route('/confirm_identity', methods=['GET', 'POST'])
def confirm_identity():
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('passwordConfirmation')

    if verified(username, password, password2):
        return redirect(url_for('homepage'))
    return render_template('signup.html')


@app.route('/student-search', methods=['GET', 'POST'])
def student_search():
    user_input = request.form.get('user-input')
    result = Student().search(keyword=user_input)
    if len(result) != 0:
        return render_template('students.html', data=[result])
    else:
        return redirect(url_for('homepage'))


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        image = request.files['selected-image']
        try:
            filename = save_image(image, app.config['UPLOAD_PATH'])
        except:
            print("Can't save image")
        
        student = {
            'id': request.form.get('student-id'),
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course'),
            'photo': filename
        }
        add_student_to_db(student)
        flash(f'{student["firstname"]} is added succesfully!', 'info')
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))


@app.route('/update_student/<string:id>', methods=['GET', 'POST'])
def update_student(id):
    if request.method == 'POST':

        student = {
            'id': id,
            'firstname': request.form.get('firstname'),
            'middlename': request.form.get('middlename'),
            'lastname': request.form.get('lastname'),
            'gender': request.form.get('gender'),
            'yearlevel': request.form.get('yearlevel'),
            'course': request.form.get('course')
        }
        update_student_record(student)
        flash(f"{student['firstname']}'s data has been changed succesfully!", 'info')
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('homepage'))


@app.route('/delete_student/<string:id>')
def delete_student(id):
    data = Student().get_student(id)
    Student().delete(id)
    flash(f'{data[0]} deleted from the database.', 'info')
    return redirect(url_for('homepage'))


# Courses routes
@app.route('/courses')
def courses():
    students = Student().get_all()
    courses = Course().get_all()
    colleges = College().get_all()
    return render_template('courses.html', data=[students,courses,colleges])


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course = {
            'code': request.form.get('course-code'),
            'name': request.form.get('course-name'),
            'college': request.form.get('course-college')
        }
        add_course_to_db(course)
        flash(f'{course["code"]} added succesfully!', 'info')
        return redirect(url_for('courses'))
    else:
        return redirect(url_for('courses'))


@app.route('/course-search', methods=['GET', 'POST'])
def course_search():
    user_input = request.form.get('user-input')
    result = Course().search(keyword=user_input)
    if len(result) != 0:
        return render_template('courses.html', data=['', result])
    else:
        return redirect(url_for('courses'))


@app.route('/delete_course/<string:id>')
def delete_course(id):
    try:
        Course().delete(id)
        flash(f'{id} deleted from the database.', 'info')
        return redirect(url_for('courses'))
    except:
        flash(f'{id} cannot be deleted. Students are enrolled in this program', 'info')
        return redirect(url_for('courses'))


@app.route('/update_course/<string:id>', methods=['GET', 'POST'])
def update_course(id):
    if request.method == 'POST':
        course = {
            'code': id,
            'name': request.form.get('course-name'),
            'college': request.form.get('course-college')
        }
        update_course_record(course)
        flash(f"{id} has been updated succesfully!", 'info')
        return redirect(url_for('courses'))
    else:
        return redirect(url_for('courses'))


# Colleges routes
@app.route('/colleges', methods=['GET', 'POST'])
def colleges():
    students = Student().get_all()
    courses = Course().get_all()
    colleges = College().get_statistics()
    departments = College().get_departments()
    return render_template('colleges.html', data=[students,courses,colleges,departments])


@app.route('/add_college', methods=['GET', 'POST'])
def add_college():
    if request.method == 'POST':
        college = {
            'code': request.form.get('college-code'),
            'name': request.form.get('college-name')
        }
        add_college_to_db(college)
        flash(f'{college["code"]} added succesfully!', 'info')
        return redirect(url_for('colleges'))
    else:
        return redirect(url_for('colleges'))


@app.route('/college-search', methods=['GET', 'POST'])
def college_search():
    user_input = request.form.get('user-input')
    result = College().search(keyword=user_input)
    if len(result) != 0:
        return render_template('colleges.html', data=['', '', result])
    else:
        return redirect(url_for('colleges'))


@app.route('/delete_college/<string:id>')
def delete_college(id):
    try:
        College().delete(id)
        flash(f'{id} deleted from the database.', 'info')
        return redirect(url_for('colleges'))
    except:
        flash(f'{id} cannot be deleted. Students or courses are registered under the selected college.', 'info')
        return redirect(url_for('colleges'))


@app.route('/update_college/<string:id>', methods=['GET', 'POST'])
def update_college(id):
    if request.method == 'POST':
        college = {
            'code': id,
            'name': request.form.get('college-name')
        }
        update_college_record(college)
        flash(f"{id} has been updated succesfully!", 'info')
        return redirect(url_for('colleges'))
    else:
        return redirect(url_for('colleges'))




if __name__ == '__main__':
    app.run(debug=True)