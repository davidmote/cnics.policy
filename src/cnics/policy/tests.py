import unittest2 as unittest
from plone.app.testing import applyProfile
from Products.CMFCore.utils import getToolByName

from cnics.policy.testing import CNICS_POLICY_INTEGRATION_TESTING

class TestSetup(unittest.TestCase):

    layer = CNICS_POLICY_INTEGRATION_TESTING

    def test_indexing_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('collective.indexing'))

    def test_datepicker_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('jyu.z3cform.datepicker'))

    def test_caching_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('plone.app.caching'))

    def test_ldap_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('plone.app.ldap'))

    def test_sequencedb_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('beast.cnics.sequencedb'))
