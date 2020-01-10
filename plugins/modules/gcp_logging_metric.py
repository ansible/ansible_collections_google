#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#     ***     DIFF TEST DIFF TEST    ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_logging_metric
description:
- Logs-based metric can also be used to extract values from logs and create a a distribution
  of the values. The distribution records the statistics of the extracted values along
  with an optional histogram of the values as specified by the bucket options.
short_description: Creates a GCP Metric
version_added: '2.10'
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  name:
    description:
    - The client-assigned metric identifier. Examples - "error_count", "nginx/requests".
    - Metric identifiers are limited to 100 characters and can include only the following
      characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash
      character (/) denotes a hierarchy of name pieces, and it cannot be the first
      character of the name.
    required: true
    type: str
  description:
    description:
    - A description of this metric, which is used in documentation. The maximum length
      of the description is 8000 characters.
    required: false
    type: str
  filter:
    description:
    - An advanced logs filter (U(https://cloud.google.com/logging/docs/view/advanced-filters))
      which is used to match log entries.
    required: true
    type: str
  metric_descriptor:
    description:
    - The metric descriptor associated with the logs-based metric.
    required: true
    type: dict
    suboptions:
      unit:
        description:
        - The unit in which the metric value is reported. It is only applicable if
          the valueType is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The supported units
          are a subset of [The Unified Code for Units of Measure](U(http://unitsofmeasure.org/ucum.html))
          standard .
        required: false
        default: '1'
        type: str
      value_type:
        description:
        - Whether the measurement is an integer, a floating-point number, etc.
        - Some combinations of metricKind and valueType might not be supported.
        - For counter metrics, set this to INT64.
        - 'Some valid choices include: "BOOL", "INT64", "DOUBLE", "STRING", "DISTRIBUTION",
          "MONEY"'
        required: true
        type: str
      metric_kind:
        description:
        - Whether the metric records instantaneous values, changes to a value, etc.
        - Some combinations of metricKind and valueType might not be supported.
        - For counter metrics, set this to DELTA.
        - 'Some valid choices include: "DELTA", "GAUGE", "CUMULATIVE"'
        required: true
        type: str
      labels:
        description:
        - The set of labels that can be used to describe a specific instance of this
          metric type. For example, the appengine.googleapis.com/http/server/response_latencies
          metric type has a label for the HTTP response code, response_code, so you
          can look at latencies for successful responses or just for responses that
          failed.
        required: false
        type: list
        suboptions:
          key:
            description:
            - The label key.
            required: true
            type: str
          description:
            description:
            - A human-readable description for the label.
            required: false
            type: str
          value_type:
            description:
            - The type of data that can be assigned to the label.
            - 'Some valid choices include: "BOOL", "INT64", "STRING"'
            required: false
            default: STRING
            type: str
      display_name:
        description:
        - A concise name for the metric, which can be displayed in user interfaces.
          Use sentence case without an ending period, for example "Request count".
          This field is optional but it is recommended to be set for any metrics associated
          with user-visible concepts, such as Quota.
        required: false
        type: str
  label_extractors:
    description:
    - A map from a label key string to an extractor expression which is used to extract
      data from a log entry field and assign as the label value. Each label key specified
      in the LabelDescriptor must have an associated extractor expression in this
      map. The syntax of the extractor expression is the same as for the valueExtractor
      field.
    required: false
    type: dict
  value_extractor:
    description:
    - A valueExtractor is required when using a distribution logs-based metric to
      extract the values to record from a log entry. Two functions are supported for
      value extraction - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument
      are 1. field - The name of the log entry field from which the value is to be
      extracted. 2. regex - A regular expression using the Google RE2 syntax (U(https://github.com/google/re2/wiki/Syntax))
      with a single capture group to extract data from the specified log entry field.
      The value of the field is converted to a string before applying the regex. It
      is an error to specify a regex that does not include exactly one capture group.
    required: false
    type: str
  bucket_options:
    description:
    - The bucketOptions are required when the logs-based metric is using a DISTRIBUTION
      value type and it describes the bucket boundaries used to create a histogram
      of the extracted values.
    required: false
    type: dict
    suboptions:
      linear_buckets:
        description:
        - Specifies a linear sequence of buckets that all have the same width (except
          overflow and underflow).
        - Each bucket represents a constant absolute uncertainty on the specific value
          in the bucket.
        required: false
        type: dict
        suboptions:
          num_finite_buckets:
            description:
            - Must be greater than 0.
            required: false
            type: int
          width:
            description:
            - Must be greater than 0.
            required: false
            type: int
          offset:
            description:
            - Lower bound of the first bucket.
            required: false
            type: str
      exponential_buckets:
        description:
        - Specifies an exponential sequence of buckets that have a width that is proportional
          to the value of the lower bound. Each bucket represents a constant relative
          uncertainty on a specific value in the bucket.
        required: false
        type: dict
        suboptions:
          num_finite_buckets:
            description:
            - Must be greater than 0.
            required: false
            type: int
          growth_factor:
            description:
            - Must be greater than 1.
            required: false
            type: str
          scale:
            description:
            - Must be greater than 0.
            required: false
            type: str
      explicit_buckets:
        description:
        - Specifies a set of buckets with arbitrary widths.
        required: false
        type: dict
        suboptions:
          bounds:
            description:
            - The values must be monotonically increasing.
            required: true
            type: list
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create)'
- 'Official Documentation: U(https://cloud.google.com/logging/docs/apis)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a metric
  google.cloud.gcp_logging_metric:
    name: test_object
    filter: resource.type=gae_app AND severity>=ERROR
    metric_descriptor:
      metric_kind: DELTA
      value_type: DISTRIBUTION
      unit: '1'
      labels:
      - key: mass
        value_type: STRING
        description: amount of matter
    value_extractor: EXTRACT(jsonPayload.request)
    label_extractors:
      mass: EXTRACT(jsonPayload.request)
    bucket_options:
      linear_buckets:
        num_finite_buckets: 3
        width: 1
        offset: 1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The client-assigned metric identifier. Examples - "error_count", "nginx/requests".
  - Metric identifiers are limited to 100 characters and can include only the following
    characters A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash
    character (/) denotes a hierarchy of name pieces, and it cannot be the first character
    of the name.
  returned: success
  type: str
description:
  description:
  - A description of this metric, which is used in documentation. The maximum length
    of the description is 8000 characters.
  returned: success
  type: str
filter:
  description:
  - An advanced logs filter (U(https://cloud.google.com/logging/docs/view/advanced-filters))
    which is used to match log entries.
  returned: success
  type: str
metricDescriptor:
  description:
  - The metric descriptor associated with the logs-based metric.
  returned: success
  type: complex
  contains:
    unit:
      description:
      - The unit in which the metric value is reported. It is only applicable if the
        valueType is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The supported units are
        a subset of [The Unified Code for Units of Measure](U(http://unitsofmeasure.org/ucum.html))
        standard .
      returned: success
      type: str
    valueType:
      description:
      - Whether the measurement is an integer, a floating-point number, etc.
      - Some combinations of metricKind and valueType might not be supported.
      - For counter metrics, set this to INT64.
      returned: success
      type: str
    metricKind:
      description:
      - Whether the metric records instantaneous values, changes to a value, etc.
      - Some combinations of metricKind and valueType might not be supported.
      - For counter metrics, set this to DELTA.
      returned: success
      type: str
    labels:
      description:
      - The set of labels that can be used to describe a specific instance of this
        metric type. For example, the appengine.googleapis.com/http/server/response_latencies
        metric type has a label for the HTTP response code, response_code, so you
        can look at latencies for successful responses or just for responses that
        failed.
      returned: success
      type: complex
      contains:
        key:
          description:
          - The label key.
          returned: success
          type: str
        description:
          description:
          - A human-readable description for the label.
          returned: success
          type: str
        valueType:
          description:
          - The type of data that can be assigned to the label.
          returned: success
          type: str
    displayName:
      description:
      - A concise name for the metric, which can be displayed in user interfaces.
        Use sentence case without an ending period, for example "Request count". This
        field is optional but it is recommended to be set for any metrics associated
        with user-visible concepts, such as Quota.
      returned: success
      type: str
labelExtractors:
  description:
  - A map from a label key string to an extractor expression which is used to extract
    data from a log entry field and assign as the label value. Each label key specified
    in the LabelDescriptor must have an associated extractor expression in this map.
    The syntax of the extractor expression is the same as for the valueExtractor field.
  returned: success
  type: dict
valueExtractor:
  description:
  - A valueExtractor is required when using a distribution logs-based metric to extract
    the values to record from a log entry. Two functions are supported for value extraction
    - EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are 1. field -
    The name of the log entry field from which the value is to be extracted. 2. regex
    - A regular expression using the Google RE2 syntax (U(https://github.com/google/re2/wiki/Syntax))
    with a single capture group to extract data from the specified log entry field.
    The value of the field is converted to a string before applying the regex. It
    is an error to specify a regex that does not include exactly one capture group.
  returned: success
  type: str
bucketOptions:
  description:
  - The bucketOptions are required when the logs-based metric is using a DISTRIBUTION
    value type and it describes the bucket boundaries used to create a histogram of
    the extracted values.
  returned: success
  type: complex
  contains:
    linearBuckets:
      description:
      - Specifies a linear sequence of buckets that all have the same width (except
        overflow and underflow).
      - Each bucket represents a constant absolute uncertainty on the specific value
        in the bucket.
      returned: success
      type: complex
      contains:
        numFiniteBuckets:
          description:
          - Must be greater than 0.
          returned: success
          type: int
        width:
          description:
          - Must be greater than 0.
          returned: success
          type: int
        offset:
          description:
          - Lower bound of the first bucket.
          returned: success
          type: str
    exponentialBuckets:
      description:
      - Specifies an exponential sequence of buckets that have a width that is proportional
        to the value of the lower bound. Each bucket represents a constant relative
        uncertainty on a specific value in the bucket.
      returned: success
      type: complex
      contains:
        numFiniteBuckets:
          description:
          - Must be greater than 0.
          returned: success
          type: int
        growthFactor:
          description:
          - Must be greater than 1.
          returned: success
          type: str
        scale:
          description:
          - Must be greater than 0.
          returned: success
          type: str
    explicitBuckets:
      description:
      - Specifies a set of buckets with arbitrary widths.
      returned: success
      type: complex
      contains:
        bounds:
          description:
          - The values must be monotonically increasing.
          returned: success
          type: list
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import (
    navigate_hash,
    GcpSession,
    GcpModule,
    GcpRequest,
    remove_nones_from_dict,
    replace_resource_dict,
)
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            filter=dict(required=True, type='str'),
            metric_descriptor=dict(
                required=True,
                type='dict',
                options=dict(
                    unit=dict(default='1', type='str'),
                    value_type=dict(required=True, type='str'),
                    metric_kind=dict(required=True, type='str'),
                    labels=dict(
                        type='list',
                        elements='dict',
                        options=dict(key=dict(required=True, type='str'), description=dict(type='str'), value_type=dict(default='STRING', type='str')),
                    ),
                    display_name=dict(type='str'),
                ),
            ),
            label_extractors=dict(type='dict'),
            value_extractor=dict(type='str'),
            bucket_options=dict(
                type='dict',
                options=dict(
                    linear_buckets=dict(type='dict', options=dict(num_finite_buckets=dict(type='int'), width=dict(type='int'), offset=dict(type='str'))),
                    exponential_buckets=dict(
                        type='dict', options=dict(num_finite_buckets=dict(type='int'), growth_factor=dict(type='str'), scale=dict(type='str'))
                    ),
                    explicit_buckets=dict(type='dict', options=dict(bounds=dict(required=True, type='list', elements='str'))),
                ),
            ),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'logging')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    auth = GcpSession(module, 'logging')
    return return_if_object(module, auth.put(link, resource_to_request(module)))


def delete(module, link):
    auth = GcpSession(module, 'logging')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'filter': module.params.get('filter'),
        u'metricDescriptor': MetricMetricdescriptor(module.params.get('metric_descriptor', {}), module).to_request(),
        u'labelExtractors': module.params.get('label_extractors'),
        u'valueExtractor': module.params.get('value_extractor'),
        u'bucketOptions': MetricBucketoptions(module.params.get('bucket_options', {}), module).to_request(),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'logging')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://logging.googleapis.com/v2/projects/{project}/metrics/{name}".format(**module.params)


def collection(module):
    return "https://logging.googleapis.com/v2/projects/{project}/metrics".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'name': response.get(u'name'),
        u'description': response.get(u'description'),
        u'filter': response.get(u'filter'),
        u'metricDescriptor': MetricMetricdescriptor(response.get(u'metricDescriptor', {}), module).from_response(),
        u'labelExtractors': response.get(u'labelExtractors'),
        u'valueExtractor': response.get(u'valueExtractor'),
        u'bucketOptions': MetricBucketoptions(response.get(u'bucketOptions', {}), module).from_response(),
    }


class MetricMetricdescriptor(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'unit': self.request.get('unit'),
                u'valueType': self.request.get('value_type'),
                u'metricKind': self.request.get('metric_kind'),
                u'labels': MetricLabelsArray(self.request.get('labels', []), self.module).to_request(),
                u'displayName': self.request.get('display_name'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'unit': self.request.get(u'unit'),
                u'valueType': self.request.get(u'valueType'),
                u'metricKind': self.request.get(u'metricKind'),
                u'labels': MetricLabelsArray(self.request.get(u'labels', []), self.module).from_response(),
                u'displayName': self.request.get(u'displayName'),
            }
        )


class MetricLabelsArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'key': item.get('key'), u'description': item.get('description'), u'valueType': item.get('value_type')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'key': item.get(u'key'), u'description': item.get(u'description'), u'valueType': item.get(u'valueType')})


class MetricBucketoptions(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'linearBuckets': MetricLinearbuckets(self.request.get('linear_buckets', {}), self.module).to_request(),
                u'exponentialBuckets': MetricExponentialbuckets(self.request.get('exponential_buckets', {}), self.module).to_request(),
                u'explicitBuckets': MetricExplicitbuckets(self.request.get('explicit_buckets', {}), self.module).to_request(),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'linearBuckets': MetricLinearbuckets(self.request.get(u'linearBuckets', {}), self.module).from_response(),
                u'exponentialBuckets': MetricExponentialbuckets(self.request.get(u'exponentialBuckets', {}), self.module).from_response(),
                u'explicitBuckets': MetricExplicitbuckets(self.request.get(u'explicitBuckets', {}), self.module).from_response(),
            }
        )


class MetricLinearbuckets(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {u'numFiniteBuckets': self.request.get('num_finite_buckets'), u'width': self.request.get('width'), u'offset': self.request.get('offset')}
        )

    def from_response(self):
        return remove_nones_from_dict(
            {u'numFiniteBuckets': self.request.get(u'numFiniteBuckets'), u'width': self.request.get(u'width'), u'offset': self.request.get(u'offset')}
        )


class MetricExponentialbuckets(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'numFiniteBuckets': self.request.get('num_finite_buckets'),
                u'growthFactor': self.request.get('growth_factor'),
                u'scale': self.request.get('scale'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'numFiniteBuckets': self.request.get(u'numFiniteBuckets'),
                u'growthFactor': self.request.get(u'growthFactor'),
                u'scale': self.request.get(u'scale'),
            }
        )


class MetricExplicitbuckets(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'bounds': self.request.get('bounds')})

    def from_response(self):
        return remove_nones_from_dict({u'bounds': self.request.get(u'bounds')})


if __name__ == '__main__':
    main()
