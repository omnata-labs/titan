from titan.app import App

from .database import Database
from .role import Role
from .table import Table
from .warehouse import Warehouse
from .user import User


__version__ = "0.0.1"


LOGO = r"""
    __  _ __          
   / /_(_) /____  ___ 
  / __/ / __/ _ `/ _ \
  \__/_/\__/\_,_/_//_/
   

""".strip(
    "\n"
)
