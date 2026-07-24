"""
Flask driven web engine
"""
from time import sleep

from flasgger import Swagger
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request
)

from core.data.Swagger_config import template
from core.entities.BotLogger import BotLogger
from core.entities.Project_manager import Project_manager, create_project, create_idea
from core.entities.storage.Kafka_controller import Kafka_controller
from core.entities.storage.Redis_controller import Redis_controller
from core.other.Utils import safe_log

web_app: Flask = Flask(__name__, static_url_path='/static')
swagger: Swagger = Swagger(web_app, template=template)
logger: BotLogger = BotLogger()

# uninitialized entities:
kafka_controller: Kafka_controller = None
cache_controller: Redis_controller = None
project_manager: Project_manager


@safe_log
def run_web_app():
    """
    Entry point to web interface run
    :return: None
    """
    global project_manager
    project_manager = Project_manager(logger)
    web_app.run()


##Pages handlers:

@web_app.route('/', methods=['GET'])
def root_page():
    project_manager.load_projects()
    return render_template('home.html')


@web_app.route('/actions', methods=['GET'])
def actions_page():
    """
    Page with redirect to add book or delete book
    :return: page
    ---
    tags:
      - add
      - projects
    parameters:
      - name: project_title
    responses:
      200:
        description: Page with actions
    """
    return render_template('actions.html')


@web_app.route('/add/project', methods=['GET', 'POST'])
def add_project():
    """
    Page for adding book to read history
    :return: page
    ---
    tags:
      - add
      - projects
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      500:
        description: Error in project adding
    """
    if request.method == 'POST':
        proj_title = request.form['title']  # required parameter
        proj_lang = request.form.getlist('language[]')
        description = request.form['description']
        proj_domain = request.form.getlist('domain[]')

        project = create_project(title=proj_title, description=description,
                                 languages=proj_lang, priority=None, domain=proj_domain)

        project_manager.add_project_or_idea(project)
        sleep(1)  # make user feel comfortable, sleep for 1 sec to guarantee work illusion
        return redirect(url_for('root_page'))
    return render_template('add_project.html')


@web_app.route('/add/idea', methods=['GET', 'POST'])
def add_idea():
    """
    Page for adding book to read history
    :return: page
    ---
    tags:
      - add
      - idea
      - projects
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      500:
        description: Error in project adding
    """
    if request.method == 'POST':
        idea_title = request.form['title']  # required parameter
        description = request.form['description']

        idea = create_idea(title=idea_title, description=description)

        project_manager.add_project_or_idea(idea)

        sleep(1)  # make user feel comfortable, sleep for 1 sec to guarantee work illusion
        return redirect(url_for('root_page'))
    return render_template('add_idea.html')


@web_app.route('/remove', methods=['GET', 'POST'])
def remove_project_or_idea():
    """
    Page for removing book
    :return: page
    ---
    tags:
      - remove
      - projects
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      500:
        description: Error in project adding
    """
    if request.method == 'POST':
        title = request.form['title']  # required parameter
        project_manager.delete_project()

        sleep(1)  # make user feel comfortable, sleep for 1 sec to guarantee work illusion
        return redirect(url_for('root_page'))
    return render_template('remove_project.html')


@web_app.route('/find', methods=['GET', 'POST'])
def find_project():
    """
    Found or not found book in history and get result
    ---
    tags:
      - find
      - projects
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      404:
        description: Error in project adding
    """
    # TODO if status code 200 show detailed project view page
    return render_template('find_project.html')


@web_app.route('/detailed_view/project', methods=['GET', 'PATCH'])
def detailed_project_view_page():
    """
    Detailed project view
    ---
    tags:
      - find
      - view
      - projects
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      404:
        description: Error in project adding
    """
    return render_template('detailed_project_view.html')


@web_app.route('/detailed_view/idea', methods=['GET', 'PATCH'])
def detailed__idea_view_page():
    """
    Detailed project view
    ---
    tags:
      - find
      - view
      - idea
      - projects
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      404:
        description: Error in project adding
    """
    return render_template('detailed_project_view.html')


@web_app.route('/about', methods=['GET'])
def about_util_page():
    """
    Page with information about utility
    :return: page

    ---
    tags:
      - about
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      500:
        description: Error in project adding
    """
    return render_template('about.html')


@web_app.route('/all', methods=['GET'])
def all_projects_page():
    """
    Page with redirect to add book or delete book
    :return: page
    ---
    tags:
      - add
      - projects
    parameters:
      - name: project_title
        status: integer
        required: true
        description: ID пользователя
    responses:
      200:
        description: Project added
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      500:
        description: Error in project adding
    """
    cards = project_manager.get_all_projects()

    return render_template('all.html', cards=cards)
