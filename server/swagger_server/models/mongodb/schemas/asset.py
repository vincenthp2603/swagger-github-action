from swagger_server.models.mongodb.mongodb import create_schema_class_from_swagger_model
from swagger_server.models.post_asset_dto import PostAssetDto

Asset = create_schema_class_from_swagger_model(PostAssetDto, 'Asset')