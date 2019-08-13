# This python script will open a file named "mailinglist.txt" that has a z-address on every line, and ask the user
# to input a memo. It will then assemble a z_sendmany transaction with a 1 zatoshi output and the memo for each recipient listed in
# mailinglist.txt . Finally, while zcashd is running, run sendletter.bat in the same folder as zcash-cli to send.

 
file = open("mailinglist.txt")
memotext=input("Input Memo (IN QUOTES): ")
hextext=memotext.encode("hex")
outstring=""
output = open("sendletter.bat","w")
outstring += 'zcash-cli z_sendmany "zsxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" '
outstring += '"['
 
for a in file:
    outstring += '{\\"address\\": \\"'+a+'\\",\\"amount\\": 0.00000001, \\"memo\\":\\"'+hextext+'\\"},'
   
 
outstring=outstring[:-1]
outstring+= ']"'
outstring = outstring.replace('\n', '')
output.write(outstring)