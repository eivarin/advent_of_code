python -m venv aoc_venv
source aoc_venv/bin/activate
pip install -r requirements.txt
aocd-token > ~/.config/aocd/token
deactivate