def exclude_keys(data: dict):
    if 'submit' and 'csrf_token' in data.keys():
        data.pop('submit')
        data.pop('csrf_token')
    return data
