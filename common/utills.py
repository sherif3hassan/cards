def clean_dict(update: dict):
    update_dict = {
        key: value for key, value in zip(update.keys(), update.values()) if value is not None
    }
    return update_dict
