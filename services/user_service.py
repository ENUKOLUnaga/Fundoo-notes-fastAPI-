from models.user_models import User
from utils.loggers import logger

# CREATE
def create_user(db, user):
    logger.info(f"Creating user: {user.email}")

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        contact_no=user.contact_no
    )

    db.add(new_user)
    db.commit()

    logger.info("User created successfully")
    return new_user


# READ ALL
def get_users(db):
    logger.info("Fetching all users")
    return db.query(User).all()


# READ ONE
def get_user(db, user_id):
    logger.info(f"Fetching user with id: {user_id}")
    return db.query(User).filter(User.id == user_id).first()


# UPDATE
def update_user(db, user_id, user):
    logger.info(f"Updating user id: {user_id}")

    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user:
        db_user.name = user.name
        db_user.contact_no = user.contact_no
        db_user.is_active = user.is_active
        db.commit()
        logger.info("User updated")
        return {"message": "User updated"}

    logger.error("User not found")
    return {"message": "User not found"}


# DELETE
def delete_user(db, user_id):
    logger.warning(f"Deleting user id: {user_id}")

    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user:
        db.delete(db_user)
        db.commit()
        logger.info("User deleted")
        return {"message": "User deleted"}

    logger.error("User not found")
    return {"message": "User not found"}