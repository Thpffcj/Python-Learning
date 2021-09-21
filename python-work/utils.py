# -*- coding: UTF-8 -*-
# Created by thpffcj on 2021/8/28.
import base64
import datetime

# MTMxMTUwMTczOTg6aGx5MTEyOTEwMjR0cw==
print(base64.b64encode('13115017398:XXXX'.encode("utf-8")))

print(datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + str('Z'))
