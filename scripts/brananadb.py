import webbrowser
try:
   print(SERVER_HOST)
except:
   SERVER_HOST = '0.0.0.0'
try:
   print(SERVER_PORT)
except:
   SERVER_PORT = 8000
l = f'http://{SERVER_HOST}:{SERVER_PORT}'
