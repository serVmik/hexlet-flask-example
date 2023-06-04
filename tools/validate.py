def validate_course(data):
    errors = {}
    if not data.get('title'):
        errors['title'] = "Can't be blank"
    if not data.get('paid'):
        errors['paid'] = "Can't be blank"
    return errors


def validate_user(data):
    errors = {}
    if len(data.get('name', '')) < 4:
        errors['name'] = "Nickname must be grater than 4 characters"
    if not data.get('email'):
        errors['email'] = "Can't be blank"
    return errors


def validate_post(data):
    errors = {}
    if not data.get('title'):
        errors['title'] = "Can't be blank"
    if not data.get('body'):
        errors['body'] = "Can't be blank"
    return errors
