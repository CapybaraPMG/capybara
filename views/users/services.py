from .model import User


def check_user_email(email: str):
    # check if the user email is present in the database
    pass

def save_user_to_db(db, data):
    try:
        user = User(username=data.get("username"), email=data.get("email"), photo=data.get("photo"))
        print(user)
        with db.session.begin():
            db.session.add(user)

        print("User added successfully")
    except Exception as error:
        print(f"this is an error {error}")
        raise error
