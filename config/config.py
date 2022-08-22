from database import models


class Config:
    @staticmethod
    def get_table_fields(table):
        table_field_models = {
            "password": {
                "default": models.Password,
                "url": models.Password.url,
                "login": models.Password.login,
                "password": models.Password.password
            }
        }
