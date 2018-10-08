def split():
    return dict()

def create():
	return dict()

def store():
	submitted_title = request.vars.title
	submitted_body = request.vars.body


	results = db.notes.insert(
         db_title = submitted_title,
         db_body= submitted_body
    )

	if results:
	     return "Note Has Been Added Successfully"
	else:
	     return "Authenticate Error"


def seeNotes():
	notes=db().select(db.notes.ALL)
	return dict(notes=notes)

def edit():
    parameters = request.args
    submitted_id =parameters[0]
    note=db(db.notes.id==submitted_id).select()[0]
    return dict(note=note)

def update():
    submitted_title = request.vars.title
    submitted_body = request.vars.body 
    submitted_id = request.vars.id
    

    if db(db.notes.id == submitted_id).select():

       db(db.notes.id == submitted_id).update(
            db_title =submitted_title,
            db_body =submitted_body
            )

       return 'Note Updated Successfully'
       
    else:
       return 'No Note Found'

def delete():
     parameters = request.args
     submitted_id = parameters[0]

     if db(db.notes.id == submitted_id).select():

        db(db.notes.id == submitted_id).delete()
        return 'Note Deleted Successfully'

     else:
        return 'No Note With the ID found'                   	

def site():
    return dict()


def signup():
    return dict()

def register():
    submitted_firstname = request.vars.firstname
    submitted_lastname = request.vars.lastname 
    submitted_email = request.vars.email
    submitted_password = request.vars.password
    submitted_tel = request.vars.tel
    submitted_radio =request.vars.radio

    results = db.users.insert(
         db_firstname = submitted_firstname,
         db_lastname= submitted_lastname,
         db_email = submitted_email,
         db_password= submitted_password,
         db_tel= submitted_tel,
         db_radio= submitted_radio
    )

    if results:
         return "user signup successfully"
    else:
         return "Authenticate Error"

def login():
    return dict()  

def signin():
    submitted_email   = request.vars.email
    submitted_password = request.vars.password

    if db(db.users.db_email==submitted_email
        and db.users.db_password==submitted_password).count()>0:
        return "User Logged in Successfully"
         
    else:
        return "User Not found. Please Sign up"          

