#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    Type: MMv1     ***
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
module: gcp_sql_ssl_cert
description:
- Represents an SSL certificate created for a Cloud SQL instance. To use the SSL certificate
  you must have the SSL Client Certificate and the associated SSL Client Key. The
  Client Key can be downloaded only when the SSL certificate is created with the insert
  method.
short_description: Creates a GCP SslCert
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
  cert:
    description:
    - PEM representation of the X.509 certificate.
    required: false
    type: str
  cert_serial_number:
    description:
    - Serial number, as extracted from the certificate.
    required: false
    type: str
  common_name:
    description:
    - User supplied name. Constrained to [a-zA-Z.-_ ]+.
    required: false
    type: str
  create_time:
    description:
    - The time when the certificate was created in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.
    required: false
    type: str
  expiration_time:
    description:
    - The time when the certificate expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.
    required: false
    type: str
  instance:
    description:
    - The name of the Cloud SQL instance. This does not include the project ID.
    - 'This field represents a link to a Instance resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''name'' and value of
      your resource''s name Alternatively, you can add `register: name-of-resource`
      to a gcp_sql_instance task and then set this instance field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
  sha1_fingerprint:
    description:
    - The SHA-1 of the certificate.
    required: true
    type: str
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
    - accesstoken
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
  access_token:
    description:
    - An OAuth2 access token if credential type is accesstoken.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
'''

EXAMPLES = '''
- name: create a instance
  google.cloud.gcp_sql_instance:
    name: "{{resource_name}}-2"
    settings:
      ip_configuration:
        authorized_networks:
        - name: google dns server
          value: 8.8.8.8/32
      tier: db-n1-standard-1
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instance

- name: create a SSL cert
  google.cloud.gcp_sql_ssl_cert:
    common_name: "{{resource_name}}"
    instance: "{{instance['name'}}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
cert:
  description:
  - PEM representation of the X.509 certificate.
  returned: success
  type: str
certSerialNumber:
  description:
  - Serial number, as extracted from the certificate.
  returned: success
  type: str
commonName:
  description:
  - User supplied name. Constrained to [a-zA-Z.-_ ]+.
  returned: success
  type: str
createTime:
  description:
  - The time when the certificate was created in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.
  returned: success
  type: str
expirationTime:
  description:
  - The time when the certificate expires in RFC 3339 format, for example 2012-11-15T16:19:00.094Z.
  returned: success
  type: str
instance:
  description:
  - The name of the Cloud SQL instance. This does not include the project ID.
  returned: success
  type: dict
sha1Fingerprint:
  description:
  - The SHA-1 of the certificate.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            cert=dict(type='str'),
            cert_serial_number=dict(type='str'),
            common_name=dict(type='str'),
            create_time=dict(type='str'),
            expiration_time=dict(type='str'),
            instance=dict(required=True, type='dict'),
            sha1_fingerprint=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/sqlservice.admin']

    state = module.params['state']
    kind = 'sql#sslCert'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'sql')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'sql')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'sql')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'sql#sslCert',
        u'cert': module.params.get('cert'),
        u'certSerialNumber': module.params.get('cert_serial_number'),
        u'commonName': module.params.get('common_name'),
        u'createTime': module.params.get('create_time'),
        u'expirationTime': module.params.get('expiration_time'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'sql')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    res = {'project': module.params['project'], 'instance': replace_resource_dict(module.params['instance'], 'name')}
    return "https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/sslCerts/{sha1_fingerprint}".format(**res)


def collection(module):
    res = {'project': module.params['project'], 'instance': replace_resource_dict(module.params['instance'], 'name')}
    return "https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/sslCerts".format(**res)


def return_if_object(module, response, kind, allow_not_found=False):
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
        u'cert': response.get(u'cert'),
        u'certSerialNumber': response.get(u'certSerialNumber'),
        u'commonName': response.get(u'commonName'),
        u'createTime': response.get(u'createTime'),
        u'expirationTime': response.get(u'expirationTime'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'sql#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'sql#sslCert')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'sql#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


if __name__ == '__main__':
    main()
