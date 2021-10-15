from flask import Blueprint, request, render_template, redirect, flash
from flask.helpers import url_for
from ssis.models.student import Student
from ssis.models.course import Course
from ssis.models.college import College
from .utils import add_course_to_db, update_course_record
from . import course

@course.route('/courses')
def courses():
    students = Student().get_all()
    courses = Course().get_all()
    colleges = College().get_all()
    return render_template(
        'courses.html', 
        data=[students,courses,colleges],
        datacount = f'{len(courses)} Courses')


@course.route('/course/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        course = {
            'code': request.form.get('course-code'),
            'name': request.form.get('course-name'),
            'college': request.form.get('course-college')
        }
        add_course_to_db(course)
        flash(f'{course["code"]} added succesfully!', 'info')
        return redirect(url_for('course.courses'))
    else:
        return redirect(url_for('course.courses'))



@course.route('/courses/search', methods=['GET', 'POST'])
def search():
    user_input = request.form.get('user-input')
    field = request.form.get('field')

    if field == 'select':
        result = Course().search(keyword=user_input)
    elif field == 'code':
        result = Course().search(keyword=user_input, field='code')
    elif field == 'name':
        result = Course().search(keyword=user_input, field='name')
    elif field == 'college':
        result = Course().search(keyword=user_input, field='college')
    else:
        result = []

    if len(result) != 0:
        return render_template(
            'courses.html', 
            data=['', result],
            datacount = f'Search Result: {len(result)}')
    else:
        return redirect(url_for('course.courses'))



@course.route('/courses/delete/<string:id>')
def delete(id):
    try:
        Course().delete(id)
        flash(f'{id} deleted from the database.', 'info')
        return redirect(url_for('course.courses'))
    except:
        flash(f'{id} cannot be deleted. Students are enrolled in this program', 'info')
        return redirect(url_for('course.courses'))


@course.route('/courses/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        course = {
            'code': id,
            'name': request.form.get('course-name'),
            'college': request.form.get('course-college')
        }
        update_course_record(course)
        flash(f"{id} has been updated succesfully!", 'info')
        return redirect(url_for('course.courses'))
    else:
        return redirect(url_for('course.courses'))