# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import wangye.theme


class WangyeThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=wangye.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'wangye.theme:default')


WANGYE_THEME_FIXTURE = WangyeThemeLayer()


WANGYE_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(WANGYE_THEME_FIXTURE,),
    name='WangyeThemeLayer:IntegrationTesting'
)


WANGYE_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(WANGYE_THEME_FIXTURE,),
    name='WangyeThemeLayer:FunctionalTesting'
)


WANGYE_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        WANGYE_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='WangyeThemeLayer:AcceptanceTesting'
)
