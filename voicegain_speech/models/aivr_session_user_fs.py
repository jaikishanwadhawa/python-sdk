# coding: utf-8

"""
    Voicegain Speech Recognition API v1

    # New  [RTC Callback API](#tag/aivr-callback) for building interactive speech-enabled phone applications  (IVR, Voicebots, etc.).    # Intro to Voicegain API This API is provided by [Voicegain](https://www.voicegain.ai) to its registered customers.  In addition to this API Spec document please also consult our Knowledge Base Articles: * [Web API Section](https://support.voicegain.ai/hc/en-us/categories/360001288691-Web-API) of our Knowledge Base   * [Authentication for Web API](https://support.voicegain.ai/hc/en-us/sections/360004485831-Authentication-for-Web-API) - how to generate and use JWT   * [Basic Web API Use Cases](https://support.voicegain.ai/hc/en-us/sections/360004660632-Basic-Web-API-Use-Cases)   * [Example applications using Voicegain API](https://support.voicegain.ai/hc/en-us/sections/360009682932-Example-applications-using-Voicegain-API)  **NOTE:** Most of the request and response examples in this API document are generated from schema example annotation. This may result in the response example not matching the request data example.</br> We will be adding specific examples to certain API methods if we notice that this is needed to clarify the usage.  # Speech-to-Text: Recognition vs Transcription Voicegain web api provides two types of methods for speech recognition.   + **/asr/recognize** - where the purpose is to identify what was said in a context of a more constrained set of choices.   This web api uses grammars as both a language model and a way to attach semantic meaning to spoken utterances. + **/asr/transcribe** - where the purpose is to **transcribe** speech audio word for word, no meaning is attached to transcribed text.   This web api uses large vocabulary language model.      The result of transcription can be returned in three formats. These are requested inside session[].content when making initial transcribe request:  + **Transcript** - Contains the complete text of transcription + **Words** - Intermediate results will contain new words, with timing and confidences, since the previous intermediate result. The final result will contain complete transcription. + **Word-Tree** - Contains a tree of all feasible alternatives. Use this when integrating with NL postprocessing to determine the final utterance and its meaning. + **Captions** - Intermediate results will be suitable to use as captions (this feature is in beta).  # Async Sessions: Real-Time, Semi Real-Time, and Off-Line  There are 3 types of Async ASR session that can be started:  + **REAL-TIME** - Real-time processing of streaming audio. For the recognition API, results are available within less than one second.  For the transcription API, real-time incremental results will be sent back with about 2 seconds delay.  + **OFF-LINE** - offline transcription or recognition. Has higher accuracy than REAL-TIME. Results are delivered once the complete audio has been processed.  Currently, 1 hour long audio is processed in about 10 minutes. + **SEMI-REAL-TIME** - Similar in use to REAL-TIME, but the results are available with a delay of about 30 seconds (or earlier for shorter audio). Same accuracy as OFF-LINE.  It is possible to start up to 2 simultaneous sessions attached to the same audio.   The allowed combinations of the types of two sessions are:  + REAL-TIME + SEMI-REAL-TIME - one possible use case is a combination of live transcription with transcription for online streaming (which may be delayed w.r.t of real time). The benefit of using separate SEMI-REAL-TIME session is that it has higher accuracy. + REAL-TIME + OFF-LINE - one possible use case is combination of live transcription with higher quality off-line transcription for archival purposes.  Other combinations of session types, including more than 2 sessions, are currently not supported.  Please, let us know if you think you have a valid use case for other combinations.   # Audio Input  The speech audio can be submitted in variety of ways:  + **Inline** - Short audio data can be encoded inside a request as a base64 string. + **Retrieved from URL** - Audio can be retrieved from a provided URL. The URL can also point to a live stream. + **Streamed via RTP** - Recommended only for Edge use cases (not for Cloud). + **Streamed via proprietary UDP protocol** - We provide a Java utility to do this. The utility can stream directly from an audio device, or from a file. + **Streamed via Websocket** - Can be used, e.g., to do microphone capture directly from the web browser. + **From Object Store** - Currently it works only with files uploaded to Voicegain object store, but will be expanded to support other Object Stores.   # JWT Authentication Almost all methods from this API require authentication by means of a JWT Token. A valid token can be obtained from the [Voicegain Portal](https://portal.voicegain.ai).   Each Context within the Account has its own JWT token. The accountId and contextId are encoded inside the token,  that is why API method requests do not require these in their request parameters.  More information about generating and using JWT with Voicegain API can be found in our  [Support Pages](https://support.voicegain.ai/hc/en-us/articles/360028023691-JWT-Authentication).   # noqa: E501

    The version of the OpenAPI document: 1.11.0 - updated July 31, 2020
    Contact: api.support@voicegain.ai
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ascalon_web_api_client.configuration import Configuration


class AIVRSessionUserFS(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'fs_name': 'str',
        'fs_password': 'str',
        'video_conf_index': 'int'
    }

    attribute_map = {
        'fs_name': 'fsName',
        'fs_password': 'fsPassword',
        'video_conf_index': 'videoConfIndex'
    }

    def __init__(self, fs_name=None, fs_password=None, video_conf_index=None, local_vars_configuration=None):  # noqa: E501
        """AIVRSessionUserFS - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fs_name = None
        self._fs_password = None
        self._video_conf_index = None
        self.discriminator = None

        self.fs_name = fs_name
        self.fs_password = fs_password
        if video_conf_index is not None:
            self.video_conf_index = video_conf_index

    @property
    def fs_name(self):
        """Gets the fs_name of this AIVRSessionUserFS.  # noqa: E501

        random user name under freeswitch  # noqa: E501

        :return: The fs_name of this AIVRSessionUserFS.  # noqa: E501
        :rtype: str
        """
        return self._fs_name

    @fs_name.setter
    def fs_name(self, fs_name):
        """Sets the fs_name of this AIVRSessionUserFS.

        random user name under freeswitch  # noqa: E501

        :param fs_name: The fs_name of this AIVRSessionUserFS.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and fs_name is None:  # noqa: E501
            raise ValueError("Invalid value for `fs_name`, must not be `None`")  # noqa: E501

        self._fs_name = fs_name

    @property
    def fs_password(self):
        """Gets the fs_password of this AIVRSessionUserFS.  # noqa: E501

        random password under freeswitch  # noqa: E501

        :return: The fs_password of this AIVRSessionUserFS.  # noqa: E501
        :rtype: str
        """
        return self._fs_password

    @fs_password.setter
    def fs_password(self, fs_password):
        """Sets the fs_password of this AIVRSessionUserFS.

        random password under freeswitch  # noqa: E501

        :param fs_password: The fs_password of this AIVRSessionUserFS.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and fs_password is None:  # noqa: E501
            raise ValueError("Invalid value for `fs_password`, must not be `None`")  # noqa: E501

        self._fs_password = fs_password

    @property
    def video_conf_index(self):
        """Gets the video_conf_index of this AIVRSessionUserFS.  # noqa: E501

        Index of the video conference this user will be submitting his video feed too. For example, if value of fsConferenceExtVideo is \"c_1hd7je99gjkd-ext-video-\"  and  videoConfIndex is 2 then the conference to which this user should be sending video to is \"c_1hd7je99gjkd-ext-video-2\"   # noqa: E501

        :return: The video_conf_index of this AIVRSessionUserFS.  # noqa: E501
        :rtype: int
        """
        return self._video_conf_index

    @video_conf_index.setter
    def video_conf_index(self, video_conf_index):
        """Sets the video_conf_index of this AIVRSessionUserFS.

        Index of the video conference this user will be submitting his video feed too. For example, if value of fsConferenceExtVideo is \"c_1hd7je99gjkd-ext-video-\"  and  videoConfIndex is 2 then the conference to which this user should be sending video to is \"c_1hd7je99gjkd-ext-video-2\"   # noqa: E501

        :param video_conf_index: The video_conf_index of this AIVRSessionUserFS.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                video_conf_index is not None and video_conf_index > 100):  # noqa: E501
            raise ValueError("Invalid value for `video_conf_index`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                video_conf_index is not None and video_conf_index < 1):  # noqa: E501
            raise ValueError("Invalid value for `video_conf_index`, must be a value greater than or equal to `1`")  # noqa: E501

        self._video_conf_index = video_conf_index

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AIVRSessionUserFS):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AIVRSessionUserFS):
            return True

        return self.to_dict() != other.to_dict()
