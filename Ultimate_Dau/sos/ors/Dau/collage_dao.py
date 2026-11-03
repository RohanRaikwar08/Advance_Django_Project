from .base_dao import BaseDAO
from ..models import Collage
from ..utility.data_validator import DataValidator


class CollageDAO(BaseDAO):

    def get_unique_key(self):
        return "name"

    def get_model(self):
        return Collage

    def get_label(self):
        return "Collage Name"

    def get_where_clause(self, query, params):
        value = params.get("name", "")

        if DataValidator.is_not_null(value):
            query = query.filter(name__istartswith=value)

        return query