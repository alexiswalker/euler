s = ''.join(str(i) for i in range(1,10**6+1))

print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])