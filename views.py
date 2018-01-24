from flask import render_template
from flask_appbuilder import AppBuilder
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from models import UserSettings

class UserSettingsView(ModelView):
    route_base='/usersettings'
    datamodel = SQLAInterface(UserSettings)
    label_columns = { 'photoPath':'Photo Path' }
    edit_columns = { 'photoPath' }
    list_columns = { 'photoPath' }

def register_views(appbuilder):
    # appbuilder.add_view(UserSettingsView(), "User Settings", icon="fa-cog")
    appbuilder.add_link("User Settings", "UserSettings", icon="fa-cog")

