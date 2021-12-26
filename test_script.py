# Pagan test

# Import the pagan module.
# pip install this way: pip install -e git+https://github.com/daboth/pagan#egg=pagan
from pagan.pagan import Avatar
import pagan
from io import BytesIO

# Acquire an arbitrary string.
inpt = "connor"

# Use pagan to generate an avatar object based on an input string.
# Optional: You may specify which hash function Pagan should use.
# The functions are available as constants.
# Default: MD5.

# Supported Hashes
# Hash	Constant
# md5	pagan.MD5
# sha1	pagan.SHA1
# sha224	pagan.SHA224
# sha256	pagan.SHA256
# sha384	pagan.SHA384
# sha512	pagan.SHA512
img = pagan.Avatar(inpt, pagan.SHA384)
print(dir(img))
print(type(img.img))
print(img.DEFAULT_FILENAME)

outpath = "output/"
filename = inpt
img.save(outpath, filename)
# Open the avatar image in an
# external image viewer.
img.show()
