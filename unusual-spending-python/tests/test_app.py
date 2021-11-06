#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.app import main

class TestMain:

    def test_returns_message(self):
        # arrange

        # act
        result = main()

        # assert
        assert result == "Hello"
