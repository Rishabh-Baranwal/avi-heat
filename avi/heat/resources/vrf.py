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


class BgpPeer(object):
    # all schemas
    remote_as_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Peer Autonomous System ID"),
        required=False,
        update_allowed=True,
    )
    peer_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the BGP Peer"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    subnet_schema = properties.Schema(
        properties.Schema.MAP,
        _("Subnet providing reachability for Peer"),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=True,
    )
    md5_secret_schema = properties.Schema(
        properties.Schema.STRING,
        _("Peer Autonomous System Md5 Digest Secret Key"),
        required=False,
        update_allowed=True,
    )
    bfd_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable Bi-Directional Forward Detection. Only async mode supported."),
        required=False,
        update_allowed=True,
    )
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Network providing reachability for Peer"),
        required=False,
        update_allowed=True,
    )
    advertise_vip_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Advertise VIP to this Peer"),
        required=False,
        update_allowed=True,
    )
    advertise_snat_ip_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Advertise SNAT IP to this Peer"),
        required=False,
        update_allowed=True,
    )
    advertisement_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Advertisement interval for this Peer"),
        required=False,
        update_allowed=True,
    )
    connect_timer_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Connect timer for this Peer"),
        required=False,
        update_allowed=True,
    )
    keepalive_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Keepalive interval for this Peer"),
        required=False,
        update_allowed=True,
    )
    hold_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Hold time for this Peer"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'remote_as',
        'peer_ip',
        'subnet',
        'md5_secret',
        'bfd',
        'network_uuid',
        'advertise_vip',
        'advertise_snat_ip',
        'advertisement_interval',
        'connect_timer',
        'keepalive_interval',
        'hold_time',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'remote_as': remote_as_schema,
        'peer_ip': peer_ip_schema,
        'subnet': subnet_schema,
        'md5_secret': md5_secret_schema,
        'bfd': bfd_schema,
        'network_uuid': network_uuid_schema,
        'advertise_vip': advertise_vip_schema,
        'advertise_snat_ip': advertise_snat_ip_schema,
        'advertisement_interval': advertisement_interval_schema,
        'connect_timer': connect_timer_schema,
        'keepalive_interval': keepalive_interval_schema,
        'hold_time': hold_time_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'subnet': getattr(IpAddrPrefix, 'field_references', {}),
        'peer_ip': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'subnet': getattr(IpAddrPrefix, 'unique_keys', {}),
        'my_key': 'peer_ip',
        'peer_ip': getattr(IpAddr, 'unique_keys', {}),
    }



class BgpProfile(object):
    # all schemas
    local_as_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Local Autonomous System ID"),
        required=True,
        update_allowed=True,
    )
    ibgp_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("BGP peer type"),
        required=True,
        update_allowed=True,
    )
    peers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=BgpPeer.properties_schema,
        required=True,
        update_allowed=False,
    )
    peers_schema = properties.Schema(
        properties.Schema.LIST,
        _("BGP Peers"),
        schema=peers_item_schema,
        required=False,
        update_allowed=True,
    )
    keepalive_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Keepalive interval for Peers"),
        required=False,
        update_allowed=True,
    )
    hold_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Hold time for Peers"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'local_as',
        'ibgp',
        'peers',
        'keepalive_interval',
        'hold_time',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'local_as': local_as_schema,
        'ibgp': ibgp_schema,
        'peers': peers_schema,
        'keepalive_interval': keepalive_interval_schema,
        'hold_time': hold_time_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'peers': getattr(BgpPeer, 'field_references', {}),
    }

    unique_keys = {
        'peers': getattr(BgpPeer, 'unique_keys', {}),
    }



class GatewayMonitor(object):
    # all schemas
    gateway_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of next hop gateway to be monitored"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    gateway_monitor_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The interval between two ping requests sent by the gateway monitor.  If a value is not specified, requests are sent every second (1000 milliseconds)."),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_fail_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The number of consecutive failed gateway health checks before a gateway is marked down."),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_success_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The number of consecutive successful gateway health checks before a gateway that was marked down by the gateway monitor is marked up."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'gateway_ip',
        'gateway_monitor_interval',
        'gateway_monitor_fail_threshold',
        'gateway_monitor_success_threshold',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'gateway_ip': gateway_ip_schema,
        'gateway_monitor_interval': gateway_monitor_interval_schema,
        'gateway_monitor_fail_threshold': gateway_monitor_fail_threshold_schema,
        'gateway_monitor_success_threshold': gateway_monitor_success_threshold_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'gateway_ip': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'gateway_ip': getattr(IpAddr, 'unique_keys', {}),
    }



class StaticRoute(object):
    # all schemas
    prefix_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=True,
    )
    next_hop_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    if_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    route_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'prefix',
        'next_hop',
        'if_name',
        'route_id',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'prefix': prefix_schema,
        'next_hop': next_hop_schema,
        'if_name': if_name_schema,
        'route_id': route_id_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'prefix': getattr(IpAddrPrefix, 'field_references', {}),
        'next_hop': getattr(IpAddr, 'field_references', {}),
    }

    unique_keys = {
        'prefix': getattr(IpAddrPrefix, 'unique_keys', {}),
        'next_hop': getattr(IpAddr, 'unique_keys', {}),
        'my_key': 'route_id',
    }



class VrfContext(AviResource):
    resource_name = "vrfcontext"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    static_routes_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=StaticRoute.properties_schema,
        required=True,
        update_allowed=False,
    )
    static_routes_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=static_routes_item_schema,
        required=False,
        update_allowed=True,
    )
    bgp_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Bgp Local and Peer Info"),
        schema=BgpProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    gateway_mon_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=GatewayMonitor.properties_schema,
        required=True,
        update_allowed=False,
    )
    gateway_mon_schema = properties.Schema(
        properties.Schema.LIST,
        _("Enable ping based heartbeat check to gateway on the Service Engines for this Virtual Routing Context"),
        schema=gateway_mon_item_schema,
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
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
        'static_routes',
        'bgp_profile',
        'gateway_mon',
        'description',
        'cloud_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'static_routes': static_routes_schema,
        'bgp_profile': bgp_profile_schema,
        'gateway_mon': gateway_mon_schema,
        'description': description_schema,
        'cloud_uuid': cloud_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'gateway_mon': getattr(GatewayMonitor, 'field_references', {}),
        'bgp_profile': getattr(BgpProfile, 'field_references', {}),
        'static_routes': getattr(StaticRoute, 'field_references', {}),
    }

    unique_keys = {
        'gateway_mon': getattr(GatewayMonitor, 'unique_keys', {}),
        'bgp_profile': getattr(BgpProfile, 'unique_keys', {}),
        'static_routes': getattr(StaticRoute, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::VrfContext': VrfContext,
    }

