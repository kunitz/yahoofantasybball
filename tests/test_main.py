from unittest import TestCase

from yahoofantasybball.main import printDate, write_player_line, write_header


class Test(TestCase):
    def test_print_date(self):
        printDate()


class Test(TestCase):
    def test_write_player_line(self):
        write_header()
        write_player_line("Player Name", 5, 130.4565, 10, "This is a long injury report")
