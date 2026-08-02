import database as db
import login as log 

db_manager = db.Database()
db_manager.create_table()

role = log.login()

if role == "admin":
    import admin_console
    
elif role == "front_desk":
    import desk_console
