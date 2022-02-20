from src.dao.dao_miniatures import select
from src.business.utils.tools import *


def get_miniature_bo(field, value, page_len=10, get_all=False):
    result = select(value, field, select_all=get_all)

    return paginate([jsonify_object(row) for row in result], page_len)

