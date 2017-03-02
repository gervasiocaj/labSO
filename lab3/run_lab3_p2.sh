#!/bin/bash
k=${1}
while ((k-- > 0 ))
do
  echo teste-$k.txt
#  perf sched record ./cpu_burn --output a-$k.txt &
done