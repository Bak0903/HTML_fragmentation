# HTML_fragmentation


This project contains the main script msg_split.py along with other necessary files such as .gitignore, requirements.txt, source.html for testing, and test.py.


## Stack

- Python 3.10

## Local Development

In order to deploy the project for local development, one should:
 1. Clone from the remote repository:
```
git clone https://github.com/Bak0903/HTML_fragmentation.git
cd HTML_fragmentation
```
 2. Create a virtual environment:
```
python3 -m venv venv
```
 3. Activate the virtual environment:
```
source venv/bin/activate
```
 4. Install dependencies:
```
pip install -r requirements.txt
```
 5. Run the main script:
```
python script/msg_split.py --max-len=4096 --source=./template/source.html
```


## How to run tests

```
python -m unittest test/test_msg_split.py
```


