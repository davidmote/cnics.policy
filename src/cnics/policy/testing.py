from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CnicsPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cnics.policy as package
        xmlconfig.file('configure.zcml', package, context=configurationContext)

    def tearDownZope(self, app):
        pass

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cnics.policy:default')


CNICS_POLICY_FIXTURE = CnicsPolicy()

CNICS_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CNICS_POLICY_FIXTURE,),
    name='Cnics:Integration'
    )
