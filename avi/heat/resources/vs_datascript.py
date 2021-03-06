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


class VSDataScript(object):
    # all schemas
    evt_schema = properties.Schema(
        properties.Schema.STRING,
        _("Event triggering execution of datascript"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['VS_DATASCRIPT_EVT_DNS_REQ', 'VS_DATASCRIPT_EVT_DNS_RESP', 'VS_DATASCRIPT_EVT_HTTP_LB_FAILED', 'VS_DATASCRIPT_EVT_HTTP_REQ', 'VS_DATASCRIPT_EVT_HTTP_REQ_DATA', 'VS_DATASCRIPT_EVT_HTTP_RESP', 'VS_DATASCRIPT_EVT_HTTP_RESP_DATA', 'VS_DATASCRIPT_EVT_HTTP_RESP_FAILED', 'VS_DATASCRIPT_EVT_MAX', 'VS_DATASCRIPT_EVT_TCP_CLIENT_ACCEPT']),
        ],
    )
    script_schema = properties.Schema(
        properties.Schema.STRING,
        _("Datascript to execute when the event triggers"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'evt',
        'script',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'evt': evt_schema,
        'script': script_schema,
    }



class VSDataScripts(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the virtual service datascript collection"),
        required=True,
        update_allowed=True,
    )
    vs_datascript_set_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the virtual service datascript collection You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'vs_datascript_set_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'vs_datascript_set_uuid': vs_datascript_set_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'vs_datascript_set_uuid': 'vsdatascriptset',
    }

    unique_keys = {
        'my_key': 'index',
    }



class VSDataScriptSet(AviResource):
    resource_name = "vsdatascriptset"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name for the virtual service datascript collection"),
        required=True,
        update_allowed=True,
    )
    datascript_item_schema = properties.Schema(
        properties.Schema.MAP,
        _("DataScripts to execute"),
        schema=VSDataScript.properties_schema,
        required=True,
        update_allowed=False,
    )
    datascript_schema = properties.Schema(
        properties.Schema.LIST,
        _("DataScripts to execute"),
        schema=datascript_item_schema,
        required=False,
        update_allowed=True,
    )
    pool_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pools that could be referred by VSDataScriptSet objects."),
        required=True,
        update_allowed=False,
    )
    pool_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("UUID of pools that could be referred by VSDataScriptSet objects. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        schema=pool_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    pool_group_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of pool groups that could be referred by VSDataScriptSet objects."),
        required=True,
        update_allowed=False,
    )
    pool_group_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("UUID of pool groups that could be referred by VSDataScriptSet objects. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        schema=pool_group_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    ipgroup_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of IP Groups that could be referred by VSDataScriptSet objects."),
        required=True,
        update_allowed=False,
    )
    ipgroup_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("UUID of IP Groups that could be referred by VSDataScriptSet objects. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        schema=ipgroup_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    string_group_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of String Groups that could be referred by VSDataScriptSet objects."),
        required=True,
        update_allowed=False,
    )
    string_group_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("UUID of String Groups that could be referred by VSDataScriptSet objects. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        schema=string_group_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.11,17.2.4) Creator name"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'datascript',
        'pool_uuids',
        'pool_group_uuids',
        'ipgroup_uuids',
        'string_group_uuids',
        'created_by',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'datascript': datascript_schema,
        'pool_uuids': pool_uuids_schema,
        'pool_group_uuids': pool_group_uuids_schema,
        'ipgroup_uuids': ipgroup_uuids_schema,
        'string_group_uuids': string_group_uuids_schema,
        'created_by': created_by_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'string_group_uuids': 'stringgroup',
        'pool_uuids': 'pool',
        'datascript': getattr(VSDataScript, 'field_references', {}),
        'ipgroup_uuids': 'ipaddrgroup',
        'pool_group_uuids': 'poolgroup',
    }

    unique_keys = {
        'datascript': getattr(VSDataScript, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::VSDataScriptSet': VSDataScriptSet,
    }

