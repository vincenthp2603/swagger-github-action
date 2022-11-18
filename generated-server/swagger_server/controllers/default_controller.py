import connexion
import six

from swagger_server import util


def alarms_controller_create():  # noqa: E501
    """alarms_controller_create

     # noqa: E501


    :rtype: None
    """
    return 'do some magic or not!'


def alarms_controller_delete(id):  # noqa: E501
    """alarms_controller_delete

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!' or None


def alarms_controller_find(ProductInstanceUri=None):  # noqa: E501
    """alarms_controller_find

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ProductInstanceUri = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def alarms_controller_update(id):  # noqa: E501
    """alarms_controller_update

     # noqa: E501

    :param id: 
    :type id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        id = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_controller_get_hello():  # noqa: E501
    """app_controller_get_hello

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def assets_controller_create():  # noqa: E501
    """assets_controller_create

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def assets_controller_delete(ProductInstanceUri):  # noqa: E501
    """assets_controller_delete

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ProductInstanceUri = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def assets_controller_find(ProductInstanceUri=None, PublisherInstanceUri=None):  # noqa: E501
    """assets_controller_find

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: dict | bytes
    :param PublisherInstanceUri: 
    :type PublisherInstanceUri: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ProductInstanceUri = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        PublisherInstanceUri = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def events_controller_create():  # noqa: E501
    """events_controller_create

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def events_controller_find(ProductInstanceUri=None):  # noqa: E501
    """events_controller_find

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        ProductInstanceUri = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
