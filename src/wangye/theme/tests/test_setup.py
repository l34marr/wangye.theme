# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from wangye.theme.testing import WANGYE_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that wangye.theme is properly installed."""

    layer = WANGYE_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if wangye.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'wangye.theme'))

    def test_browserlayer(self):
        """Test that IWangyeThemeLayer is registered."""
        from wangye.theme.interfaces import (
            IWangyeThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IWangyeThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = WANGYE_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['wangye.theme'])

    def test_product_uninstalled(self):
        """Test if wangye.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'wangye.theme'))

    def test_browserlayer_removed(self):
        """Test that IWangyeThemeLayer is removed."""
        from wangye.theme.interfaces import \
            IWangyeThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IWangyeThemeLayer, utils.registered_layers())

