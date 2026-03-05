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
class writetodb:
   def showdatabase():
      l += '/sz'
      webbrowser.open_new(l)
   def addtodatabase(a):
      l += '/' + a
      webbrowser.open_new(l)
   def cleardatabase():
      l += '/'
      webbrowser.open_new(l)
class opendatabase:
   def stringtolist(file, character):
      f = open(file)
      c = f.read()
      return c.split(character)
   def listtostring(list, character): return character.join(list)
