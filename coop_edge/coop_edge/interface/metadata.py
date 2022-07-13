import hashlib

FAMILY_NAME = 'coop_edge'
FAMILY_VERSION = '0.1'
ADDRESS_PREFIX = hashlib.sha512(FAMILY_NAME.encode('utf-8')).hexdigest()[0:6]
