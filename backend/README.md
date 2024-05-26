# HTML_fragmentation

**[HTML_fragmentation](https://github.com/Bak0903/HTML_fragmentation)**

This project contains the main script msg_split.py along with other necessary files such as .gitignore, requirements.txt, source.html for testing, and test.py.

## Stack

- Python 3.10

## Local Development

In order to deploy the project for local development, one should:
 1. clone from the remote repository 
 2. copy default envs (and change them if there is a need)
 3. execute docker-compose command (make sure that you have docker and docker-compose installed on your machine)
```
cd {project_folder}
cp .env.sample .env
docker-compose up
```

## How to run tests

```
docker-compose -f docker-compose-test.yml up --build
```

## Variables

| Key          | Description                | Default value                       |
|:-------------|:---------------------------|:------------------------------------|
| MAX_LEN      | Maximum length             | 4096                                |
| BLOCKED_TAGS | Source tags                | <p,<b,<strong,<i,<ul,<ol,<div,<span |


