#!/bin/bash
set -e

echo "Installing note CLI..."

mkdir -p "$HOME/.local/bin"

ln -sf "$(pwd)/note" "$HOME/.local/bin/note"

echo "Installed!"