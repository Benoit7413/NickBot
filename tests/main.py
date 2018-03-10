import unittest
import asyncio
import pycodestyle
from nickbot.classes.emojiflag import EmojiFlag


class EmojiTest(unittest.TestCase):
    """Test case utilisé pour tester les fonctions du module 'random'."""
    username = ["Benoit | 🇫🇷", "Alpha | 🇬🇧", "-ROmEo-",
                "Omega 🕶", "🅱oot (🅱est 🅱all)", "'Noddy ツ 🙊 🙉 🙊"]

    def test_add(self):
        """Test adding a flag."""
        for nick in self.username:
            self.assertEqual(EmojiFlag.add(
                nick, "fr gb de cz gbdefr"), nick + ' | 🇫🇷 🇬🇧 🇩🇪 🇨🇿 🇬🇧 🇩🇪 🇫🇷')

    def test_remove(self):
        """Test removing a flag."""
        for nick in self.username:
            nick_add = EmojiFlag.add(nick, "fr gb de cz gbdefr")
            self.assertEqual(EmojiFlag.remove(nick_add), nick)

    def test_change(self):
        """Test changing a flag."""
        for nick in self.username:
            nick_add = EmojiFlag.add(nick, "fr gb de cz gbdefr")
            self.assertEqual(EmojiFlag.change(nick_add, "fr"), nick + ' | 🇫🇷')

    def test_change_clean(self):
        """Test changing a flag on a clean nickname."""
        for nick in self.username:
            nick_clean = EmojiFlag.remove(nick)
            self.assertEqual(EmojiFlag.change(
                nick_clean, "fr GB de cz gbDefr"),
                nick_clean + ' | 🇫🇷 🇬🇧 🇩🇪 🇨🇿 🇬🇧 🇩🇪 🇫🇷')


class TestCodeFormat(unittest.TestCase):

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['.'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
