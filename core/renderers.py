from rest_framework.renderers import JSONRenderer


class BaseRenderer(JSONRenderer):
    media_type = "application/json"
