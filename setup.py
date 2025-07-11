# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 00:15:03 2025

@author: Owner
"""
from setuptools import setup, find_packages

setup(
    name="camel_ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        # "camel-ai",       # 必要なら外部 camel-ai を追加
        "pydantic>=2.0.0",
    ],
)