#!/usr/bin/env bash

# credits: https://codeforces.com/blog/entry/118045

solver=$1 # like 'python3 filename'
server=$2 

# hack since if you just do -h, $2 will still be empty
if [[ -z "$solver" || -z "$server" ]]; then echo "Usage: tester-script SOLVER_PROCESS SERVER_PROCESS"; exit; fi


mkfifo pipe_in pipe_out

echo "-------------------  interaction  ------------------"

$solver < pipe_in 2> error_solver.log  | tee pipe_out &
$server < pipe_out 2> error_server.log | tee pipe_in 

echo "------------------- solver stderr ------------------"
cat error_solver.log
echo "------------------- server stderr ------------------"
cat error_server.log

rm error_solver.log
rm error_server.log
rm pipe_in
rm pipe_out
