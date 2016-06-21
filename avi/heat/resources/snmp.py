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


class SnmpTrapServer(object):
    # all schemas
    ip_addr_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the SNMP trap destination"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    community_schema = properties.Schema(
        properties.Schema.STRING,
        _("The community string to communicate with the trap server."),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip_addr',
        'community',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip_addr': ip_addr_schema,
        'community': community_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip_addr': getattr(IpAddr, 'field_references', {}),
    }



class SnmpConfiguration(object):
    # all schemas
    community_schema = properties.Schema(
        properties.Schema.STRING,
        _("Community string for SNMP v2c"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'community',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'community': community_schema,
    }




class SnmpTrapProfile(AviResource):
    resource_name = "snmptrapprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user-friendly name of the SNMP trap configuration."),
        required=True,
        update_allowed=True,
    )
    trap_servers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SnmpTrapServer.properties_schema,
        required=True,
        update_allowed=False,
    )
    trap_servers_schema = properties.Schema(
        properties.Schema.LIST,
        _("The IP address or hostname of the SNMP trap destination server."),
        schema=trap_servers_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'trap_servers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'trap_servers': trap_servers_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'trap_servers': getattr(SnmpTrapServer, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::SnmpTrapProfile': SnmpTrapProfile,
    }

