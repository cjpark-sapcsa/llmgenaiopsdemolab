import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)  # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data = {
    "question": "How can I request a refill for my prescription at Lamna Healthcare?",
    "chat_history": []
}

body = str.encode(json.dumps(data))

# Use the REST endpoint from your deployment
url = 'https://rag-1016-endpoint.eastus2.inference.ml.azure.com/score'

# Replace this with the primary/secondary key from the Azure portal
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCIsImtpZCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3Mjg5Nzc0MTQsIm5iZiI6MTcyODk3NzQxNCwiZXhwIjoxNzI4OTgxMzQ4LCJhY3IiOiIxIiwiYWlvIjoiQWFRQVcvOFlBQUFBQWFIMDcycHZvNkJzQWRjajF2L2dSZDE3VTExUUhaMWt6ZEpSOHZoUFVQT05TTTZTSFYxTUQ2bEFqdk1UWjFsWFRUeTE4RTVsYy9qQm1NcWplNmU5NkJWU1NIVlo1bVRjRGFuS1ZqbjBaZUZBRHVjc0plQ3hKSmpSTE81S3pWSVhwQ29rY1lTL2JzTGdWYnN3Z3BobkNRMkRPbDdObTZIVWVVeUFFUTFuTFBrVkJ3clFhUkVsVWVQdVE3YXR2NEc1ZnR3Wk81RmJxWkRiMC9CS2Y3VzVUZz09IiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwMDcwODM1RTUyIiwiYW1yIjpbInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiY2JkNGIxYmYtNjJhMy00NTUxLWI1MzktMzNjYjBhMWMyZWMyIiwiZW1haWwiOiJDaGFuSmluLlBhcmtAbWljcm9zb2Z0LmNvbSIsImZhbWlseV9uYW1lIjoiUGFyayIsImdpdmVuX25hbWUiOiJDaGFuIEppbiIsImdyb3VwcyI6WyJiMTMwNDAyMi0wOGU2LTQ0N2QtYjA5NC0xNTM3MDU5N2M2YjYiLCIwOTUzMWE3Mi0yYzNlLTRlMDYtYmUxZS0yNTk2YmQwOGRjZGQiLCJkMzRjNGViZS00OTg0LTQ5MDMtYTY0ZC04YzIwMjgzZDUxNmIiLCJhNGJmOThlMS1jMWNlLTQ5ZWUtOTYyNC04NzViYmVhOTRlNzQiLCJlMzA5NmRmNy1iNjVjLTRlMzItYWIxYS03YTM1ZGM2ODRmMGEiXSwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3LyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjI0MDQ6ZjgwMTo5MDAwOjFhOjQ5Zjg6Y2YzZDozOTgzOjNiYTEiLCJuYW1lIjoiQ2hhbiBKaW4gUGFyayIsIm9pZCI6IjY2ODlmYTQxLWVkZWYtNDc4ZC1hMzAzLWZkYWE2NjEwY2I2ZSIsInB1aWQiOiIxMDAzMjAwMjBDMDZENDkwIiwicmgiOiIwLkFVWUFFOEN6RmdEVGpVYXNaSDdhQ0NDMjAxOXZwaGpmMnhkTW5kY1dOSEVxbkw3eEFMYy4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiI0YzkydmQwcjJjQkZNdkVVZ01wZnVYSlUzWkhaeDlwMjZPYVQ3eDFxNE9ZIiwidGlkIjoiMTZiM2MwMTMtZDMwMC00NjhkLWFjNjQtN2VkYTA4MjBiNmQzIiwidW5pcXVlX25hbWUiOiJDaGFuSmluLlBhcmtAbWljcm9zb2Z0LmNvbSIsInV0aSI6ImFINi1tVng1VkUtakp0X3d2Nk1LQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfaWRyZWwiOiIxIDQifQ.ENRSy8IHGCmNiBXHw3NvHiaJU2Omd0LcbY-OLHVDC1WD1eCORdIsB8F7TMwZ6S37n6h02rmhjtyMVfNrklpLFVTHEj9qdpPuZ-TIkO_KTDzx1oWPagM7T7AHSVmAv38sfxWIFkRc00QvS5YelKtoOSXC_-qHdUOrKZyIilEnN-W9b5XX103AFaKNGoM0NlC0zksxsYt_q3NCF1mppzAmq2Ne2Ki7V382tsisPO2TVIUh_Hx3WLiCwYUEVehFQe3l4Gz57v6Zomw882fIIWZQw8Q-A-PqejQOW8qwwrFNOBxKHsh0Q2jd4Pl8DgCDDvBzJZVTHF4RNLlGZ3fAlXzvOg'  # <--- Replace this with your actual key

if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")

headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + api_key}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))
