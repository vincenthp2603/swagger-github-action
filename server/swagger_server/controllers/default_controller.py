import connexion
import six

from swagger_server.models.post_alarm_dto import PostAlarmDto  # noqa: E501
from swagger_server.models.post_asset_dto import PostAssetDto  # noqa: E501
from swagger_server.models.post_event_dto import PostEventDto  # noqa: E501
from swagger_server.models.put_alarm_dto import PutAlarmDto  # noqa: E501
from swagger_server import util

from swagger_server.models.mongodb.schemas.asset import Asset

def alarms_controller_create(body):  # noqa: E501
    """alarms_controller_create

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostAlarmDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def alarms_controller_delete(id):  # noqa: E501
    """alarms_controller_delete

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def alarms_controller_find(ProductInstanceUri=None):  # noqa: E501
    """alarms_controller_find

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: str

    :rtype: None
    """
    return 'do some magic!'


def alarms_controller_update(id, body):  # noqa: E501
    """alarms_controller_update

     # noqa: E501

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PutAlarmDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_controller_get_hello():  # noqa: E501
    """app_controller_get_hello

     # noqa: E501


    :rtype: None
    """
    return 'Hello'


def assets_controller_create(body):  # noqa: E501
    """assets_controller_create

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        #body = PostAssetDto.from_dict(connexion.request.get_json())  # noqa: E501
        post_asset_dto = connexion.request.get_json()
        asset = Asset(**post_asset_dto)
        asset.save()
    return str(asset.id)

def assets_controller_delete(ProductInstanceUri):  # noqa: E501
    """assets_controller_delete

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: str

    :rtype: None
    """
    asset = Asset.objects(ProductInstanceUri=ProductInstanceUri).first()
    asset.delete()
    return str(asset.id)

def assets_controller_find(ProductInstanceUri=None, PublisherInstanceUri=None):  # noqa: E501
    """assets_controller_find

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: str
    :param PublisherInstanceUri: 
    :type PublisherInstanceUri: str

    :rtype: None
    """
    if ProductInstanceUri is not None:
        assets = Asset.objects(ProductInstanceUri=ProductInstanceUri)
    elif PublisherInstanceUri is not None:
        assets = Asset.objects(PublisherInstanceUri=PublisherInstanceUri)
    else:
        assets = []
    return assets.to_json()


def events_controller_create(body):  # noqa: E501
    """events_controller_create

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PostEventDto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def events_controller_find(ProductInstanceUri=None):  # noqa: E501
    """events_controller_find

     # noqa: E501

    :param ProductInstanceUri: 
    :type ProductInstanceUri: str

    :rtype: None
    """
    return 'do some magic!'
