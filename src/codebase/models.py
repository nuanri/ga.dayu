# pylint: disable=R0902,E1101,W0201,too-few-public-methods,W0613

import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Sequence,
    String,
)

from codebase.utils.sqlalchemy import ORMBase


class Notice(ORMBase):

    __tablename__ = "notice_record"

    id = Column(Integer, Sequence("notice_record_id_seq"), primary_key=True)
    uid = Column(String(64))  # 即 x_user_id
    phone_numbers = Column(String())
    sign_name = Column(String(64))  # 签名
    template_code = Column(String(64))  # 发送短信的模版 code
    template_param = Column(String(512))  # 发送的内容
    type = Column(String(6))  # sms 为手机短信，email 为邮件
    created = Column(DateTime(), default=datetime.datetime.utcnow)
