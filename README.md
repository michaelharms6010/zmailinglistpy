# Python Zcash Memo Mailer


IMPORTANT: You MUST update the "from" address in the python code to be the z-address you wish to send from. It is a placeholder by default, "zsxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

This python script will open a file in the same directory named "mailinglist.txt" that has a z-address on every line (example provided), and ask the user to input a memo. It will then assemble a z_sendmany transaction with a 1 zatoshi output and the memo for each recipient listed in mailinglist.txt . Finally, while zcashd is running, run sendletter.bat in the same folder as zcash-cli to send.


## Known Problems / Limitations

This is currently limited (to ~7 transactions) in Windows 10 by the maximum string length (~8000 chars) allowable by Powershell. I have not yet tested its behavior on Linux. I have it on decent authority that this can be resolved with a relatively simple Perl script to talk to the zcashd rpc client. I am currently researching how to do this :)
