import sys
import re
import json

jsonify = "--json" in sys.argv

dct = {}
sorted_dict = {}
lst = []
with open(sys.argv[1]) as f:
    for i in f:
        if re.match(r"5[0-9][0-9]", i.split()[8]):
            if i.split()[0] in dct.keys():
                dct[i.split()[0]] += 1
            else:
                dct[i.split()[0]] = 1

sorted_values = sorted(dct.values(), reverse=True)
for i in sorted_values:
    for k in dct.keys():
        if dct[k] == i:
            sorted_dict[k] = dct[k]
            dct.pop(k)
            break

with open("users_num_req_out.txt", "w") as f:
    if jsonify:
        json_lst = []
        for i in list(sorted_dict.keys())[:5]:
            json_lst.append({"number_of_requests": sorted_dict[i], "ip_address": i})
        f.write(json.dumps(json_lst))
    else:
        f.write("Top 5 users by the number of requests that ended with a server error\n")
        for i in list(sorted_dict.keys())[:5]:
            f.write(f"{sorted_dict[i]} {i}\n")
