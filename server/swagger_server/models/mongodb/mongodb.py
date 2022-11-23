from mongoengine import *

def connect_to_mongodb():
    connect(
        db='api-gateway',
        host='mongodb://admin:admin@localhost:27017'
    )

def create_schema_class_from_swagger_model(swagger_model, schema_class_name):
    base_model = swagger_model()
    swagger_types = base_model.swagger_types
    swagger_attribute_map = base_model.attribute_map
    swagger_inv_attribute_map = { v: k for k, v in swagger_attribute_map.items() }
    schema_template = {
        "meta": {'allow_inheritance': True}
    }
    for key in swagger_types:
        swagger_type =  swagger_types[key]
        attr = swagger_attribute_map[key]
        if swagger_type is str:
            schema_template[attr] = StringField()
        elif swagger_type is int:
            schema_template[attr] = IntField()
        elif swagger_type is float:
            schema_template[attr] = FloatField()
        elif swagger_type is list:
            schema_template[attr] = ListField()
        else:
            schema_template[attr] = DictField()
    
    def constructor(self, dto):
        for key, value in dto.items():
            setattr(self, key, value)


    return type(schema_class_name, (Document,), {
        #"__init__": constructor,
        **schema_template
    })
