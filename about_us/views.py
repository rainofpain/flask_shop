import flask
import flask_login

from Project.config_page import config_page


@config_page(template_name= 'about_us.html')
def render_about_us():
    return {}
    