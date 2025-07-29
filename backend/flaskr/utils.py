from werkzeug.security import generate_password_hash, check_password_hash


def generate_password(password):
    # Use pbkdf2:sha256 which is widely supported
    return generate_password_hash(password, method='pbkdf2:sha256', salt_length=10)


def check_password(password_hash, password):
    return check_password_hash(password_hash, password)
