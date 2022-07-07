#! /bin/bash
file=$1
echo "Total number of requests by type" > all_req_by_type_out.txt
req=`(cat $file | awk '{print $6}' | awk '!x[$0]++')`
declare -A ret
for i in $req
do
  ret[$i]=0
done

for i in $(cut -d ' ' -f 6 $file)
do
  ret[$i]=$((${ret[$i]}+1))
done

for i in $req
do
  echo "$(echo -n "$i" | tail -c +2) - ${ret[$i]}" >> all_req_by_type_out.txt
done
