#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "cbb59368-5fa9-4131-bd62-462bde0be1d3")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "fd8cbd5d-a20a-4ce7-aa0d-7512ec3c86ae")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://arifqnaservices.azurewebsites.net/qnamaker")
