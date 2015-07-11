from zope.interface import Interface
from zope import schema
from zope.viewlet.interfaces import IViewletManager

from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """


class ILeftCol(IViewletManager):
    """A viewlet manager that sits in the left most column of the page
       (an addition to the main template)
    """


class IUtilsView(Interface):
    """ Marker interface for misc browser view """

    def getUpcomingEvents(limit):
        """Grabbing upcoming events for the home page"""

    def getMonthName(self, month):
        """ Translates a month int into a short name """

    def formatSiteMap(self, code):
        """ Customizes the sitemap pre-formated code to fit the comps """


class ITiledListingView(Interface):
    """marker interface for a view providing tiled view listed items

    This view is suitable for folders or collections
    """


class IEventListingView(Interface):
    """marker interface for a view providing one column listed items

    This view is suitable for folders or collections
    """


class IISAWSettings(Interface):
    emergency_message = schema.Text(title=u"Emergency Message",
            description=u"Any text here will be displayed at the top of the site. An empty field means do not display emergency message",
            required=False)
