#!/usr/bin/python3
"""Create a unique FileStorage by using the variable storage"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
