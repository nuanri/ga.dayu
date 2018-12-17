from tornado.web import url

from codebase.controllers import (
    default,
    notice
)


HANDLERS = [
    url(r"/_spec",
        default.SpecHandler),

    url(r"/_health",
        default.HealthHandler),

    # notice

    url(r"/sms",
        notice.SmsHandler),
]
