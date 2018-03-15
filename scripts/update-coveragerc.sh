#!/bin/bash

function insert_source_file_into_omit() {
    local package=$1
    local path=$2
    installed_package=$(pip list --format=legacy | grep "${package}" | cut -d' ' -f1)
    match_count=$(cat .coveragerc | grep -c "${path}")
    if [[ "${installed_package}" == "" && $match_count -eq 0 ]]; then
        sed -i "s/omit =/omit = \n  ${path}/g" .coveragerc
    fi
}

insert_source_file_into_omit "prometheus_client" "jaeger_client\/metrics_factory\/prometheus_metrics.py"
