from app import create_app
from flask_script import Manager,Shell,Server
from  flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')



migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)
@manager.command

if __name__ == '__main__':
    manager.run(debug=True)