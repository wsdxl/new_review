"""
Author:dxl
Time: 2020/9/2 8:00
File: 加密时间戳获取.py
"""
import time
from common.handle_sign import HandleSign
time_stamp=int(time.time())

# token值
token = "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjI2NSwiZXhwIjoxNTc0NjY3MjMzfQ.ftrNcidmk_zxwl0" \
        "wzdhE5_39bsGlILoSSoTCy043fjhbjhCFG4FwCnOj4iy5svbDlSbgCJM3qRa1zsXJLJmH4A"
#
# s=token[:50]+str(time_stamp)
# print(s)
# sign=HandleSign.to_encrypt(s)
# print(sign)

sign=HandleSign.generate_sign(token)
print(sign)