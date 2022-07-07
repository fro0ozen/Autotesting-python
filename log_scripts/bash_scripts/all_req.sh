#! /bin/bash
file=$1
echo "Total number of requests" > all_req_out.txt
cut -d ' ' -f 7 $file | wc -l >> all_req_out.txt
