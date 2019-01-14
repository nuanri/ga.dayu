# pylint: disable=R0201

import json
from eva.conf import settings

from codebase.vendor.dysms.aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
# from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
# import uuid
from aliyunsdkcore.profile import region_provider
# from aliyunsdkcore.http import method_type as MT
# from aliyunsdkcore.http import format_type as FT
# import const


class DaYuSms:

    def __init__(self, data):
        self.data = data

    def client(self):
        acs_client = AcsClient(
            settings.ACCESS_KEY_ID,
            settings.ACCESS_KEY_SECRET,
            settings.REGION
        )
        region_provider.add_endpoint(
            settings.PRODUCT_NAME,
            settings.REGION,
            settings.DOMAIN
        )
        return acs_client

    @classmethod
    def custom_vars(cls, data):
        data["phone_numbers"] = ','.join(data["phone_numbers"])
        return cls(data)

    def send(self):
        sms_request = SendSmsRequest.SendSmsRequest()
        # 申请的短信模板编码,必填
        sms_request.set_TemplateCode(self.data["template_code"])
        # 短信模板变量参数
        if self.data["template_param"] is not None:
            sms_request.set_TemplateParam(self.data["template_param"])
        # 设置业务请求流水号，必填。
        sms_request.set_OutId(self.data["business_id"])
        # 短信签名
        sms_request.set_SignName(self.data["sign_name"])
        # 短信发送的号码列表，必填。
        sms_request.set_PhoneNumbers(self.data["phone_numbers"])
        # 调用短信发送接口，返回json
        acs_client = self.client()
        sms_response = acs_client.do_action_with_exception(sms_request)
        res = json.loads(sms_response)
        print("sms_response = ", res)
        err = {}
        if res.get("Code") != 'OK':
            d = {}
            d["message"] = res.get("Message")
            d["data"]["code"] = res.get("Code")
            err.update(d)
        return err
