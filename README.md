Full File Sequence Encryptions: CLI Version

My hopes for this project are to improve it to be fully usable in day to day encryption needs.
At the moment, I am developing it to be a CLI environment, mostly usable for windows and linux.

![The Syntax](/images/tut1.png)

I expect to have a fully working version within a week, from there it will be fairly simple to
add the following standards:

  -MD5
  -SHA512
  
For decrypting:
  -While very insecure, the way I would crack this is by running John The Ripper against your encrypted
  message using the most common 1000-10000 words. This, of course, means anyone can do this. I'd like
  to implement a key system, allowing simple peer to peer encryption and decryption. For now, that is mostly
  a TODO
