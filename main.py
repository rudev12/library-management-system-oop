import login as log 
role =log.login()

if role =="admin":
    import admin_console
    
elif role =="front_desk":
    import desk_console
    
