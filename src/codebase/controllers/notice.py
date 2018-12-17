# pylint: disable=W0223,W0221,broad-except
import json
import uuid

from tornado.web import HTTPError

from codebase.web import APIRequestHandler
from codebase.models import Notice
# from eva.conf import settings
from codebase.utils.dayu import DaYuSms


class _BaseNoticeRoleHandler(APIRequestHandler):

    def get_uid(self):
        uid = self.request.headers.get("X-User-Id")
        if not uid:
            raise HTTPError(403, reason="no-x-user-id")
        return uid

    def validate_data(self):
        body = self.get_body_json()
        for k, v in body["template_param"].items():
            if not isinstance(k, str):
                self.fail("字典 key 类型错误")
                return False
            if not isinstance(v, (int, str, list)):
                self.fail("字典 value 类型错误")
                return False
        return True


class SmsHandler(_BaseNoticeRoleHandler):

    def post(self):
        """发送手机验证码
        """
        if not self.validate_data():
            return

        body = self.get_body_json()
        body["business_id"] = uuid.uuid1()

        dayu = DaYuSms.custom_vars(body)
        err = dayu.send()
        if err:
            self.fail(**err)
            return

        notice = Notice(
            phone_numbers=body["phone_numbers"],
            sign_name=body["sign_name"],
            template_code=body["template_code"],
            template_param=json.dumps(body["template_param"]),
            uid=self.get_uid(),
            type="sms"
        )
        self.db.add(notice)
        self.db.commit()
        self.success()
