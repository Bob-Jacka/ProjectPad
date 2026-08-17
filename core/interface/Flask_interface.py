"""
Flask driven web engine
"""
from time import sleep
from typing import Any

from common_py_lib.logger.CommonLogger import CommonLogger
from common_py_lib.wrappers.PyWrappers import safe_log
from flasgger import Swagger
from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    jsonify
)

from core.data.Data import Priority
from core.data.Swagger_config import template
from core.entities.Entity_manager import Entity_manager, create_project, create_idea, create_enhancement, create_note

web_app: Flask = Flask(__name__, static_url_path='/static')
swagger: Swagger = Swagger(web_app, template=template)
logger: CommonLogger = CommonLogger()
pm: Any


@safe_log
def run_web_app(entity_manager: Entity_manager):
    """
    Entry point to web interface run
    :return: None
    """
    global pm
    pm = entity_manager
    pm.load_projects()

    web_app.run(host='0.0.0.0', port=5000, debug=True)


##Pages handlers:

@web_app.route('/', methods=['GET'])
def root_page():
    return render_template('home.html')


@web_app.route('/profile', methods=['GET'])
def profile_page():
    """
    Page with redirect to profile page
    :return: page
    ---
    tags:
      - profile
    responses:
      200:
        description: Page with profile data
    """
    return render_template('profile.html')


@web_app.route('/actions', methods=['GET'])
def actions_page():
    """
    Page with redirect to add book or delete book
    :return: page
    ---
    tags:
      - add
      - remove
      - projects
      - idea
    responses:
      200:
        description: Page with actions
    """
    return render_template('actions.html')


@web_app.route('/ai', methods=['GET'])
def ai_page():
    """
    Page with redirect to ai page, where you can ask ai about your projects
    :return: page
    ---
    tags:
      - ai
      - projects
    responses:
      200:
        description: Page with actions
    """
    return render_template('ai.html')


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
        status: project status
        description: project description
    responses:
      200:
        description: Project added
      500:
        description: Error in project adding
    """
    if request.method == 'POST':
        proj_title = request.form['title']  # required parameter
        proj_lang = request.form.getlist('language[]')
        description = request.form['description']
        proj_domain = request.form.getlist('domain[]')

        project = create_project(title=proj_title, description=description,
                                 languages=proj_lang, priority=None, domains=proj_domain)

        pm.add_project_or_idea(project)
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
      - name: idea title
        description: idea description
    responses:
      200:
        description: Project added
      500:
        description: Error in project adding
    """
    if request.method == 'POST':
        idea_title = request.form['title']  # required parameter
        description = request.form['description']

        idea = create_idea(title=idea_title, description=description)

        pm.add_project_or_idea(idea)

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
      500:
        description: Error in project adding
    """
    if request.method == 'POST':
        title = request.form['title']  # required parameter
        pm.delete_project()

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


@web_app.route('/detailed_view/project/<str>', methods=['GET', 'PATCH'])
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
    responses:
      200:
        description: page received
      500:
        description: Error in page receiving
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
    responses:
      200:
        description: page received
      500:
        description: Error in page receiving
    """
    cards = pm.get_all_projects()

    return render_template('all.html', cards=cards)


@web_app.get('/status')
def get_server_status():
    print('Connection!')
    return {"status": "ok"}


@web_app.route('/mobile_connect', methods=['POST'])
def mobile_connect():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    obj_type = data.get("type")

    if obj_type == "Note":
        note = create_note()
        pm.add_project_or_idea(note)
    elif obj_type == "Enhancement":
        enhancement = create_enhancement(data['description'], data['created_at'])
        pm.add_project_or_idea(enhancement)
    elif obj_type == "Idea":
        idea = create_idea(data['title'], data['description'])
        pm.add_project_or_idea(idea)
    elif obj_type == "Project":
        project = create_project(data['title'], data['description'], [], Priority.HIGH, [])
        pm.add_project_or_idea(project)
    else:
        return jsonify({"error": f"Unknown type: {obj_type}"}), 400

    return jsonify({
        "post": "ok"
    }), 200
