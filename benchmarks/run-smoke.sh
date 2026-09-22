#!/bin/sh
set -eu

benchmark_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

python3 "$benchmark_dir/run.py" doctor
python3 "$benchmark_dir/run.py" prepare
python3 "$benchmark_dir/run.py" run \
  --agents claude,codex,agy \
  --manage-agy-settings \
  --cases conditional-get-304 \
  --repetitions 1 \
  "$@"
