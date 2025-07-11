# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 00:30:01 2025

@author: Owner
"""

import os
from camel_ai.owl import OWLClient

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    client = OWLClient(api_key)
    prompt = "Hello, world!"
    print("User Prompt:", prompt)
    response = client.completion(prompt)
    print("Model Response:\n", response)

if __name__ == "__main__":
    main()