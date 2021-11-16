from flask import request, render_template, redirect, flash
from flask.helpers import url_for
from ssis.models.student import Student
from ssis.models.course import Course
from ssis.models.college import College
from .utils import add_college_to_db, update_college_record
from . import college
from math import ceil

current_page = 1

@college.route('/colleges', methods=['GET', 'POST'])
def colleges() -> str:
    students = Student().get_all(paginate=False)
    courses = Course().get_all(paginate=False)
    colleges = College().get_all(current_page, 5)
    departments = College().get_departments()
    colleges_count = len(colleges)
    return render_template('/college/colleges.html', 
                            data=[students,courses,colleges,departments], 
                            datacount=f'{colleges_count} Colleges'
                           )


@college.route('/colleges/next', methods=['GET', 'POST'])
def next() -> str:
    global current_page
    college_count = College().get_total()
    current_page += 1
    limit_page = ceil(college_count/5)
    max_page_reached = current_page > limit_page

    if not max_page_reached:
        return redirect(url_for('college.colleges', page_num=current_page))
    else:
        current_page -= 1
        return redirect(url_for('college.colleges', page_num=current_page, limit=True))



@college.route('/colleges/prev', methods=['GET', 'POST'])
def prev() -> str:
    global current_page
    college_count = College().get_total()
    current_page -= 1
    max_page_reached = current_page <1

    if not max_page_reached:
        return redirect(url_for('college.colleges', page_num=current_page))
    else:
        current_page = 1
        return redirect(url_for('college.colleges', page_num=current_page, limit=True))



@college.route('/colleges/add', methods=['GET', 'POST'])
def add() -> str:
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
def search() -> str:
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
        return render_template('/college/colleges.html', 
                                data=['', '', result], 
                                datacount= str(len(result)))
    else:
        flash(f'No college found', 'info')
        return render_template('/college/colleges.html', 
                                data=['', '', result], 
                                datacount= str(len(result)))


@college.route('/colleges/delete/<string:id>')
def delete(id: str) -> str:
    try:
        College().delete(id)
        flash(f'{id} deleted from the database.', 'info')
        return redirect(url_for('college.colleges'))
    except:
        flash(f'{id} cannot be deleted. Students or courses are registered under the selected college.', 'info')
        return redirect(url_for('college.colleges'))


@college.route('/colleges/update/<string:id>', methods=['GET', 'POST'])
def update(id: str) -> str:
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