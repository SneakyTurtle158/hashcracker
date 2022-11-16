# hashcracker
Dictionary cracker for md5, sha1, or sha256 hashes

##Requirments:
```
pip2 install -r requirements.txt
```

#How to use:
Download a password dictionary file, (rockyou.txt is available at: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

Syntax for using the script:
```
python3 cracker.py <hashtocrack> <pathtodictionary> <algorithtype>
```
Algorithm types and input for the script:
MD5:  md5sumhex
SHA1: sha1sumhex
SHA256: sha256sumhex

#Example:

Hash to crack (MD5 hash): f25a2fc72690b780b2a14e140ef6a9e0

```
python3 cracker.py f25a2fc72690b780b2a14e140ef6a9e0 /usr/share/wordlists/rockyou.txt md5sumhex
```
