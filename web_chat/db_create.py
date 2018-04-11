#!flask/bin/python
from migrate.versioning import api
from app import db
import config
import os
db.create_all()
if not os.path.exists(config.SQLALCHEMY_MIGRATE_REPO):
    api.create(
        config.SQLALCHEMY_MIGRATE_REPO,
        'database repository')
    api.version_control(
        config.SQLALCHEMY_DATABASE_URI,
        config.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(
        config.SQLALCHEMY_DATABASE_URI,
        config.SQLALCHEMY_MIGRATE_REPO,
        api.version_control(
            config.SQLALCHEMY_MIGRATE_REPO))
