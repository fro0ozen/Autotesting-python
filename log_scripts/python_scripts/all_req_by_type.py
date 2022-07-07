import sys
import json

jsonify = "--json" in sys.argv

dct = {}
with open(sys.argv[1]) as f:
    for i in f:
        lst = i.split()
        if dct.get(lst[5][1:], False):
            dct[lst[5][1:]] += 1
        else:
            dct[lst[5][1:]] = 1

with open("all_req_by_type_out.txt", "w") as f:
    if jsonify:
        json_lst = []
        for i in dct.keys():
            json_lst.append({"request_type": i, "request_type_number": dct[i]})
        f.write(json.dumps(json_lst))
    else:
        f.write(f"Total number of requests by type\n")
        for i in dct.keys():
            f.write(f"{i} - {dct[i]}\n")
