# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *
from match import *


class ErrorPageBody(AviResource):
    resource_name = "errorpagebody"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) "),
        required=True,
        update_allowed=True,
    )
    error_page_body_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) Error page body sent to client when match"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'error_page_body',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'error_page_body': error_page_body_schema,
    }



class ErrorPage(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.2.4) Index of the error page"),
        required=False,
        update_allowed=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.2.4) Enable or disable the error page (Default: True)"),
        required=False,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.4) Add match criteria for http status codes to the error page"),
        schema=HTTPStatusMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    error_page_body_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) Custom error page body used to sent to the client You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    error_redirect_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) Redirect sent to client when match"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'enable',
        'match',
        'error_page_body_uuid',
        'error_redirect',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'error_page_body_uuid': error_page_body_uuid_schema,
        'error_redirect': error_redirect_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'match': getattr(HTTPStatusMatch, 'field_references', {}),
        'error_page_body_uuid': 'errorpagebody',
    }

    unique_keys = {
        'my_key': 'index',
        'match': getattr(HTTPStatusMatch, 'unique_keys', {}),
    }



class ErrorPageProfile(AviResource):
    resource_name = "errorpageprofile"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) "),
        required=True,
        update_allowed=True,
    )
    company_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) (Deprecated in: 18.1.1) Name of the company to show in error page"),
        required=False,
        update_allowed=True,
    )
    app_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) (Deprecated in: 18.1.1) Name of the Virtual Service which generated the error page"),
        required=False,
        update_allowed=True,
    )
    host_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.2.4) (Deprecated in: 18.1.1) Fully qualified domain name for which the error page is generated"),
        required=False,
        update_allowed=True,
    )
    error_pages_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("(Introduced in: 17.2.4) Defined Error Pages for HTTP status codes"),
        schema=ErrorPage.properties_schema,
        required=True,
        update_allowed=False,
    )
    error_pages_schema = properties.Schema(
        properties.Schema.LIST,
        _("(Introduced in: 17.2.4) Defined Error Pages for HTTP status codes"),
        schema=error_pages_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'company_name',
        'app_name',
        'host_name',
        'error_pages',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'company_name': company_name_schema,
        'app_name': app_name_schema,
        'host_name': host_name_schema,
        'error_pages': error_pages_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'error_pages': getattr(ErrorPage, 'field_references', {}),
    }

    unique_keys = {
        'error_pages': getattr(ErrorPage, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::ErrorPageBody': ErrorPageBody,
        'Avi::LBaaS::ErrorPageProfile': ErrorPageProfile,
    }

