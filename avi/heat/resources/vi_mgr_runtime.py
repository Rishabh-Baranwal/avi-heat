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
from vi_mgr_common import *


class VIMgrVcenterRuntime(AviResource):
    resource_name = "vimgrvcenterruntime"
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['CLOUD_VCENTER', 'CLOUD_DOCKER_UCP', 'CLOUD_APIC', 'CLOUD_OPENSTACK', 'CLOUD_MESOS', 'CLOUD_RANCHER', 'CLOUD_VCA', 'CLOUD_LINUXSERVER', 'CLOUD_OSHIFT_K8S', 'CLOUD_AWS', 'CLOUD_NONE']),
        ],
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    vcenter_url_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    username_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    password_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    datacenter_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    datacenter_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=datacenter_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    privilege_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['WRITE_ACCESS', 'READ_ACCESS', 'NO_ACCESS']),
        ],
    )
    inventory_state_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['VCENTER_DISCOVERY_COMPLETE_PER_TENANT_IP_ROUTE', 'VCENTER_DISCOVERY_FAILURE', 'VCENTER_DISCOVERY_ONGOING', 'VCENTER_DISCOVERY_MAKING_SE_OVA', 'VCENTER_DISCOVERY_WAITING_DC', 'VCENTER_DISCOVERY_RETRIEVING_NW', 'VCENTER_DISCOVERY_RESYNCING', 'VCENTER_DISCOVERY_COMPLETE_NO_MGMT_NW', 'VCENTER_DISCOVERY_RETRIEVING_DC', 'VCENTER_DISCOVERY_BAD_CREDENTIALS', 'VCENTER_DISCOVERY_COMPLETE', 'VCENTER_DISCOVERY_DELETING_VCENTER']),
        ],
    )
    discovered_datacenter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    progress_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_dcs_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_hosts_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_clusters_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_vms_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_nws_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_vcenter_req_pending_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    disc_start_time_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    disc_end_time_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    management_network_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    inventory_progress_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    apic_mode_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    vcenter_template_se_location_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    api_version_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    vcenter_fullname_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    vcenter_connected_schema = properties.Schema(
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
        'type',
        'name',
        'vcenter_url',
        'username',
        'password',
        'datacenter_uuids',
        'privilege',
        'inventory_state',
        'discovered_datacenter',
        'progress',
        'num_dcs',
        'num_hosts',
        'num_clusters',
        'num_vms',
        'num_nws',
        'num_vcenter_req_pending',
        'disc_start_time',
        'disc_end_time',
        'management_network',
        'inventory_progress',
        'apic_mode',
        'vcenter_template_se_location',
        'api_version',
        'vcenter_fullname',
        'vcenter_connected',
        'cloud_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'name': name_schema,
        'vcenter_url': vcenter_url_schema,
        'username': username_schema,
        'password': password_schema,
        'datacenter_uuids': datacenter_uuids_schema,
        'privilege': privilege_schema,
        'inventory_state': inventory_state_schema,
        'discovered_datacenter': discovered_datacenter_schema,
        'progress': progress_schema,
        'num_dcs': num_dcs_schema,
        'num_hosts': num_hosts_schema,
        'num_clusters': num_clusters_schema,
        'num_vms': num_vms_schema,
        'num_nws': num_nws_schema,
        'num_vcenter_req_pending': num_vcenter_req_pending_schema,
        'disc_start_time': disc_start_time_schema,
        'disc_end_time': disc_end_time_schema,
        'management_network': management_network_schema,
        'inventory_progress': inventory_progress_schema,
        'apic_mode': apic_mode_schema,
        'vcenter_template_se_location': vcenter_template_se_location_schema,
        'api_version': api_version_schema,
        'vcenter_fullname': vcenter_fullname_schema,
        'vcenter_connected': vcenter_connected_schema,
        'cloud_uuid': cloud_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'datacenter_uuids': 'vimgrdcruntime',
    }



class VIMgrHostRuntime(AviResource):
    resource_name = "vimgrhostruntime"
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['CLOUD_VCENTER', 'CLOUD_DOCKER_UCP', 'CLOUD_APIC', 'CLOUD_OPENSTACK', 'CLOUD_MESOS', 'CLOUD_RANCHER', 'CLOUD_VCA', 'CLOUD_LINUXSERVER', 'CLOUD_OSHIFT_K8S', 'CLOUD_AWS', 'CLOUD_NONE']),
        ],
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    managed_object_id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    cluster_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    cluster_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_cpu_packages_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_cpu_cores_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    num_cpu_threads_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    cpu_hz_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    mem_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    pnics_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CdpLldpInfo.properties_schema,
        required=True,
        update_allowed=False,
    )
    pnics_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=pnics_item_schema,
        required=False,
        update_allowed=True,
    )
    vm_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    vm_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=vm_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    mgmt_portgroup_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    powerstate_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    maintenance_mode_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    connection_state_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    quarantined_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    quarantine_start_ts_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    quarantined_periods_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    cntlr_accessible_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    network_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    network_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=network_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    se_fail_cnt_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    se_success_cnt_schema = properties.Schema(
        properties.Schema.NUMBER,
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
        'type',
        'name',
        'managed_object_id',
        'cluster_name',
        'cluster_uuid',
        'num_cpu_packages',
        'num_cpu_cores',
        'num_cpu_threads',
        'cpu_hz',
        'mem',
        'pnics',
        'vm_uuids',
        'mgmt_portgroup',
        'powerstate',
        'maintenance_mode',
        'connection_state',
        'quarantined',
        'quarantine_start_ts',
        'quarantined_periods',
        'cntlr_accessible',
        'network_uuids',
        'se_fail_cnt',
        'se_success_cnt',
        'cloud_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'name': name_schema,
        'managed_object_id': managed_object_id_schema,
        'cluster_name': cluster_name_schema,
        'cluster_uuid': cluster_uuid_schema,
        'num_cpu_packages': num_cpu_packages_schema,
        'num_cpu_cores': num_cpu_cores_schema,
        'num_cpu_threads': num_cpu_threads_schema,
        'cpu_hz': cpu_hz_schema,
        'mem': mem_schema,
        'pnics': pnics_schema,
        'vm_uuids': vm_uuids_schema,
        'mgmt_portgroup': mgmt_portgroup_schema,
        'powerstate': powerstate_schema,
        'maintenance_mode': maintenance_mode_schema,
        'connection_state': connection_state_schema,
        'quarantined': quarantined_schema,
        'quarantine_start_ts': quarantine_start_ts_schema,
        'quarantined_periods': quarantined_periods_schema,
        'cntlr_accessible': cntlr_accessible_schema,
        'network_uuids': network_uuids_schema,
        'se_fail_cnt': se_fail_cnt_schema,
        'se_success_cnt': se_success_cnt_schema,
        'cloud_uuid': cloud_uuid_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'pnics': getattr(CdpLldpInfo, 'field_references', {}),
        'vm_uuids': 'vimgrvmruntime',
    }

    unique_keys = {
        'pnics': getattr(CdpLldpInfo, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::VIMgrVcenterRuntime': VIMgrVcenterRuntime,
        'Avi::LBaaS::VIMgrHostRuntime': VIMgrHostRuntime,
    }

