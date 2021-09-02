from .base import env

if env == "local":
    from .local import *
else: 
    print("product")
    from .product import *
