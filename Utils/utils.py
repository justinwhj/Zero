def update(old_obj, new_obj):
    for key in old_obj.__dict__:
        if key=="_sa_instance_state":
            continue
        setattr(old_obj, key, getattr(new_obj, key))