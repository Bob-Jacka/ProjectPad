"""
Flask driven web engine
"""
from time import sleep

from flask import (
    Flask,
    render_template,
    redirect,
    url_for, request
)

from core.entities.BotLogger import BotLogger
from core.entities.ProjectManager import Project_manager
from core.other.Utils import safe_log

web_app: Flask = Flask(__name__, static_url_path='/static')
logger: BotLogger = BotLogger()
project_manager: Project_manager


class Cache:
    pass


@safe_log
def run_web_app():
    """
    Entry point to web interface run
    :return:
    """
    global project_manager
    project_manager = Project_manager(logger)
    web_app.run()


##Pages handlers:

@web_app.route('/', methods=['GET'])
def root_page():
    return render_template('home.html')


@web_app.route('/add', methods=['GET', 'POST'])
def add_project():
    """
    Page for adding book to read history
    :return: page
    """
    if request.method == 'POST':
        title = request.form['title']  # required parameter

        sleep(1)  # make user feel comfortable, sleep for 1 sec to guarantee work illusion
        return redirect(url_for('root_page'))
    return render_template('add_project.html')


@web_app.route('/remove', methods=['GET', 'POST'])
def remove_project():
    """
    Page for removing book
    :return: page
    """
    if request.method == 'POST':
        title = request.form['title']  # required parameter

        sleep(1)  # make user feel comfortable, sleep for 1 sec to guarantee work illusion
        return redirect(url_for('root_page'))
    return render_template('remove_project.html')


@web_app.route('/find', methods=['GET', 'POST'])
def find_project():
    """
    Found or not found book in history and get result
    """
    pass


@web_app.route('/about', methods=['GET'])
def about_util_page():
    """
    Page with information about utility
    :return: page
    """
    return render_template('about.html')


@web_app.route('/actions', methods=['GET'])
def actions_page():
    """
    Page with redirect to add book or delete book
    :return: page
    """
    return render_template('actions.html')
