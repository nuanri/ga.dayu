# pylint: disable=R0902,E1101,W0201,too-few-public-methods,W0613

import datetime

from sqlalchemy_utils import UUIDType
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Sequence,
    String,
)

from codebase.utils.sqlalchemy import ORMBase


class User(ORMBase):
    """
    用户由 AuthN 服务创建并鉴别，本处存储仅是为了关系映射方便
    1. uuid 作为用户 ID 不宜放在其他关联表中，而应该使用 Integer 主键
    2. SQLAlchemy 可以提供方便的查询
    """

    __tablename__ = "authz_user"

    id = Column(Integer, Sequence("authz_user_id_seq"), primary_key=True)
    # TODO: 虽然我们这里认为 user id 是 uuid，当实际情况不一定是
    # 这里可以考虑根据用户配置，动态创建 uid 项，而不是强制使用 uuid
    uuid = Column(UUIDType(), unique=True)
    created = Column(DateTime(), default=datetime.datetime.utcnow)


class Notice(ORMBase):

    __tablename__ = "notice_record"

    id = Column(Integer, Sequence("notice_record_id_seq"), primary_key=True)
    uid = Column(UUIDType())  # 即 x_user_id
    phone_numbers = Column(String())
    sign_name = Column(String(64))  # 签名
    template_code = Column(String(64))  # 发送短信的模版 code
    template_param = Column(String(512))  # 发送的内容
    type = Column(String(6))  # sms 为手机短信，email 为邮件
    created = Column(DateTime(), default=datetime.datetime.utcnow)
