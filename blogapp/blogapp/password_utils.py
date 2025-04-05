import bcrypt


def encode_password(password: str) -> str:
    """ encodes the given password to a hashed repr suitable for storage """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def is_correct_password(db_hashed_pw: str, entered_pw: str):
    """ checks if the entered user password is correct """
    return bcrypt.checkpw(entered_pw.encode("utf-8"), db_hashed_pw.encode("utf-8"))
