Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'Kfir Jet')
m.hexdigest()
'2d6d73e3e4bbbb2559bfd03b77d2f0949a9d281e5374a3ae2ce47a7e02ec09e2'
