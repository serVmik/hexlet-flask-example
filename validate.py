def validate_course(data):
    errors = {}
    if not data.get('title'):
        errors['title'] = "Can't be blank"
    if not data.get('paid'):
        errors['paid'] = "Can't be blank"
    return errors


def validate_user(data):
    errors = {}
    for key, value in data.items():
        if not value:
            errors[key] = "Can't be blank"
    return errors
