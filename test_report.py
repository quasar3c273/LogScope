import unittest

from logscope.report import count_errors


class ErrorReportTests(unittest.TestCase):
    def test_mixed_stream(self):
        lines = ['{"path":"/a","status":500}', '{"path":"/a","status":599}',
                 '{"path":"/a","status":499}', 'null', 'broken',
                 '{"path":"/a","status":600}', '{"status":503}']
        self.assertEqual(count_errors(iter(lines)), ({"/a": 2}, 4))

    def test_empty_stream(self):
        self.assertEqual(count_errors([]), ({}, 0))
