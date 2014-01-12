This is just a very simple proxy to rename a username. It's written in python using the twisted library for network connections. 

Steps to make this work:
0) set up the popular server.properties and make sure you set online-mode=false and then start the server
1) sudo apt-get install python twisted on the server
2) download the script proxy_user_rename.py
3) change the 'usernameToChange' string to what you want to change
4) change the 'usernameToChangeTo' string to what you want the new name to be
5) chmod 744 proxy_user_rename.py
6) execute the script: ./proxy_user_rename.py
7) Open up the application this is made for, and join the server at: 192.168.1.1:40321
8) Send the other user directly to the server 192.168.1.1 and both of you can play.

You can of course edit the python and change the proxy port (40321) to something else. Don't pick a well known port though, or it won't work as well. I only need this so my son and I can play. But you could either (a) upgrade the script to accept multiple connections and rename each of them or (b) you can run this script multiple times with different proxy ports
