
from flask import Blueprint, request, render_template, redirect, flash
from flask.helpers import url_for
from ssis.models.student import Student
from ssis.models.course import Course
from ssis.models.college import College
from .utils import add_college_to_db, update_college_record
from . import college

@college.route('/colleges', methods=['GET', 'POST'])
def colleges():
    students = Student().get_all()
    courses = Course().get_all()
    colleges = College().get_statistics()
    departments = College().get_departments()
    return render_template(
        'colleges.html', 
        data=[students,courses,colleges,departments],
        datacount = f'{len(colleges)} Colleges')


@college.route('/colleges/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        college = {
            'code': request.form.get('college-code'),
            'name': request.form.get('college-name')
        }
        add_college_to_db(college)
        flash(f'{college["code"]} added succesfully!', 'info')
        return redirect(url_for('college.colleges'))
    else:
        return redirect(url_for('college.colleges'))


@college.route('/colleges/search', methods=['GET', 'POST'])
def search():
    user_input = request.form.get('user-input')
    field = request.form.get('field')

    if field == 'select':
        result = College().search(keyword=user_input)
    elif field == 'code':
        result = College().search(keyword=user_input, field='code')
    elif field == 'name':
        result = College().search(keyword=user_input, field='name')
    elif field == 'coursecount':
        result = College().search(keyword=user_input, field='coursecount')
    elif field == 'studentcount':
        result = College().search(keyword=user_input, field='studentcount')
    else:
        result = []

    if len(result) != 0:
        return render_template(
            'colleges.html', 
            data=['', '', result],
            datacount = f'Search Result: {len(result)}')
    else:
        return redirect(url_for('college.colleges'))


@college.route('/colleges/delete/<string:id>')
def delete(id):
    try:
        College().delete(id)
        flash(f'{id} deleted from the database.', 'info')
        return redirect(url_for('college.colleges'))
    except:
        flash(f'{id} cannot be deleted. Students or courses are registered under the selected college.', 'info')
        return redirect(url_for('college.colleges'))


@college.route('/colleges/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        college = {
            'code': id,
            'name': request.form.get('college-name')
        }
        update_college_record(college)
        flash(f"{id} has been updated succesfully!", 'info')
        return redirect(url_for('college.colleges'))
    else:
        return redirect(url_for('college.colleges'))