#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from swagger_server.models.mongodb.mongodb import connect_to_mongodb


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'IIoT Portal API Gateway'}, pythonic_params=False)
    connect_to_mongodb()
    app.run(port=8080)


if __name__ == '__main__':
    main()
