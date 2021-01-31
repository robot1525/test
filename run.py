import os

#output1 = os.popen("ifconfig").readlines()
outputs_curl_icanhazip = os.popen("curl icanhazip.com").readlines()
#os.popen("curl ifconfig.me")
#os.popen("curl ipecho.net/plain")

w = open("ips.txt", "w")
w.write(outputs_curl_icanhazip[0][:-1])
w.close()