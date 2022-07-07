#! /bin/bash
file=$1
echo "Top 10 most frequent searches" > frequent_req_out.txt
cut -d ' ' -f 7 $file | sort | uniq -c | sort -rn | head -10 >> frequent_req_out.txt
