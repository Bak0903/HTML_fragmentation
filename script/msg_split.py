import re
import click
from typing import Generator

BLOCKED_TAGS = ['<p', '<b', '<strong', '<i', '<ul', '<ol', '<div', '<span', ]
MAX_LEN = 4096


def split_message(source: str, max_len: int = MAX_LEN)-> Generator[str, None, None]:
    """Splits the original message (`source`) into fragments of the specified length 
        (`max_len`)."""
    source_len = len(source)

    start = 0
    end = max_len
    current_chunk = ''
    opening_tags = ''
    closing_tags = ''
    unclosed_tags = []

    splited_messages = []
    
    chunk = source[start:end]
    while start < source_len:
        tags = get_all_tags(chunk)
        is_block = check_is_split_here(tags)
        if is_block:
            unclosed_tags = find_unclosed_tag(tags)
            if unclosed_tags:
                tag = unclosed_tags[0]
                closing_tags = f'</{tag[1:]}>' + closing_tags
                opening_tags += f'<{tag[1:]}>'
                end -= len(closing_tags)
                chunk = chunk[:-len(closing_tags)]
                chunk += closing_tags
            else:
                # splited_messages.append(chunk)
                yield chunk
                start = end
                end += max_len - len(opening_tags)
                chunk = source[start:end]
                chunk = opening_tags + chunk
                closing_tags = ''
                opening_tags = ''
        else:
            end = tags[-1][1]
            chunk = chunk[:end]
        if start >= end:
            raise Exception(f"Can not split message by max_len={max_len}")


def check_is_split_here(tags: list) -> bool:
    """Determines if the current tag is a suitable split point based on 
        the given list of tags"""
    if not tags:
        return True
    tag = tags[-1][0]
    if '/' in tag:
        return True
    if tag in BLOCKED_TAGS:
        return True
    return False


def find_unclosed_tag(tags: list) -> list:
    '''Finds unclosed tags by checking the 
        given list of tags.'''
    opening_tags = []
    closing_tags = []
    for tag, pos in tags:
        if tag.startswith("</"):
            closing_tags.append(tag)
        elif tag in BLOCKED_TAGS:
            opening_tags.append(tag)
    for tag in closing_tags:
        opening_tag = tag.replace('/', '')
        if opening_tag in opening_tags:
            opening_tags.remove(opening_tag)
    return opening_tags


def get_all_tags(chunk: str) -> list:
    '''Finds all tags in the given string.'''
    tag_pattern = re.compile(r'</?[A-Za-z0-9]+')
    tags = [ (m.group(), m.start()) for m in tag_pattern.finditer(chunk)]
    return tags


@click.command()
@click.option('--max-len', default=4096, help='Split max length')
@click.option('--source', help='Source file')
def run_split(max_len: int, source: str):
    with open(source, 'r') as file:
        html_as_string = file.read()
    messages = split_message(html_as_string, max_len)
    for idx, message in enumerate(messages):
        click.echo(f"-- fragment #{idx+1}: {len(message)} chars --")
        click.echo(message)


if __name__ == '__main__':
    run_split()
