# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test modules."""


def test_init(hello_world):
    """Run a test."""
    import airflow_pandas

    # Test __init__
    assert hasattr(airflow_pandas, '__version__')

    # Test pytest fixtures
    assert(hello_world == "Hello World!")