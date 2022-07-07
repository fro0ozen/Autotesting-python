import sys
import re
import json

jsonify = "--json" in sys.argv

lst = []
with open(sys.argv[1]) as f:
    for i in f:
        if re.match(r"4[0-9][0-9]", i.split()[8]):
            lst.append(i.split())
    lst.sort(key=lambda x: int(x[9]), reverse=True)

with open("largest_req_out.txt", "w") as f:
    if jsonify:
        json_lst = []
        for i in lst[:5]:
            json_lst.append({
                "ip_address": i[0],
                "url": i[6],
                "status_code": i[8],
                "request_size": i[9]})
        f.write(json.dumps(json_lst))
    else:
        f.write("Top 5 largest requests that failed with client error\n")
        for i in lst[:5]:
            f.write(f"{i[0]} {i[6]} {i[8]} {i[9]}\n")
