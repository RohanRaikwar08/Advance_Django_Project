from ..Dau.collage_dao import CollageDAO
from ..service.base_service import BaseService


class CollageService(BaseService):

    def get_dao(self):
        return CollageDAO()