import unittest
from backend.msg_split import split_message, check_is_split_here, find_unclosed_tag, get_all_tags


class TestMyProgram(unittest.TestCase):
    def test_split_message(self):
        html_string = "<html><body><p>This is a test.</p><p>Another paragraph.</p></body></html>"
        
        # Test splitting with chunk size 30
        chunks = split_message(html_string, 30)
        expected_chunks = [
            '<html><body><p>This is a t</p>', 
            '<p>est.</p><p>Another para</p>', 
            '<p>graph.</p></body></html>'
            ]

        for expected in expected_chunks:
            self.assertEqual(next(chunks), expected)

        with self.assertRaises(StopIteration):
            next(chunks)

        # Test splitting with chunk size larger than text length
        chunks = split_message(html_string, 100)
        expected_chunks = ['<html><body><p>This is a test.</p><p>Another paragraph.</p></body></html>']

        for expected in expected_chunks:
            self.assertEqual(next(chunks), expected)

        with self.assertRaises(StopIteration):
            next(chunks)
    
    def test_check_is_split_here(self):
        status = check_is_split_here([])
        expected_status = True
        self.assertEqual(status, expected_status)

        status = check_is_split_here([('<a>', 0), ('</a>', 10)])
        expected_status = True
        self.assertEqual(status, expected_status)

        status = check_is_split_here([('<p>', 0), ('<b>', 10)])
        expected_status = False
        self.assertEqual(status, expected_status)
    
    def test_find_unclosed_tag(self):
        opening_tags = find_unclosed_tag([('<p', 0), ('</p', 10), ('<p', 20)])
        expected_status_opening_tags = ['<p']
        self.assertEqual(opening_tags, expected_status_opening_tags)


        opening_tags = find_unclosed_tag([('<p', 0), ('</p', 10), ('<p', 20), ('</p', 40)])
        expected_status_opening_tags = []
        self.assertEqual(opening_tags, expected_status_opening_tags)
    
    def test_get_all_tags(self):
        chunk = "<html><body><p>This is a test.</p><p>Another paragraph."
        tags = get_all_tags(chunk)
        expected_tags = [('<html', 0), ('<body', 6), ('<p', 12), ('</p', 30), ('<p', 34)]
        self.assertEqual(tags, expected_tags)


if __name__ == '__main__':
    unittest.main()
