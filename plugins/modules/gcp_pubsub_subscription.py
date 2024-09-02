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
module: gcp_pubsub_subscription
description:
- A named resource representing the stream of messages from a single, specific topic,
  to be delivered to the subscribing application.
short_description: Creates a GCP Subscription
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
    - Name of the subscription.
    required: true
    type: str
  topic:
    description:
    - A reference to a Topic resource.
    - 'This field represents a link to a Topic resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''name'' and value of
      your resource''s name Alternatively, you can add `register: name-of-resource`
      to a gcp_pubsub_topic task and then set this topic field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
  labels:
    description:
    - A set of key/value label pairs to assign to this Subscription.
    required: false
    type: dict
  push_config:
    description:
    - If push delivery is used with this subscription, this field is used to configure
      it. An empty pushConfig signifies that the subscriber will pull and ack messages
      using API methods.
    required: false
    type: dict
    suboptions:
      oidc_token:
        description:
        - If specified, Pub/Sub will generate and attach an OIDC JWT token as an Authorization
          header in the HTTP request for every pushed message.
        required: false
        type: dict
        suboptions:
          service_account_email:
            description:
            - Service account email to be used for generating the OIDC token.
            - The caller (for subscriptions.create, subscriptions.patch, and subscriptions.modifyPushConfig
              RPCs) must have the iam.serviceAccounts.actAs permission for the service
              account.
            required: true
            type: str
          audience:
            description:
            - 'Audience to be used when generating OIDC token. The audience claim
              identifies the recipients that the JWT is intended for. The audience
              value is a single case-sensitive string. Having multiple values (array)
              for the audience field is not supported. More info about the OIDC JWT
              token audience here: U(https://tools.ietf.org/html/rfc7519#section-4.1.3)
              Note: if not specified, the Push endpoint URL will be used.'
            required: false
            type: str
      push_endpoint:
        description:
        - A URL locating the endpoint to which messages should be pushed.
        - For example, a Webhook endpoint might use "U(https://example.com/push").
        required: true
        type: str
      attributes:
        description:
        - Endpoint configuration attributes.
        - Every endpoint has a set of API supported attributes that can be used to
          control different aspects of the message delivery.
        - The currently supported attribute is x-goog-version, which you can use to
          change the format of the pushed message. This attribute indicates the version
          of the data expected by the endpoint. This controls the shape of the pushed
          message (i.e., its fields and metadata). The endpoint version is based on
          the version of the Pub/Sub API.
        - If not present during the subscriptions.create call, it will default to
          the version of the API used to make such call. If not present during a subscriptions.modifyPushConfig
          call, its value will not be changed. subscriptions.get calls will always
          return a valid version, even if the subscription was created without this
          attribute.
        - 'The possible values for this attribute are: - v1beta1: uses the push format
          defined in the v1beta1 Pub/Sub API.'
        - "- v1 or v1beta2: uses the push format defined in the v1 Pub/Sub API."
        required: false
        type: dict
  ack_deadline_seconds:
    description:
    - This value is the maximum time after a subscriber receives a message before
      the subscriber should acknowledge the message. After message delivery but before
      the ack deadline expires and before the message is acknowledged, it is an outstanding
      message and will not be delivered again during that time (on a best-effort basis).
    - For pull subscriptions, this value is used as the initial value for the ack
      deadline. To override this value for a given message, call subscriptions.modifyAckDeadline
      with the corresponding ackId if using pull. The minimum custom deadline you
      can specify is 10 seconds. The maximum custom deadline you can specify is 600
      seconds (10 minutes).
    - If this parameter is 0, a default value of 10 seconds is used.
    - For push delivery, this value is also used to set the request timeout for the
      call to the push endpoint.
    - If the subscriber never acknowledges the message, the Pub/Sub system will eventually
      redeliver the message.
    required: false
    type: int
  message_retention_duration:
    description:
    - How long to retain unacknowledged messages in the subscription's backlog, from
      the moment a message is published. If retainAckedMessages is true, then this
      also configures the retention of acknowledged messages, and thus configures
      how far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot
      be more than 7 days (`"604800s"`) or less than 10 minutes (`"600s"`).
    - 'A duration in seconds with up to nine fractional digits, terminated by ''s''.
      Example: `"600.5s"`.'
    required: false
    default: 604800s
    type: str
  retain_acked_messages:
    description:
    - Indicates whether to retain acknowledged messages. If `true`, then messages
      are not expunged from the subscription's backlog, even if they are acknowledged,
      until they fall out of the messageRetentionDuration window.
    required: false
    type: bool
  expiration_policy:
    description:
    - A policy that specifies the conditions for this subscription's expiration.
    - A subscription is considered active as long as any connected subscriber is successfully
      consuming messages from the subscription or is issuing operations on the subscription.
      If expirationPolicy is not set, a default policy with ttl of 31 days will be
      used. If it is set but ttl is "", the resource never expires. The minimum allowed
      value for expirationPolicy.ttl is 1 day.
    required: false
    type: dict
    suboptions:
      ttl:
        description:
        - Specifies the "time-to-live" duration for an associated resource. The resource
          expires if it is not active for a period of ttl.
        - If ttl is not set, the associated resource never expires.
        - A duration in seconds with up to nine fractional digits, terminated by 's'.
        - Example - "3.5s".
        required: true
        type: str
  filter:
    description:
    - The subscription only delivers the messages that match the filter. Pub/Sub automatically
      acknowledges the messages that don't match the filter. You can filter messages
      by their attributes. The maximum length of a filter is 256 bytes. After creating
      the subscription, you can't modify the filter.
    required: false
    type: str
  dead_letter_policy:
    description:
    - A policy that specifies the conditions for dead lettering messages in this subscription.
      If dead_letter_policy is not set, dead lettering is disabled.
    - The Cloud Pub/Sub service account associated with this subscription's parent
      project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com)
      must have permission to Acknowledge() messages on this subscription.
    required: false
    type: dict
    suboptions:
      dead_letter_topic:
        description:
        - The name of the topic to which dead letter messages should be published.
        - Format is `projects/{project}/topics/{topic}`.
        - The Cloud Pub/Sub service account associated with the enclosing subscription's
          parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com)
          must have permission to Publish() to this topic.
        - The operation will fail if the topic does not exist.
        - Users should ensure that there is a subscription attached to this topic
          since messages published to a topic with no subscriptions are lost.
        required: false
        type: str
      max_delivery_attempts:
        description:
        - The maximum number of delivery attempts for any message. The value must
          be between 5 and 100.
        - The number of delivery attempts is defined as 1 + (the sum of number of
          NACKs and number of times the acknowledgement deadline has been exceeded
          for the message).
        - A NACK is any call to ModifyAckDeadline with a 0 deadline. Note that client
          libraries may automatically extend ack_deadlines.
        - This field will be honored on a best effort basis.
        - If this parameter is 0, a default value of 5 is used.
        required: false
        type: int
  retry_policy:
    description:
    - A policy that specifies how Pub/Sub retries message delivery for this subscription.
    - If not set, the default retry policy is applied. This generally implies that
      messages will be retried as soon as possible for healthy subscribers. RetryPolicy
      will be triggered on NACKs or acknowledgement deadline exceeded events for a
      given message .
    required: false
    type: dict
    suboptions:
      minimum_backoff:
        description:
        - The minimum delay between consecutive deliveries of a given message. Value
          should be between 0 and 600 seconds. Defaults to 10 seconds.
        - 'A duration in seconds with up to nine fractional digits, terminated by
          ''s''. Example: "3.5s".'
        required: false
        type: str
      maximum_backoff:
        description:
        - 'The maximum delay between consecutive deliveries of a given message. Value
          should be between 0 and 600 seconds. Defaults to 600 seconds. A duration
          in seconds with up to nine fractional digits, terminated by ''s''. Example:
          "3.5s".'
        required: false
        type: str
  enable_message_ordering:
    description:
    - If `true`, messages published with the same orderingKey in PubsubMessage will
      be delivered to the subscribers in the order in which they are received by the
      Pub/Sub system. Otherwise, they may be delivered in any order.
    required: false
    type: bool
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
notes:
- 'API Reference: U(https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)'
- 'Managing Subscriptions: U(https://cloud.google.com/pubsub/docs/admin#managing_subscriptions)'
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set access_token using the C(GCP_ACCESS_TOKEN)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a topic
  google.cloud.gcp_pubsub_topic:
    name: topic-subscription
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: topic

- name: create a subscription
  google.cloud.gcp_pubsub_subscription:
    name: test_object
    topic: "{{ topic }}"
    ack_deadline_seconds: 300
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - Name of the subscription.
  returned: success
  type: str
topic:
  description:
  - A reference to a Topic resource.
  returned: success
  type: dict
labels:
  description:
  - A set of key/value label pairs to assign to this Subscription.
  returned: success
  type: dict
pushConfig:
  description:
  - If push delivery is used with this subscription, this field is used to configure
    it. An empty pushConfig signifies that the subscriber will pull and ack messages
    using API methods.
  returned: success
  type: complex
  contains:
    oidcToken:
      description:
      - If specified, Pub/Sub will generate and attach an OIDC JWT token as an Authorization
        header in the HTTP request for every pushed message.
      returned: success
      type: complex
      contains:
        serviceAccountEmail:
          description:
          - Service account email to be used for generating the OIDC token.
          - The caller (for subscriptions.create, subscriptions.patch, and subscriptions.modifyPushConfig
            RPCs) must have the iam.serviceAccounts.actAs permission for the service
            account.
          returned: success
          type: str
        audience:
          description:
          - 'Audience to be used when generating OIDC token. The audience claim identifies
            the recipients that the JWT is intended for. The audience value is a single
            case-sensitive string. Having multiple values (array) for the audience
            field is not supported. More info about the OIDC JWT token audience here:
            U(https://tools.ietf.org/html/rfc7519#section-4.1.3) Note: if not specified,
            the Push endpoint URL will be used.'
          returned: success
          type: str
    pushEndpoint:
      description:
      - A URL locating the endpoint to which messages should be pushed.
      - For example, a Webhook endpoint might use "U(https://example.com/push").
      returned: success
      type: str
    attributes:
      description:
      - Endpoint configuration attributes.
      - Every endpoint has a set of API supported attributes that can be used to control
        different aspects of the message delivery.
      - The currently supported attribute is x-goog-version, which you can use to
        change the format of the pushed message. This attribute indicates the version
        of the data expected by the endpoint. This controls the shape of the pushed
        message (i.e., its fields and metadata). The endpoint version is based on
        the version of the Pub/Sub API.
      - If not present during the subscriptions.create call, it will default to the
        version of the API used to make such call. If not present during a subscriptions.modifyPushConfig
        call, its value will not be changed. subscriptions.get calls will always return
        a valid version, even if the subscription was created without this attribute.
      - 'The possible values for this attribute are: - v1beta1: uses the push format
        defined in the v1beta1 Pub/Sub API.'
      - "- v1 or v1beta2: uses the push format defined in the v1 Pub/Sub API."
      returned: success
      type: dict
ackDeadlineSeconds:
  description:
  - This value is the maximum time after a subscriber receives a message before the
    subscriber should acknowledge the message. After message delivery but before the
    ack deadline expires and before the message is acknowledged, it is an outstanding
    message and will not be delivered again during that time (on a best-effort basis).
  - For pull subscriptions, this value is used as the initial value for the ack deadline.
    To override this value for a given message, call subscriptions.modifyAckDeadline
    with the corresponding ackId if using pull. The minimum custom deadline you can
    specify is 10 seconds. The maximum custom deadline you can specify is 600 seconds
    (10 minutes).
  - If this parameter is 0, a default value of 10 seconds is used.
  - For push delivery, this value is also used to set the request timeout for the
    call to the push endpoint.
  - If the subscriber never acknowledges the message, the Pub/Sub system will eventually
    redeliver the message.
  returned: success
  type: int
messageRetentionDuration:
  description:
  - How long to retain unacknowledged messages in the subscription's backlog, from
    the moment a message is published. If retainAckedMessages is true, then this also
    configures the retention of acknowledged messages, and thus configures how far
    back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more
    than 7 days (`"604800s"`) or less than 10 minutes (`"600s"`).
  - 'A duration in seconds with up to nine fractional digits, terminated by ''s''.
    Example: `"600.5s"`.'
  returned: success
  type: str
retainAckedMessages:
  description:
  - Indicates whether to retain acknowledged messages. If `true`, then messages are
    not expunged from the subscription's backlog, even if they are acknowledged, until
    they fall out of the messageRetentionDuration window.
  returned: success
  type: bool
expirationPolicy:
  description:
  - A policy that specifies the conditions for this subscription's expiration.
  - A subscription is considered active as long as any connected subscriber is successfully
    consuming messages from the subscription or is issuing operations on the subscription.
    If expirationPolicy is not set, a default policy with ttl of 31 days will be used.
    If it is set but ttl is "", the resource never expires. The minimum allowed value
    for expirationPolicy.ttl is 1 day.
  returned: success
  type: complex
  contains:
    ttl:
      description:
      - Specifies the "time-to-live" duration for an associated resource. The resource
        expires if it is not active for a period of ttl.
      - If ttl is not set, the associated resource never expires.
      - A duration in seconds with up to nine fractional digits, terminated by 's'.
      - Example - "3.5s".
      returned: success
      type: str
filter:
  description:
  - The subscription only delivers the messages that match the filter. Pub/Sub automatically
    acknowledges the messages that don't match the filter. You can filter messages
    by their attributes. The maximum length of a filter is 256 bytes. After creating
    the subscription, you can't modify the filter.
  returned: success
  type: str
deadLetterPolicy:
  description:
  - A policy that specifies the conditions for dead lettering messages in this subscription.
    If dead_letter_policy is not set, dead lettering is disabled.
  - The Cloud Pub/Sub service account associated with this subscription's parent project
    (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com) must have
    permission to Acknowledge() messages on this subscription.
  returned: success
  type: complex
  contains:
    deadLetterTopic:
      description:
      - The name of the topic to which dead letter messages should be published.
      - Format is `projects/{project}/topics/{topic}`.
      - The Cloud Pub/Sub service account associated with the enclosing subscription's
        parent project (i.e., service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com)
        must have permission to Publish() to this topic.
      - The operation will fail if the topic does not exist.
      - Users should ensure that there is a subscription attached to this topic since
        messages published to a topic with no subscriptions are lost.
      returned: success
      type: str
    maxDeliveryAttempts:
      description:
      - The maximum number of delivery attempts for any message. The value must be
        between 5 and 100.
      - The number of delivery attempts is defined as 1 + (the sum of number of NACKs
        and number of times the acknowledgement deadline has been exceeded for the
        message).
      - A NACK is any call to ModifyAckDeadline with a 0 deadline. Note that client
        libraries may automatically extend ack_deadlines.
      - This field will be honored on a best effort basis.
      - If this parameter is 0, a default value of 5 is used.
      returned: success
      type: int
retryPolicy:
  description:
  - A policy that specifies how Pub/Sub retries message delivery for this subscription.
  - If not set, the default retry policy is applied. This generally implies that messages
    will be retried as soon as possible for healthy subscribers. RetryPolicy will
    be triggered on NACKs or acknowledgement deadline exceeded events for a given
    message .
  returned: success
  type: complex
  contains:
    minimumBackoff:
      description:
      - The minimum delay between consecutive deliveries of a given message. Value
        should be between 0 and 600 seconds. Defaults to 10 seconds.
      - 'A duration in seconds with up to nine fractional digits, terminated by ''s''.
        Example: "3.5s".'
      returned: success
      type: str
    maximumBackoff:
      description:
      - 'The maximum delay between consecutive deliveries of a given message. Value
        should be between 0 and 600 seconds. Defaults to 600 seconds. A duration in
        seconds with up to nine fractional digits, terminated by ''s''. Example: "3.5s".'
      returned: success
      type: str
enableMessageOrdering:
  description:
  - If `true`, messages published with the same orderingKey in PubsubMessage will
    be delivered to the subscribers in the order in which they are received by the
    Pub/Sub system. Otherwise, they may be delivered in any order.
  returned: success
  type: bool
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
import re

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            topic=dict(required=True, type='dict'),
            labels=dict(type='dict'),
            push_config=dict(
                type='dict',
                options=dict(
                    oidc_token=dict(type='dict', options=dict(service_account_email=dict(required=True, type='str'), audience=dict(type='str'))),
                    push_endpoint=dict(required=True, type='str'),
                    attributes=dict(type='dict'),
                ),
            ),
            ack_deadline_seconds=dict(type='int'),
            message_retention_duration=dict(default='604800s', type='str'),
            retain_acked_messages=dict(type='bool'),
            expiration_policy=dict(type='dict', options=dict(ttl=dict(required=True, type='str'))),
            filter=dict(type='str'),
            dead_letter_policy=dict(type='dict', options=dict(dead_letter_topic=dict(type='str'), max_delivery_attempts=dict(type='int'))),
            retry_policy=dict(type='dict', options=dict(minimum_backoff=dict(type='str'), maximum_backoff=dict(type='str'))),
            enable_message_ordering=dict(type='bool'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/pubsub']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), fetch)
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, self_link(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'pubsub')
    return return_if_object(module, auth.put(link, resource_to_request(module)))


def update(module, link, fetch):
    auth = GcpSession(module, 'pubsub')
    params = {'updateMask': updateMask(resource_to_request(module), response_to_hash(module, fetch))}
    request = resource_to_request(module)
    del request['name']
    return return_if_object(module, auth.patch(link, request, params=params))


def updateMask(request, response):
    update_mask = []
    if request.get('labels') != response.get('labels'):
        update_mask.append('labels')
    if request.get('pushConfig') != response.get('pushConfig'):
        update_mask.append('pushConfig')
    if request.get('ackDeadlineSeconds') != response.get('ackDeadlineSeconds'):
        update_mask.append('ackDeadlineSeconds')
    if request.get('messageRetentionDuration') != response.get('messageRetentionDuration'):
        update_mask.append('messageRetentionDuration')
    if request.get('retainAckedMessages') != response.get('retainAckedMessages'):
        update_mask.append('retainAckedMessages')
    if request.get('expirationPolicy') != response.get('expirationPolicy'):
        update_mask.append('expirationPolicy')
    if request.get('deadLetterPolicy') != response.get('deadLetterPolicy'):
        update_mask.append('deadLetterPolicy')
    if request.get('retryPolicy') != response.get('retryPolicy'):
        update_mask.append('retryPolicy')
    return ','.join(update_mask)


def delete(module, link):
    auth = GcpSession(module, 'pubsub')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': name_pattern(module.params.get('name'), module),
        u'topic': topic_pattern(replace_resource_dict(module.params.get(u'topic', {}), 'name'), module),
        u'labels': module.params.get('labels'),
        u'pushConfig': SubscriptionPushconfig(module.params.get('push_config', {}), module).to_request(),
        u'ackDeadlineSeconds': module.params.get('ack_deadline_seconds'),
        u'messageRetentionDuration': module.params.get('message_retention_duration'),
        u'retainAckedMessages': module.params.get('retain_acked_messages'),
        u'expirationPolicy': SubscriptionExpirationpolicy(module.params.get('expiration_policy', {}), module).to_request(),
        u'filter': module.params.get('filter'),
        u'deadLetterPolicy': SubscriptionDeadletterpolicy(module.params.get('dead_letter_policy', {}), module).to_request(),
        u'retryPolicy': SubscriptionRetrypolicy(module.params.get('retry_policy', {}), module).to_request(),
        u'enableMessageOrdering': module.params.get('enable_message_ordering'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'pubsub')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://pubsub.googleapis.com/v1/projects/{project}/subscriptions/{name}".format(**module.params)


def collection(module):
    return "https://pubsub.googleapis.com/v1/projects/{project}/subscriptions".format(**module.params)


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
        u'name': name_pattern(module.params.get('name'), module),
        u'topic': topic_pattern(replace_resource_dict(module.params.get(u'topic', {}), 'name'), module),
        u'labels': response.get(u'labels'),
        u'pushConfig': SubscriptionPushconfig(response.get(u'pushConfig', {}), module).from_response(),
        u'ackDeadlineSeconds': response.get(u'ackDeadlineSeconds'),
        u'messageRetentionDuration': response.get(u'messageRetentionDuration'),
        u'retainAckedMessages': response.get(u'retainAckedMessages'),
        u'expirationPolicy': SubscriptionExpirationpolicy(response.get(u'expirationPolicy', {}), module).from_response(),
        u'filter': module.params.get('filter'),
        u'deadLetterPolicy': SubscriptionDeadletterpolicy(response.get(u'deadLetterPolicy', {}), module).from_response(),
        u'retryPolicy': SubscriptionRetrypolicy(response.get(u'retryPolicy', {}), module).from_response(),
        u'enableMessageOrdering': module.params.get('enable_message_ordering'),
    }


def name_pattern(name, module):
    if name is None:
        return

    regex = r"projects/.*/subscriptions/.*"

    if not re.match(regex, name):
        name = "projects/{project}/subscriptions/{name}".format(**module.params)

    return name


def topic_pattern(name, module):
    if name is None:
        return

    regex = r"projects/.*/topics/.*"

    if not re.match(regex, name):
        formatted_params = {
            'project': module.params['project'],
            'topic': replace_resource_dict(module.params['topic'], 'name'),
        }
        name = "projects/{project}/topics/{topic}".format(**formatted_params)

    return name


class SubscriptionPushconfig(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'oidcToken': SubscriptionOidctoken(self.request.get('oidc_token', {}), self.module).to_request(),
                u'pushEndpoint': self.request.get('push_endpoint'),
                u'attributes': self.request.get('attributes'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'oidcToken': SubscriptionOidctoken(self.request.get(u'oidcToken', {}), self.module).from_response(),
                u'pushEndpoint': self.request.get(u'pushEndpoint'),
                u'attributes': self.request.get(u'attributes'),
            }
        )


class SubscriptionOidctoken(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'serviceAccountEmail': self.request.get('service_account_email'), u'audience': self.request.get('audience')})

    def from_response(self):
        return remove_nones_from_dict({u'serviceAccountEmail': self.request.get(u'serviceAccountEmail'), u'audience': self.request.get(u'audience')})


class SubscriptionExpirationpolicy(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'ttl': self.request.get('ttl')})

    def from_response(self):
        return remove_nones_from_dict({u'ttl': self.request.get(u'ttl')})


class SubscriptionDeadletterpolicy(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {u'deadLetterTopic': self.request.get('dead_letter_topic'), u'maxDeliveryAttempts': self.request.get('max_delivery_attempts')}
        )

    def from_response(self):
        return remove_nones_from_dict(
            {u'deadLetterTopic': self.request.get(u'deadLetterTopic'), u'maxDeliveryAttempts': self.request.get(u'maxDeliveryAttempts')}
        )


class SubscriptionRetrypolicy(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'minimumBackoff': self.request.get('minimum_backoff'), u'maximumBackoff': self.request.get('maximum_backoff')})

    def from_response(self):
        return remove_nones_from_dict({u'minimumBackoff': self.request.get(u'minimumBackoff'), u'maximumBackoff': self.request.get(u'maximumBackoff')})


if __name__ == '__main__':
    main()
