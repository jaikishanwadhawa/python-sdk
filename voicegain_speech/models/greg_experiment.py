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


class GregExperiment(object):
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
        'experiment_id': 'str',
        'account_id': 'str',
        'context_id': 'str',
        'audio_set_id': 'str',
        'date': 'str',
        'grammar_id': 'str',
        'name': 'str',
        'platform': 'ExperimentPlatform',
        'platform_data': 'GregExperimentBasePlatformData',
        'question_id': 'str',
        'status': 'GregExperimentStatus'
    }

    attribute_map = {
        'experiment_id': 'experimentId',
        'account_id': 'accountId',
        'context_id': 'contextId',
        'audio_set_id': 'audioSetId',
        'date': 'date',
        'grammar_id': 'grammarId',
        'name': 'name',
        'platform': 'platform',
        'platform_data': 'platformData',
        'question_id': 'questionId',
        'status': 'status'
    }

    def __init__(self, experiment_id=None, account_id=None, context_id=None, audio_set_id=None, date=None, grammar_id=None, name=None, platform=None, platform_data=None, question_id=None, status=None, local_vars_configuration=None):  # noqa: E501
        """GregExperiment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._experiment_id = None
        self._account_id = None
        self._context_id = None
        self._audio_set_id = None
        self._date = None
        self._grammar_id = None
        self._name = None
        self._platform = None
        self._platform_data = None
        self._question_id = None
        self._status = None
        self.discriminator = None

        self.experiment_id = experiment_id
        self.account_id = account_id
        self.context_id = context_id
        if audio_set_id is not None:
            self.audio_set_id = audio_set_id
        if date is not None:
            self.date = date
        if grammar_id is not None:
            self.grammar_id = grammar_id
        if name is not None:
            self.name = name
        if platform is not None:
            self.platform = platform
        if platform_data is not None:
            self.platform_data = platform_data
        if question_id is not None:
            self.question_id = question_id
        if status is not None:
            self.status = status

    @property
    def experiment_id(self):
        """Gets the experiment_id of this GregExperiment.  # noqa: E501


        :return: The experiment_id of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._experiment_id

    @experiment_id.setter
    def experiment_id(self, experiment_id):
        """Sets the experiment_id of this GregExperiment.


        :param experiment_id: The experiment_id of this GregExperiment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and experiment_id is None:  # noqa: E501
            raise ValueError("Invalid value for `experiment_id`, must not be `None`")  # noqa: E501

        self._experiment_id = experiment_id

    @property
    def account_id(self):
        """Gets the account_id of this GregExperiment.  # noqa: E501

        Account Id  # noqa: E501

        :return: The account_id of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GregExperiment.

        Account Id  # noqa: E501

        :param account_id: The account_id of this GregExperiment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def context_id(self):
        """Gets the context_id of this GregExperiment.  # noqa: E501

        Context Id  # noqa: E501

        :return: The context_id of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this GregExperiment.

        Context Id  # noqa: E501

        :param context_id: The context_id of this GregExperiment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and context_id is None:  # noqa: E501
            raise ValueError("Invalid value for `context_id`, must not be `None`")  # noqa: E501

        self._context_id = context_id

    @property
    def audio_set_id(self):
        """Gets the audio_set_id of this GregExperiment.  # noqa: E501

        Id of the AudioSet that is being used to test the recognition.  May not be modified (in any way) once Recognitions are assigned to this Experiment.   # noqa: E501

        :return: The audio_set_id of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._audio_set_id

    @audio_set_id.setter
    def audio_set_id(self, audio_set_id):
        """Sets the audio_set_id of this GregExperiment.

        Id of the AudioSet that is being used to test the recognition.  May not be modified (in any way) once Recognitions are assigned to this Experiment.   # noqa: E501

        :param audio_set_id: The audio_set_id of this GregExperiment.  # noqa: E501
        :type: str
        """

        self._audio_set_id = audio_set_id

    @property
    def date(self):
        """Gets the date of this GregExperiment.  # noqa: E501

        Start date/time of the experiment  # noqa: E501

        :return: The date of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this GregExperiment.

        Start date/time of the experiment  # noqa: E501

        :param date: The date of this GregExperiment.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def grammar_id(self):
        """Gets the grammar_id of this GregExperiment.  # noqa: E501

        Id of the Grammar that is being used in this Experiment. May not be modified once Recognitions are assigned to this Experiment.  # noqa: E501

        :return: The grammar_id of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._grammar_id

    @grammar_id.setter
    def grammar_id(self, grammar_id):
        """Sets the grammar_id of this GregExperiment.

        Id of the Grammar that is being used in this Experiment. May not be modified once Recognitions are assigned to this Experiment.  # noqa: E501

        :param grammar_id: The grammar_id of this GregExperiment.  # noqa: E501
        :type: str
        """

        self._grammar_id = grammar_id

    @property
    def name(self):
        """Gets the name of this GregExperiment.  # noqa: E501

        Unique experiment Name  # noqa: E501

        :return: The name of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GregExperiment.

        Unique experiment Name  # noqa: E501

        :param name: The name of this GregExperiment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def platform(self):
        """Gets the platform of this GregExperiment.  # noqa: E501


        :return: The platform of this GregExperiment.  # noqa: E501
        :rtype: ExperimentPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this GregExperiment.


        :param platform: The platform of this GregExperiment.  # noqa: E501
        :type: ExperimentPlatform
        """

        self._platform = platform

    @property
    def platform_data(self):
        """Gets the platform_data of this GregExperiment.  # noqa: E501


        :return: The platform_data of this GregExperiment.  # noqa: E501
        :rtype: GregExperimentBasePlatformData
        """
        return self._platform_data

    @platform_data.setter
    def platform_data(self, platform_data):
        """Sets the platform_data of this GregExperiment.


        :param platform_data: The platform_data of this GregExperiment.  # noqa: E501
        :type: GregExperimentBasePlatformData
        """

        self._platform_data = platform_data

    @property
    def question_id(self):
        """Gets the question_id of this GregExperiment.  # noqa: E501

        Id of the Question that is being subject of this Experiment. May not be modified once Recognitions are assigned to this Experiment.  # noqa: E501

        :return: The question_id of this GregExperiment.  # noqa: E501
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this GregExperiment.

        Id of the Question that is being subject of this Experiment. May not be modified once Recognitions are assigned to this Experiment.  # noqa: E501

        :param question_id: The question_id of this GregExperiment.  # noqa: E501
        :type: str
        """

        self._question_id = question_id

    @property
    def status(self):
        """Gets the status of this GregExperiment.  # noqa: E501


        :return: The status of this GregExperiment.  # noqa: E501
        :rtype: GregExperimentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GregExperiment.


        :param status: The status of this GregExperiment.  # noqa: E501
        :type: GregExperimentStatus
        """

        self._status = status

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
        if not isinstance(other, GregExperiment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GregExperiment):
            return True

        return self.to_dict() != other.to_dict()
