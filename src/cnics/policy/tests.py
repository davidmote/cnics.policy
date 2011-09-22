import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import leadtheway.policy


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            ztc.installPackage(leadtheway.policy)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='leadtheway.policy',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='leadtheway.policy.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='leadtheway.policy',
        #    test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='leadtheway.policy',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
