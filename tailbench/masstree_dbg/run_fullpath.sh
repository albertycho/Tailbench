#!/bin/bash

if [[ -z "${NTHREADS}" ]]; then NTHREADS=32; fi

QPS=20000
MAXREQS=50000
WARMUPREQS=14000

TBENCH_QPS=${QPS} TBENCH_MAXREQS=${MAXREQS} TBENCH_WARMUPREQS=${WARMUPREQS} \
    TBENCH_MINSLEEPNS=10000 /home/azureuser/CXL_WD/Tailbench/tailbench/masstree/mttest_integrated -j${NTHREADS} \
    mycsba masstree
