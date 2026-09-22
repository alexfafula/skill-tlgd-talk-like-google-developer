#!/bin/sh
set -eu

benchmark_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

python3 "$benchmark_dir/run.py" doctor
python3 "$benchmark_dir/run.py" prepare
python3 "$benchmark_dir/run.py" run \
  --agents agy \
  --manage-agy-settings \
  --repetitions 1 \
  "$@"
