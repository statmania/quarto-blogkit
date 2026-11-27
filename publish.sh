#!/usr/bin/env bash
root="$(dirname "$0")"
ext="$root/_extensions/statmania/blogkit"
[ -d "$ext" ] || ext="$root/_extensions/blogkit"
exec bash "$ext/publish.sh" "$@"
