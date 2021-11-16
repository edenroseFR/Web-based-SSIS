from flask import request, render_template, redirect, flash
from flask.helpers import url_for
from ssis.models.student import Student
from ssis.models.course import Course
from ssis.models.college import College
from .utils import add_course_to_db, update_course_record, check_page_limit, check_limit_validity
from . import course
from math import ceil

current_page = 1
course_limit = 5

@course.route('/courses')
def courses() -> str:
    global course_limit

    min_page = request.args.get('min_page')
    max_page = request.args.get('max_page')
    page_limit = check_page_limit(min_page, max_page)
    course_count = str(Course().get_total())
    entered_limit = request.args.get('limit-field')
    if entered_limit == course_count:
        page_limit = 'min-and-max'
    try:
        course_limit = check_limit_validity(int(entered_limit), int(course_count))
    except:
        course_limit = course_limit
    students = Student().get_all(paginate=False)
    courses = Course().get_all(current_page, course_limit)
    colleges = College().get_all(paginate=False)
    return render_template('/course/courses.html', 
                            data=[students,courses,colleges],
                            datacount = course_count,
                            course_limit = course_limit,
                            limit=page_limit)



@course.route('/courses/next', methods=['GET', 'POST'])
def next() -> str:
    global current_page
    course_count = Course().get_total()
    current_page += 1
    limit_page = ceil(course_count/course_limit)
    max_page_reached = current_page == limit_page

    if not max_page_reached:
        return redirect(url_for('course.courses', page_num=current_page))
    else:
        return redirect(url_for('course.courses', page_num=current_page, max_page=True))


@course.route('/courses/prev', methods=['GET', 'POST'])
def prev() -> str:
    global current_page
    max_page_reached = current_page == 1

    if not max_page_reached:
        current_page -= 1
        return redirect(url_for('course.courses', page_num=current_page))
    else:
        current_page = 1
        return redirect(url_for('course.courses', page_num=current_page, min_page=True))


@course.route('/course/add', methods=['GET', 'POST'])
def add() -> str:
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
def search() -> str:
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
        return render_template('/course/courses.html', 
                                data=['', result],
                                datacount = str(len(result)),
                                course_limit = '5')
    else:
        flash(f'No course found', 'info')
        return render_template('/course/courses.html', 
                                data=['', result],
                                datacount = str(len(result)),
                                course_limit = '5')



@course.route('/courses/delete/<string:id>')
def delete(id: str) -> str:
    try:
        Course().delete(id)
        flash(f'{id} deleted from the database.', 'info')
        return redirect(url_for('course.courses'))
    except:
        flash(f'{id} cannot be deleted. Students are enrolled in this program', 'info')
        return redirect(url_for('course.courses'))


@course.route('/courses/update/<string:id>', methods=['GET', 'POST'])
def update(id: str) -> str:
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