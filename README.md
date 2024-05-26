# HTML_fragmentation

This project contains the main script msg_split.py along with other necessary files such as .gitignore, requirements.txt, source.html for testing, and test.py.

Contents

msg_split.py: This is the main script of the project. It is responsible for splitting messages into smaller chunks.
.gitignore: This file specifies intentionally untracked files that Git should ignore.
requirements.txt: This file lists all the Python libraries that the project depends on. It can be used to install dependencies using pip install -r requirements.txt.
source.html: This HTML file is used for testing purposes.
test.py: This Python script contains test cases for the msg_split.py script.

Usage

Clone the repository:

git clone https://github.com/Bak0903/HTML_fragmentation.git

Install dependencies:

pip install -r requirements.txt

Run the main script:

python msg_split.py --max-len=4096 --source=./source.html
