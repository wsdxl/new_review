"""
Author:dxl
Time: 2020/9/1 22:59
File: 生成秘钥.py
"""
from Crypto import Random
from Crypto.PublicKey import RSA
# 伪随机数生成器
random_gen=Random.new().read

# 生成密钥对实例对象：1024是密钥对的长度
rsa=RSA.generate(1024,random_gen)

# 获取私钥，保存到文件
private_pem=rsa.exportKey()
with open('private.pem','wb') as f:
    f.write(private_pem)

# 获取公钥，保存到文件
public_pem=rsa.publickey().exportKey()
with open('public.pem','wb') as f:
    f.write(public_pem)