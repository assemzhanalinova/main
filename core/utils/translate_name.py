from django.utils.translation import gettext_lazy as _


def get_translation_dict_by_choices(object_id, choices):
    """
    translation choices class

    :param object_id: choice class value
    :type: object_id: int/srt

    :param choices: choices class tuple
    :type choices: tuple/dict

    :return: dict/ none
    """
    choices = dict(choices)
    if object_id in choices:
        name = choices[object_id]
        return {"id": object_id, "name": name, "translation": _(name)}

    else:
        return None
