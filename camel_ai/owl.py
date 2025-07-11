# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 00:26:15 2025

@author: Owner
"""

class OWLClient:
    """
    OpenAI API をラップするクライアントクラスの雛形。
    """
    def __init__(self, api_key: str = None):
        import os
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def completion(self, prompt: str) -> str:
        import openai
        openai.api_key = self.api_key
        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content