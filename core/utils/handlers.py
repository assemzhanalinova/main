import uuid


def uploaded_filename(filename) -> str:
    """
    rename filename to uuid value

    :params filename: Image/File object
    :type filename: file

    """
    extension = filename.split(".")[-1]
    new_filename = "{}.{}".format(uuid.uuid4(), extension)
    return new_filename
