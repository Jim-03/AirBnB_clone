#!/usr/bin/python3
"""module for models directory"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
