
from flask_admin import Admin , expose , AdminIndexView 
from flask_admin.contrib.fileadmin import FileAdmin

from app import app , path

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('tables.html')

admin = Admin(app=app,index_view=MyHomeView())

admin.add_view(FileAdmin(path, '/static/', name='Static Files'))