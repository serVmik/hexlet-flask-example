def search_user_by_term(search, users):
    result = []
    for user in users:
        if search.lower() in user.get('name').lower():
            result.append(user)
    return result


def add_id(items):
    id = 1
    for item in items:
        if item.get('id', 1) >= id:
            id = item.get('id') + 1
    return id
