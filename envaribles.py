#Linux Environment Varibles
#env
#echo $PATH
#   /usr/local/sbin/etc/etc/etc

#!/usr/bin/env python3
import os

print("HOME: " + os.environ.get("HOME", ""))
print("SELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))


