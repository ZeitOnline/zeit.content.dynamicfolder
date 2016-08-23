# coding: utf8
from zeit.cms.i18n import MessageFactory as _
import zeit.cms.content.interfaces
import zeit.cms.interfaces
import zeit.cms.repository.interfaces
import zope.interface
import zope.schema


DAV_NAMESPACE = 'http://namespaces.zeit.de/CMS/zeit.content.dynamicfolder'


class IVirtualContent(zope.interface.Interface):
    """Maker interface for virtual content objects not present in DAV."""


class IDynamicFolder(zeit.cms.repository.interfaces.IDAVContent):
    """Interface for the Content-Type DynamicFolder.

    Does not specify that it is a container, since it is only a container
    inside the respository, but not when checked out.

    """

    config_file = zope.schema.Choice(
        title=_(u'Configuration file'),
        source=zeit.cms.content.contentsource.cmsContentSource)

    content_template_file = zope.interface.Attribute(
        'XML template to create virtual content (ICMSContent)')


class IRepositoryDynamicFolder(
        IDynamicFolder,
        zeit.cms.repository.interfaces.IFolder):
    """DynamicFolder is a container inside the repository."""


class ILocalDynamicFolder(
        IDynamicFolder,
        zeit.cms.workingcopy.interfaces.ILocalContent):
    """DynamicFolder is a simple object, i.e. no folder, when checked out."""
