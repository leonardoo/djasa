"""
Django accounts management made easy.

"""
default_app_config = 'djasa.apps.DjangoAnotherStartAppConfig'

VERSION = (0, 0, 1)

__version__ = '.'.join((str(each) for each in VERSION[:4]))

def get_version():
    """
    Returns string with digit parts only as version.

    """
    return '.'.join((str(each) for each in VERSION[:3]))
