------------------------------------------------------------------------------------------------------------------------------------------|<br/>
-Hi everyone 👋, welcome to the RVSP github,<br/>

This project consist of bypassing any anti-virus by using a custom reverse-shell<br/>
coded by myself with the help of my friend patoche890. We decided to share this project to found a community of B-HATS<br/>
To Help us in our project. If you wanna help us, there's a discord link upside and in the top-right panel.<br/>
Go see it 👍<br/>
Enjoy our tool 👋<br/>

------------------------------------------------------------------------------------------------------------------------------------------|<br/>

<b>Installation :<b/>

1) You need to install Python 3.12<br>

2) In cmd run :
```ruby
pip install -r requirements.txt
```
3) Go into ./General-Users/Python-Files/ then edit Client.py :
```ruby
SERVER_HOST = '127.0.0.1' --> Put the Server-Listener IP
SERVER_PORT = 4444 --> Put the Server-Listener PORT
```
4) Run encode.py then paste the full path of your Client.py file<br>

5) Copy the encoded client.py then past it in decode-exec.py here :
```ruby
encoded = (""" HERE """)
```

6) Go to pyobfuscate.com And Obfusc the File like this :<br>
   -Code minifier (1)<br>
   -Var Obfusc (2)<br>
