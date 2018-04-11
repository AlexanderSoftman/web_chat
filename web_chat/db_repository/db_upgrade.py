#!flask/bin/python
from migrate.versioning import api
import config
v = api.db_version(
    config.SQLALCHEMY_DATABASE_URI,
    config.SQLALCHEMY_MIGRATE_REPO)
api.downgrade(
    config.SQLALCHEMY_DATABASE_URI,
    config.SQLALCHEMY_MIGRATE_REPO,
    v - 1)
print("Current database version: %s" % (api.db_version(
    config.SQLALCHEMY_DATABASE_URI,
    config.SQLALCHEMY_MIGRATE_REPO)))
