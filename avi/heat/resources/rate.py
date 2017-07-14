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
from action import *


class RateLimiterAction(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of action to be enforced upon hitting the rate limit."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['RL_ACTION_RESET_CONN', 'RL_ACTION_LOCAL_RSP', 'RL_ACTION_DROP_CONN', 'RL_ACTION_CLOSE_CONN', 'RL_ACTION_NONE', 'RL_ACTION_REDIRECT']),
        ],
    )
    redirect_schema = properties.Schema(
        properties.Schema.MAP,
        _("Parameters for HTTP Redirect rate limit action."),
        schema=HTTPRedirectAction.properties_schema,
        required=False,
        update_allowed=True,
    )
    status_code_schema = properties.Schema(
        properties.Schema.STRING,
        _("HTTP status code for Local Response rate limit action."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HTTP_LOCAL_RESPONSE_STATUS_CODE_403', 'HTTP_LOCAL_RESPONSE_STATUS_CODE_429', 'HTTP_LOCAL_RESPONSE_STATUS_CODE_200', 'HTTP_LOCAL_RESPONSE_STATUS_CODE_404']),
        ],
    )
    file_schema = properties.Schema(
        properties.Schema.MAP,
        _("File to be used for HTTP Local response rate limit action."),
        schema=HTTPLocalFile.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'type',
        'redirect',
        'status_code',
        'file',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'redirect': redirect_schema,
        'status_code': status_code_schema,
        'file': file_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'redirect': getattr(HTTPRedirectAction, 'field_references', {}),
        'file': getattr(HTTPLocalFile, 'field_references', {}),
    }

    unique_keys = {
        'redirect': getattr(HTTPRedirectAction, 'unique_keys', {}),
        'file': getattr(HTTPLocalFile, 'unique_keys', {}),
    }



class EquivalentLabels(object):
    # all schemas
    labels_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    labels_schema = properties.Schema(
        properties.Schema.LIST,
        _("Equivalent labels."),
        schema=labels_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'labels',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'labels': labels_schema,
    }



class RateProfile(object):
    # all schemas
    count_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of connections or requests or packets"),
        required=False,
        update_allowed=True,
    )
    burst_sz_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of connections or requests or packets to be let through instantaneously"),
        required=False,
        update_allowed=True,
    )
    period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time value in seconds to enforce rate count"),
        required=False,
        update_allowed=True,
    )
    explicit_tracking_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Explicitly tracks an attacker across rate periods"),
        required=False,
        update_allowed=True,
    )
    fine_grain_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable fine granularity"),
        required=False,
        update_allowed=True,
    )
    action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Action to perform upon rate limiting"),
        schema=RateLimiterAction.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'count',
        'burst_sz',
        'period',
        'explicit_tracking',
        'fine_grain',
        'action',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'count': count_schema,
        'burst_sz': burst_sz_schema,
        'period': period_schema,
        'explicit_tracking': explicit_tracking_schema,
        'fine_grain': fine_grain_schema,
        'action': action_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'action': getattr(RateLimiterAction, 'field_references', {}),
    }

    unique_keys = {
        'action': getattr(RateLimiterAction, 'unique_keys', {}),
    }



class RateLimiterProfile(object):
    # all schemas
    client_ip_connections_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit all connections made from any single client IP address to the Virtual Service."),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_ip_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit all HTTP requests from any single client IP address to all URLs of the Virtual Service."),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    uri_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit all HTTP requests from all client IP addresses to any single URL."),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_ip_to_uri_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit all HTTP requests from any single client IP address to any single URL."),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_ip_failed_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit all requests from a client for a specified period of time once the count of failed requests from that client crosses a threshold for that period. Clients are tracked based on their IP address. Count and time period are specified through the RateProfile. Requests are deemed failed based on client or server side error status codes, consistent with how Avi Logs and Metrics subsystems mark failed requests. "),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    uri_failed_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit all requests to a URI for a specified period of time once the count of failed requests to that URI crosses a threshold for that period. Count and time period are specified through the RateProfile. Requests are deemed failed based on client or server side error status codes, consistent with how Avi Logs and Metrics subsystems mark failed requests. "),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_ip_to_uri_failed_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit all requests from a client to a URI for a specified period of time once the count of failed requests from that client to the URI crosses a threshold for that period. Clients are tracked based on their IP address. Count and time period are specified through the RateProfile. Requests are deemed failed based on client or server side error status codes, consistent with how Avi Logs and Metrics subsystems mark failed requests. "),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    client_ip_scanners_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Automatically track clients and classify them into 3 groups - Good, Bad, Unknown. Clients are tracked based on their IP Address. Clients are added to the Good group when the Avi Scan Detection system builds history of requests from them that complete successfully. Clients are added to Unknown group when there is insufficient history about them. Requests from such clients are rate limited to the rate specified in the RateProfile. Finally, Clients with history of failed requests are added to Bad group and their requests are rate limited with stricter thresholds than the Unknown Clients group. The Avi Scan Detection system automatically tunes itself so that the Good, Bad, and Unknown client IPs group membership changes dynamically with the changes in traffic patterns through the ADC."),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    uri_scanners_requests_rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Automatically track URIs and classify them into 3 groups - Good, Bad, Unknown. URIs are added to the Good group when the Avi Scan Detection system builds history of requests to URIs that complete successfully. URIs are added to Unknown group when there is insufficient history about them. Requests for such URIs are rate limited to the rate specified in the RateProfile. Finally, URIs with history of failed requests are added to Bad group and requests to them are rate limited with stricter thresholds than the Unknown URIs group. The Avi Scan Detection system automatically tunes itself so that the Good, Bad, and Unknown URIs group membership changes dynamically with the changes in traffic patterns through the ADC."),
        schema=RateProfile.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'client_ip_connections_rate_limit',
        'client_ip_requests_rate_limit',
        'uri_requests_rate_limit',
        'client_ip_to_uri_requests_rate_limit',
        'client_ip_failed_requests_rate_limit',
        'uri_failed_requests_rate_limit',
        'client_ip_to_uri_failed_requests_rate_limit',
        'client_ip_scanners_requests_rate_limit',
        'uri_scanners_requests_rate_limit',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'client_ip_connections_rate_limit': client_ip_connections_rate_limit_schema,
        'client_ip_requests_rate_limit': client_ip_requests_rate_limit_schema,
        'uri_requests_rate_limit': uri_requests_rate_limit_schema,
        'client_ip_to_uri_requests_rate_limit': client_ip_to_uri_requests_rate_limit_schema,
        'client_ip_failed_requests_rate_limit': client_ip_failed_requests_rate_limit_schema,
        'uri_failed_requests_rate_limit': uri_failed_requests_rate_limit_schema,
        'client_ip_to_uri_failed_requests_rate_limit': client_ip_to_uri_failed_requests_rate_limit_schema,
        'client_ip_scanners_requests_rate_limit': client_ip_scanners_requests_rate_limit_schema,
        'uri_scanners_requests_rate_limit': uri_scanners_requests_rate_limit_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'uri_failed_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'client_ip_scanners_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'client_ip_to_uri_failed_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'client_ip_to_uri_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'uri_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'uri_scanners_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'client_ip_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'client_ip_failed_requests_rate_limit': getattr(RateProfile, 'field_references', {}),
        'client_ip_connections_rate_limit': getattr(RateProfile, 'field_references', {}),
    }

    unique_keys = {
        'uri_failed_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'client_ip_scanners_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'client_ip_to_uri_failed_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'client_ip_to_uri_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'uri_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'uri_scanners_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'client_ip_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'client_ip_failed_requests_rate_limit': getattr(RateProfile, 'unique_keys', {}),
        'client_ip_connections_rate_limit': getattr(RateProfile, 'unique_keys', {}),
    }

