# import pytest

from kata.app import main


class TestMain:

    def test_returns_message(self):
        # arrange

        # act
        result = main()

        # assert
        assert result == "Hello"
