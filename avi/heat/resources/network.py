# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from common import *
from options import *


class Subnet(object):
    # all schemas
    prefix_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specify an IP subnet prefix for this Network"),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=True,
    )
    static_ips_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    static_ips_schema = properties.Schema(
        properties.Schema.LIST,
        _("Specify a pool of IP addresses for use in Service Engines"),
        schema=static_ips_item_schema,
        required=False,
        update_allowed=True,
    )
    static_ranges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrRange.properties_schema,
        required=True,
        update_allowed=False,
    )
    static_ranges_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=static_ranges_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'prefix',
        'static_ips',
        'static_ranges',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'prefix': prefix_schema,
        'static_ips': static_ips_schema,
        'static_ranges': static_ranges_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'prefix': getattr(IpAddrPrefix, 'field_references', {}),
        'static_ips': getattr(IpAddr, 'field_references', {}),
        'static_ranges': getattr(IpAddrRange, 'field_references', {}),
    }

    unique_keys = {
        'prefix': getattr(IpAddrPrefix, 'unique_keys', {}),
        'static_ips': getattr(IpAddr, 'unique_keys', {}),
        'my_key': 'prefix',
        'static_ranges': getattr(IpAddrRange, 'unique_keys', {}),
    }



class Network(AviResource):
    resource_name = "network"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    vcenter_dvs_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    vimgrnw_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    dhcp_enabled_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Select the IP address management scheme for this Network"),
        required=False,
        update_allowed=True,
    )
    exclude_discovered_subnets_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When selected, excludes all discovered subnets in this network from consideration for virtual service placement."),
        required=False,
        update_allowed=True,
    )
    configured_subnets_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=Subnet.properties_schema,
        required=True,
        update_allowed=False,
    )
    configured_subnets_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=configured_subnets_item_schema,
        required=False,
        update_allowed=True,
    )
    vrf_context_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    synced_from_se_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    cloud_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'vcenter_dvs',
        'vimgrnw_uuid',
        'dhcp_enabled',
        'exclude_discovered_subnets',
        'configured_subnets',
        'vrf_context_uuid',
        'synced_from_se',
        'cloud_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'vcenter_dvs': vcenter_dvs_schema,
        'vimgrnw_uuid': vimgrnw_uuid_schema,
        'dhcp_enabled': dhcp_enabled_schema,
        'exclude_discovered_subnets': exclude_discovered_subnets_schema,
        'configured_subnets': configured_subnets_schema,
        'vrf_context_uuid': vrf_context_uuid_schema,
        'synced_from_se': synced_from_se_schema,
        'cloud_uuid': cloud_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'vrf_context_uuid': 'vrfcontext',
        'configured_subnets': getattr(Subnet, 'field_references', {}),
        'vimgrnw_uuid': 'vimgrnwruntime',
    }

    unique_keys = {
        'configured_subnets': getattr(Subnet, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::Network': Network,
    }

