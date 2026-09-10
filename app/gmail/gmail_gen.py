import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL","grmini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise Runtime error("GEMINI_API_KEY is missing,")

prompt = f"""
you are a professional Gmail email writing assistant.

convert the user's voice command into a professional email.

Rules:

-Do not copy the command literally.
-Do not explain anything.
-Do not invent names, dates, prices, companies, attachments, or facts.
-Keep the email natural and concise

Output exactly:

SUBJECT: <subject>
BODY:
<email body>

User command:
(command)
"""

  url = (
    f"https://generativelanguage.googleapis.com/"
    f"v1beta/model/(MODEL):generatecontent"
)  
payload = {
  "contents": [{"parts": [{"text": prompt}}],
  "generationconig":{
    "Temperature":0.7.
    "maxOutputTokens": 800
  }
}
req = urllib.request.Request(
  url,
  data = json.dumps(payload).encode()
  headers={
  "content-Type":"application/json",
  "x-goog-api-key": API_KEY
},
  method="POST"
)
for attempt in range

