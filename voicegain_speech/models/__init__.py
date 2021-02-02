# coding: utf-8

# flake8: noqa
"""
    Voicegain API v1

    # New  [RTC Callback API](#tag/aivr-callback) for building interactive speech-enabled phone applications  (IVR, Voicebots, etc.).    # Intro to Voicegain APIs The APIs are provided by [Voicegain](https://www.voicegain.ai) to its registered customers. </br> The core APIs are for Speech-to-Text (STT), either transcription or recognition (further described in next Sections).</br> Other available APIs include: + RTC Callback APIs which in addition to speech-to-text allow for control of RTC session (e.g., a telephone call). + Websocket APIs for managing broadcast websockets used in real-time transcription. + Language Model creation and manipulation APIs. + Data upload APIs that help in certain STT use scenarios. + Speech Analytics APIs (currently in **beta**) + Training Set APIs - for use in preparing data for acoustic model training. + GREG APIs - for working with ASR and Grammar tuning tool - GREG. + Security APIs.   Python SDK for this API is available at [PyPI Repository](https://pypi.org/project/voicegain-speech/)  In addition to this API Spec document please also consult our Knowledge Base Articles: * [Web API Section](https://support.voicegain.ai/hc/en-us/categories/360001288691-Web-API) of our Knowledge Base   * [Authentication for Web API](https://support.voicegain.ai/hc/en-us/sections/360004485831-Authentication-for-Web-API) - how to generate and use JWT   * [Basic Web API Use Cases](https://support.voicegain.ai/hc/en-us/sections/360004660632-Basic-Web-API-Use-Cases)   * [Example applications using Voicegain API](https://support.voicegain.ai/hc/en-us/sections/360009682932-Example-applications-using-Voicegain-API)  **NOTE:** Most of the request and response examples in this API document are generated from schema example annotation. This may result in the response example not matching the request data example.</br> We will be adding specific examples to certain API methods if we notice that this is needed to clarify the usage.  # Transcribe API  **/asr/transcribe**</br> The Transcribe API allows you to submit audio and receive the transcribed text word-for-word from the STT engine.  This API uses our Large Vocabulary language model and supports long form audio in async mode. </br> The API can, e.g., be used to transcribe audio data - whether it is podcasts, voicemails, call recordings, etc.  In real-time streaming mode it can, e.g., be used for building voice-bots (your the application will have to provide NLU capabilities to determine intent from the transcribed text).    The result of transcription can be returned in four formats. These are requested inside session[].content when making initial transcribe request:  + **Transcript** - Contains the complete text of transcription + **Words** - Intermediate results will contain new words, with timing and confidences, since the previous intermediate result. The final result will contain complete transcription. + **Word-Tree** - Contains a tree of all feasible alternatives. Use this when integrating with NL postprocessing to determine the final utterance and its meaning. + **Captions** - Intermediate results will be suitable to use as captions (this feature is in beta).  # Recognize API  **/asr/recognize**</br> This API should be used if you want to constrain STT recognition results to the speech-grammar that is submitted along with the audio  (grammars are used in place of large vocabulary language model).</br> While building grammars can be time-consuming step, they can simplify the development of applications since the semantic  meaning can be extracted along with the text. </br> Voicegain supports grammars in the JSGF and GRXML formats – both grammar standards used by enterprises in IVRs since early 2000s.</br> The recognize API only supports short form audio - no more than 30 seconds.   # Sync/Async Mode  Speech-to-Text APIs can be accessed in two modes:  + **Sync mode:**  This is the default mode that is invoked when a client makes a request for the Transcribe (/asr/transcribe) and Recognize (/asr/recognize) urls.</br> A Speech-to-Text API synchronous request is the simplest method for performing processing on speech audio data.  Speech-to-Text can process up to 1 minute of speech audio data sent in a synchronous request.  After Speech-to-Text processes all of the audio, it returns a response.</br> A synchronous request is blocking, meaning that Speech-to-Text must return a response before processing the next request.  Speech-to-Text typically processes audio faster than realtime.</br> For longer audio please use Async mode.    + **Async Mode:**  This is invoked by adding the /async to the Transcribe and Recognize url (so /asr/transcribe/async and /asr/recognize/async respectively). </br> In this mode the initial HTTP request request will return as soon as the STT session is established.  The response will contain a session id which can be used to obtain either incremental or full result of speech-to-text processing.  In this mode, the Voicegain platform can provide multiple intermediate recognition/transcription responses to the client as they become available before sending a final response.  ## Async Sessions: Real-Time, Semi Real-Time, and Off-Line  There are 3 types of Async ASR session that can be started:  + **REAL-TIME** - Real-time processing of streaming audio. For the recognition API, results are available within less than one second after end of utterance.  For the transcription API, real-time incremental results will be sent back with under 1 seconds delay.  + **OFF-LINE** - offline transcription or recognition. Has higher accuracy than REAL-TIME. Results are delivered once the complete audio has been processed.  Currently, 1 hour long audio is processed in about 10 minutes. + **SEMI-REAL-TIME** - Similar in use to REAL-TIME, but the results are available with a delay of about 30-45 seconds (or earlier for shorter audio).  Same accuracy as OFF-LINE.  It is possible to start up to 2 simultaneous sessions attached to the same audio.   The allowed combinations of the types of two sessions are:  + REAL-TIME + SEMI-REAL-TIME - one possible use case is a combination of live transcription with transcription for online streaming (which may be delayed w.r.t of real time). The benefit of using separate SEMI-REAL-TIME session is that it has higher accuracy. + REAL-TIME + OFF-LINE - one possible use case is combination of live transcription with higher quality off-line transcription for archival purposes. + 2x REAL-TIME - for example for separately transcribing left and right channels of stereo audio  Other combinations of session types, including more than 2 sessions, are currently not supported.  Please, let us know if you think you have a valid use case for other combinations.  # RTC Callback API   Voicegain Real Time Communication (RTC) Callback APIs work on audio data that is part of an RTC session (a telephone call for example).   # Audio Input  The speech audio can be submitted in variety of ways:  + **Inline** - Short audio data can be encoded inside a request as a base64 string. + **Retrieved from URL** - Audio can be retrieved from a provided URL. The URL can also point to a live stream. + **Streamed via RTP** - Recommended only for Edge use cases (not for Cloud). + **Streamed via proprietary UDP protocol** - We provide a Java utility to do this. The utility can stream directly from an audio device, or from a file. + **Streamed via Websocket** - Can be used, e.g., to do microphone capture directly from the web browser. + **From Object Store** - Currently it works only with files uploaded to Voicegain object store, but will be expanded to support other Object Stores.  # Pagination  For methods that support pagination Voicegain has standardized on using the following query parameters: + page={page number} + per_page={number items per page}  In responses, Voicegain APIs use the [Link Header standard](https://tools.ietf.org/html/rfc5988) to provide the pagination information. The following values of the `rel` field are used: self, first, prev, next, last.  In addition to the `Link` header, the `X-Total-Count` header is used to provide the total count of items matching a query.  An example response header might look like (note: we have broken the Link header in multiple lines for readability )  ``` X-Total-Count: 255 Link: <https://api.voicegain.ai/v1/sa/call?page=1&per_page=50>; rel=\"first\",       <https://api.voicegain.ai/v1/sa/call?page=2&per_page=50>; rel=\"prev\",       <https://api.voicegain.ai/v1/sa/call?page=3&per_page=50>; rel=\"self\",       <https://api.voicegain.ai/v1/sa/call?page=4&per_page=50>; rel=\"next\",       <https://api.voicegain.ai/v1/sa/call?page=6&per_page=50>; rel=\"last\" ```  # JWT Authentication Almost all methods from this API require authentication by means of a JWT Token. A valid token can be obtained from the [Voicegain Portal](https://portal.voicegain.ai).   Each Context within the Account has its own JWT token. The accountId and contextId are encoded inside the token,  that is why API method requests do not require these in their request parameters.  More information about generating and using JWT with Voicegain API can be found in our  [Support Pages](https://support.voicegain.ai/hc/en-us/articles/360028023691-JWT-Authentication).   # noqa: E501

    The version of the OpenAPI document: 1.22.0 - updated January 12, 2021
    Contact: api.support@voicegain.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from voicegain_speech.models.aivr_callback_response import AIVRCallbackResponse
from voicegain_speech.models.aivr_callback_response_final import AIVRCallbackResponseFinal
from voicegain_speech.models.aivr_conference_transfer import AIVRConferenceTransfer
from voicegain_speech.models.aivr_disconnect import AIVRDisconnect
from voicegain_speech.models.aivr_event import AIVREvent
from voicegain_speech.models.aivr_event_type import AIVREventType
from voicegain_speech.models.aivr_existing_session import AIVRExistingSession
from voicegain_speech.models.aivr_logic import AIVRLogic
from voicegain_speech.models.aivr_logic_media import AIVRLogicMedia
from voicegain_speech.models.aivr_logic_transfer import AIVRLogicTransfer
from voicegain_speech.models.aivr_logic_type import AIVRLogicType
from voicegain_speech.models.aivr_new_session import AIVRNewSession
from voicegain_speech.models.aivr_phone_transfer import AIVRPhoneTransfer
from voicegain_speech.models.aivr_prompt import AIVRPrompt
from voicegain_speech.models.aivr_prompt_completion import AIVRPromptCompletion
from voicegain_speech.models.aivr_prompt_playing import AIVRPromptPlaying
from voicegain_speech.models.aivr_prompt_properties_audio import AIVRPromptPropertiesAudio
from voicegain_speech.models.aivr_prompt_properties_html import AIVRPromptPropertiesHtml
from voicegain_speech.models.aivr_question import AIVRQuestion
from voicegain_speech.models.aivr_recognition_result import AIVRRecognitionResult
from voicegain_speech.models.aivr_recording import AIVRRecording
from voicegain_speech.models.aivr_response_properties_audio import AIVRResponsePropertiesAudio
from voicegain_speech.models.aivr_response_properties_html import AIVRResponsePropertiesHtml
from voicegain_speech.models.aivrs_question_specifics import AIVRSQuestionSpecifics
from voicegain_speech.models.aivr_session_user import AIVRSessionUser
from voicegain_speech.models.aivr_session_user_base import AIVRSessionUserBase
from voicegain_speech.models.aivr_session_user_fs import AIVRSessionUserFS
from voicegain_speech.models.aivr_transfer import AIVRTransfer
from voicegain_speech.models.account_and_context_id import AccountAndContextId
from voicegain_speech.models.aircall import Aircall
from voicegain_speech.models.aircall_all_of import AircallAllOf
from voicegain_speech.models.asr_processing_event import AsrProcessingEvent
from voicegain_speech.models.asr_processing_status import AsrProcessingStatus
from voicegain_speech.models.asr_processing_status_additional import AsrProcessingStatusAdditional
from voicegain_speech.models.asr_processing_status_after_input_started import AsrProcessingStatusAfterInputStarted
from voicegain_speech.models.asr_processing_status_for_callback import AsrProcessingStatusForCallback
from voicegain_speech.models.asr_recognition_result import AsrRecognitionResult
from voicegain_speech.models.asr_settings_common import AsrSettingsCommon
from voicegain_speech.models.asr_settings_recognition import AsrSettingsRecognition
from voicegain_speech.models.asr_settings_recognition_all_of import AsrSettingsRecognitionAllOf
from voicegain_speech.models.asr_settings_recognition_defaults import AsrSettingsRecognitionDefaults
from voicegain_speech.models.asr_settings_recognition_defaults_all_of import AsrSettingsRecognitionDefaultsAllOf
from voicegain_speech.models.asr_settings_transcription import AsrSettingsTranscription
from voicegain_speech.models.asr_settings_transcription_all_of import AsrSettingsTranscriptionAllOf
from voicegain_speech.models.asr_settings_transcription_all_of_diarization import AsrSettingsTranscriptionAllOfDiarization
from voicegain_speech.models.asr_settings_transcription_async import AsrSettingsTranscriptionAsync
from voicegain_speech.models.asr_settings_transcription_async_all_of import AsrSettingsTranscriptionAsyncAllOf
from voicegain_speech.models.asr_settings_transcription_common import AsrSettingsTranscriptionCommon
from voicegain_speech.models.asr_settings_transcription_common_all_of import AsrSettingsTranscriptionCommonAllOf
from voicegain_speech.models.asr_settings_transcription_defaults import AsrSettingsTranscriptionDefaults
from voicegain_speech.models.asr_settings_transcription_defaults_all_of import AsrSettingsTranscriptionDefaultsAllOf
from voicegain_speech.models.asr_settings_transcription_sa import AsrSettingsTranscriptionSA
from voicegain_speech.models.asr_settings_transcription_sa_all_of import AsrSettingsTranscriptionSAAllOf
from voicegain_speech.models.asr_settings_transcription_sa_all_of_diarization import AsrSettingsTranscriptionSAAllOfDiarization
from voicegain_speech.models.async_audio_input_source import AsyncAudioInputSource
from voicegain_speech.models.async_mode import AsyncMode
from voicegain_speech.models.async_mode_recognition import AsyncModeRecognition
from voicegain_speech.models.async_mode_speech_analytics import AsyncModeSpeechAnalytics
from voicegain_speech.models.async_mode_transcription import AsyncModeTranscription
from voicegain_speech.models.async_post_response_base import AsyncPostResponseBase
from voicegain_speech.models.async_post_response_base_audio import AsyncPostResponseBaseAudio
from voicegain_speech.models.async_reco_post_response import AsyncRecoPostResponse
from voicegain_speech.models.async_reco_post_response_all_of import AsyncRecoPostResponseAllOf
from voicegain_speech.models.async_recognition_callback_response import AsyncRecognitionCallbackResponse
from voicegain_speech.models.async_recognition_request import AsyncRecognitionRequest
from voicegain_speech.models.async_recognition_response import AsyncRecognitionResponse
from voicegain_speech.models.async_recognition_result import AsyncRecognitionResult
from voicegain_speech.models.async_recognition_result_all_of import AsyncRecognitionResultAllOf
from voicegain_speech.models.async_result_full import AsyncResultFull
from voicegain_speech.models.async_result_full_all_of import AsyncResultFullAllOf
from voicegain_speech.models.async_result_full_all_of_audio import AsyncResultFullAllOfAudio
from voicegain_speech.models.async_result_full_all_of_audio_source import AsyncResultFullAllOfAudioSource
from voicegain_speech.models.async_result_full_all_of_audio_source_data_store import AsyncResultFullAllOfAudioSourceDataStore
from voicegain_speech.models.async_result_full_all_of_result import AsyncResultFullAllOfResult
from voicegain_speech.models.async_result_incremental import AsyncResultIncremental
from voicegain_speech.models.async_result_incremental_detail import AsyncResultIncrementalDetail
from voicegain_speech.models.async_result_incremental_detail_result import AsyncResultIncrementalDetailResult
from voicegain_speech.models.async_session_established import AsyncSessionEstablished
from voicegain_speech.models.async_session_short_info import AsyncSessionShortInfo
from voicegain_speech.models.async_transc_post_response import AsyncTranscPostResponse
from voicegain_speech.models.async_transc_post_response_all_of import AsyncTranscPostResponseAllOf
from voicegain_speech.models.async_transc_session_established import AsyncTranscSessionEstablished
from voicegain_speech.models.async_transc_session_established_all_of import AsyncTranscSessionEstablishedAllOf
from voicegain_speech.models.async_transcription_callback_response import AsyncTranscriptionCallbackResponse
from voicegain_speech.models.async_transcription_request import AsyncTranscriptionRequest
from voicegain_speech.models.async_transcription_response import AsyncTranscriptionResponse
from voicegain_speech.models.async_transcription_response_shared import AsyncTranscriptionResponseShared
from voicegain_speech.models.audio_channel import AudioChannel
from voicegain_speech.models.audio_channel_selector import AudioChannelSelector
from voicegain_speech.models.audio_channels import AudioChannels
from voicegain_speech.models.audio_format import AudioFormat
from voicegain_speech.models.audio_input_async import AudioInputAsync
from voicegain_speech.models.audio_input_async_all_of import AudioInputAsyncAllOf
from voicegain_speech.models.audio_input_base import AudioInputBase
from voicegain_speech.models.audio_input_data import AudioInputData
from voicegain_speech.models.audio_input_data_all_of import AudioInputDataAllOf
from voicegain_speech.models.audio_input_data_all_of_source import AudioInputDataAllOfSource
from voicegain_speech.models.audio_input_sync import AudioInputSync
from voicegain_speech.models.audio_input_sync_all_of import AudioInputSyncAllOf
from voicegain_speech.models.audio_resource_uri import AudioResourceUri
from voicegain_speech.models.audio_resource_uri_all_of import AudioResourceUriAllOf
from voicegain_speech.models.audio_zone_class import AudioZoneClass
from voicegain_speech.models.audio_zone_item import AudioZoneItem
from voicegain_speech.models.builtin import BUILTIN
from voicegain_speech.models.builtin_all_of import BUILTINAllOf
from voicegain_speech.models.call_resolution_phrase import CallResolutionPhrase
from voicegain_speech.models.callback_req import CallbackReq
from voicegain_speech.models.callback_req_reco import CallbackReqReco
from voicegain_speech.models.callback_resp import CallbackResp
from voicegain_speech.models.caption import Caption
from voicegain_speech.models.content_type import ContentType
from voicegain_speech.models.continuous_recognition import ContinuousRecognition
from voicegain_speech.models.core_aivr_session import CoreAIVRSession
from voicegain_speech.models.core_aivr_session_telco_data import CoreAIVRSessionTelcoData
from voicegain_speech.models.creating_entity import CreatingEntity
from voicegain_speech.models.data_obj_ref import DataObjRef
from voicegain_speech.models.data_object import DataObject
from voicegain_speech.models.data_object_all_of import DataObjectAllOf
from voicegain_speech.models.data_object_base import DataObjectBase
from voicegain_speech.models.data_object_ids import DataObjectIds
from voicegain_speech.models.data_object_modifiable import DataObjectModifiable
from voicegain_speech.models.data_object_with_audio import DataObjectWithAudio
from voicegain_speech.models.data_object_with_audio_all_of import DataObjectWithAudioAllOf
from voicegain_speech.models.debug_info import DebugInfo
from voicegain_speech.models.debug_settings import DebugSettings
from voicegain_speech.models.demo import Demo
from voicegain_speech.models.demo_all_of import DemoAllOf
from voicegain_speech.models.diarization_data import DiarizationData
from voicegain_speech.models.diarization_zone import DiarizationZone
from voicegain_speech.models.diarization_zone_item import DiarizationZoneItem
from voicegain_speech.models.disconnect import Disconnect
from voicegain_speech.models.disconnect_all_of import DisconnectAllOf
from voicegain_speech.models.error import Error
from voicegain_speech.models.error_all_of import ErrorAllOf
from voicegain_speech.models.error_info import ErrorInfo
from voicegain_speech.models.estimated_queue_wait import EstimatedQueueWait
from voicegain_speech.models.experiment_platform import ExperimentPlatform
from voicegain_speech.models.file_location import FileLocation
from voicegain_speech.models.greg import GREG
from voicegain_speech.models.greg_all_of import GREGAllOf
from voicegain_speech.models.grxml import GRXML
from voicegain_speech.models.grxml_all_of import GRXMLAllOf
from voicegain_speech.models.grammar import Grammar
from voicegain_speech.models.greg_audio import GregAudio
from voicegain_speech.models.greg_audio_all_of import GregAudioAllOf
from voicegain_speech.models.greg_audio_base import GregAudioBase
from voicegain_speech.models.greg_audio_base_with_audio import GregAudioBaseWithAudio
from voicegain_speech.models.greg_audio_id import GregAudioId
from voicegain_speech.models.greg_audio_input import GregAudioInput
from voicegain_speech.models.greg_audio_input_audio_hash import GregAudioInputAudioHash
from voicegain_speech.models.greg_audio_input_audio_id import GregAudioInputAudioId
from voicegain_speech.models.greg_audio_set import GregAudioSet
from voicegain_speech.models.greg_audio_set_base import GregAudioSetBase
from voicegain_speech.models.greg_audio_set_base_inclusive import GregAudioSetBaseInclusive
from voicegain_speech.models.greg_audio_set_core import GregAudioSetCore
from voicegain_speech.models.greg_audio_set_id import GregAudioSetId
from voicegain_speech.models.greg_audio_set_inclusive import GregAudioSetInclusive
from voicegain_speech.models.greg_audio_set_inclusive_core import GregAudioSetInclusiveCore
from voicegain_speech.models.greg_audio_set_inner import GregAudioSetInner
from voicegain_speech.models.greg_audio_set_response import GregAudioSetResponse
from voicegain_speech.models.greg_audio_thin import GregAudioThin
from voicegain_speech.models.greg_experiment import GregExperiment
from voicegain_speech.models.greg_experiment_base import GregExperimentBase
from voicegain_speech.models.greg_experiment_base_inclusive import GregExperimentBaseInclusive
from voicegain_speech.models.greg_experiment_base_platform_data import GregExperimentBasePlatformData
from voicegain_speech.models.greg_experiment_id import GregExperimentId
from voicegain_speech.models.greg_experiment_inclusive import GregExperimentInclusive
from voicegain_speech.models.greg_experiment_modifiable import GregExperimentModifiable
from voicegain_speech.models.greg_experiment_platform_external_asr import GregExperimentPlatformExternalASR
from voicegain_speech.models.greg_experiment_platform_upload import GregExperimentPlatformUpload
from voicegain_speech.models.greg_experiment_platform_voicegain import GregExperimentPlatformVoicegain
from voicegain_speech.models.greg_experiment_response import GregExperimentResponse
from voicegain_speech.models.greg_experiment_status import GregExperimentStatus
from voicegain_speech.models.greg_experiment_status_modifiable import GregExperimentStatusModifiable
from voicegain_speech.models.greg_grammar import GregGrammar
from voicegain_speech.models.greg_grammar_base import GregGrammarBase
from voicegain_speech.models.greg_grammar_base_light import GregGrammarBaseLight
from voicegain_speech.models.greg_grammar_id import GregGrammarId
from voicegain_speech.models.greg_grammar_inner import GregGrammarInner
from voicegain_speech.models.greg_grammar_light import GregGrammarLight
from voicegain_speech.models.greg_interpretation import GregInterpretation
from voicegain_speech.models.greg_question import GregQuestion
from voicegain_speech.models.greg_question_base import GregQuestionBase
from voicegain_speech.models.greg_question_id import GregQuestionId
from voicegain_speech.models.greg_question_inner import GregQuestionInner
from voicegain_speech.models.greg_recog_base_no_exp_nlsml_core import GregRecogBaseNoExpNlsmlCore
from voicegain_speech.models.greg_recog_base_no_exp_obj_core import GregRecogBaseNoExpObjCore
from voicegain_speech.models.greg_recog_base_no_exp_obj_or_nlsml import GregRecogBaseNoExpObjOrNlsml
from voicegain_speech.models.greg_recog_base_obj_or_nlsml import GregRecogBaseObjOrNlsml
from voicegain_speech.models.greg_recog_base_with_exp import GregRecogBaseWithExp
from voicegain_speech.models.greg_recognition import GregRecognition
from voicegain_speech.models.greg_recognition_base import GregRecognitionBase
from voicegain_speech.models.greg_recognition_id import GregRecognitionId
from voicegain_speech.models.greg_review_status import GregReviewStatus
from voicegain_speech.models.greg_source_of_truth import GregSourceOfTruth
from voicegain_speech.models.greg_truth_update import GregTruthUpdate
from voicegain_speech.models.greg_truth_updates import GregTruthUpdates
from voicegain_speech.models.gui_input import GuiInput
from voicegain_speech.models.hangup import Hangup
from voicegain_speech.models.html_checkbox import HtmlCheckbox
from voicegain_speech.models.html_choice_item import HtmlChoiceItem
from voicegain_speech.models.html_radio_buttons import HtmlRadioButtons
from voicegain_speech.models.html_text_entry import HtmlTextEntry
from voicegain_speech.models.if_exists import IfExists
from voicegain_speech.models.inline_data import InlineData
from voicegain_speech.models.inline_object import InlineObject
from voicegain_speech.models.inline_object1 import InlineObject1
from voicegain_speech.models.input import Input
from voicegain_speech.models.input_all_of import InputAllOf
from voicegain_speech.models.integration import Integration
from voicegain_speech.models.jjsgf import JJSGF
from voicegain_speech.models.jjsgf_all_of import JJSGFAllOf
from voicegain_speech.models.keyword_spot_example import KeywordSpotExample
from voicegain_speech.models.keyword_spot_group import KeywordSpotGroup
from voicegain_speech.models.keyword_spot_item import KeywordSpotItem
from voicegain_speech.models.lm_type import LMType
from voicegain_speech.models.lang_model_status import LangModelStatus
from voicegain_speech.models.language_model_doc import LanguageModelDoc
from voicegain_speech.models.language_model_doc_modifiable import LanguageModelDocModifiable
from voicegain_speech.models.language_model_src_data import LanguageModelSrcData
from voicegain_speech.models.mrcp_version import MRCPVersion
from voicegain_speech.models.mrc_pv1_asr_settings import MRCPv1AsrSettings
from voicegain_speech.models.mrc_pv2_asr_settings import MRCPv2AsrSettings
from voicegain_speech.models.mood_type import MoodType
from voicegain_speech.models.name_value_pair import NameValuePair
from voicegain_speech.models.named_entity_type import NamedEntityType
from voicegain_speech.models.new_speech_analytics_session import NewSpeechAnalyticsSession
from voicegain_speech.models.new_speech_analytics_session_response import NewSpeechAnalyticsSessionResponse
from voicegain_speech.models.new_speech_analytics_session_response_poll import NewSpeechAnalyticsSessionResponsePoll
from voicegain_speech.models.non_session_error_response import NonSessionErrorResponse
from voicegain_speech.models.non_session_error_response400 import NonSessionErrorResponse400
from voicegain_speech.models.non_session_error_response401 import NonSessionErrorResponse401
from voicegain_speech.models.output import Output
from voicegain_speech.models.output_all_of import OutputAllOf
from voicegain_speech.models.overtalk import Overtalk
from voicegain_speech.models.pii_redaction_conf import PIIRedactionConf
from voicegain_speech.models.phrase_spot_example import PhraseSpotExample
from voicegain_speech.models.phrase_spot_item import PhraseSpotItem
from voicegain_speech.models.poll_req import PollReq
from voicegain_speech.models.poll_resp import PollResp
from voicegain_speech.models.portal_output_init import PortalOutputInit
from voicegain_speech.models.progress import Progress
from voicegain_speech.models.progress_phase import ProgressPhase
from voicegain_speech.models.quartiles_energy import QuartilesEnergy
from voicegain_speech.models.quartiles_pitch import QuartilesPitch
from voicegain_speech.models.reco_alt import RecoAlt
from voicegain_speech.models.recog_nlsml import RecogNlsml
from voicegain_speech.models.recog_nlsml_no_exp import RecogNlsmlNoExp
from voicegain_speech.models.recog_obj import RecogObj
from voicegain_speech.models.recog_obj_no_exp import RecogObjNoExp
from voicegain_speech.models.recognition_result import RecognitionResult
from voicegain_speech.models.requested_content import RequestedContent
from voicegain_speech.models.resource_uri import ResourceUri
from voicegain_speech.models.s3 import S3
from voicegain_speech.models.s3_all_of import S3AllOf
from voicegain_speech.models.sample_rate import SampleRate
from voicegain_speech.models.session_error_response import SessionErrorResponse
from voicegain_speech.models.session_init_recognition import SessionInitRecognition
from voicegain_speech.models.session_init_transcription import SessionInitTranscription
from voicegain_speech.models.session_success_response import SessionSuccessResponse
from voicegain_speech.models.settings_async_transcription import SettingsAsyncTranscription
from voicegain_speech.models.settings_recognition import SettingsRecognition
from voicegain_speech.models.settings_sync_transcription import SettingsSyncTranscription
from voicegain_speech.models.silence import Silence
from voicegain_speech.models.sos_ref import SosRef
from voicegain_speech.models.speaker_result import SpeakerResult
from voicegain_speech.models.speech_analytics_channel import SpeechAnalyticsChannel
from voicegain_speech.models.speech_analytics_channel_result import SpeechAnalyticsChannelResult
from voicegain_speech.models.speech_analytics_channel_with_transcribe import SpeechAnalyticsChannelWithTranscribe
from voicegain_speech.models.speech_analytics_channel_with_transcribe_all_of import SpeechAnalyticsChannelWithTranscribeAllOf
from voicegain_speech.models.speech_analytics_config import SpeechAnalyticsConfig
from voicegain_speech.models.speech_analytics_config_identifying import SpeechAnalyticsConfigIdentifying
from voicegain_speech.models.speech_analytics_config_modifiable import SpeechAnalyticsConfigModifiable
from voicegain_speech.models.speech_analytics_emotion import SpeechAnalyticsEmotion
from voicegain_speech.models.speech_analytics_emotion_data import SpeechAnalyticsEmotionData
from voicegain_speech.models.speech_analytics_emotion_item import SpeechAnalyticsEmotionItem
from voicegain_speech.models.speech_analytics_keyword import SpeechAnalyticsKeyword
from voicegain_speech.models.speech_analytics_keyword_data import SpeechAnalyticsKeywordData
from voicegain_speech.models.speech_analytics_keyword_item import SpeechAnalyticsKeywordItem
from voicegain_speech.models.speech_analytics_named_entity import SpeechAnalyticsNamedEntity
from voicegain_speech.models.speech_analytics_named_entity_item import SpeechAnalyticsNamedEntityItem
from voicegain_speech.models.speech_analytics_phrase import SpeechAnalyticsPhrase
from voicegain_speech.models.speech_analytics_phrase_data import SpeechAnalyticsPhraseData
from voicegain_speech.models.speech_analytics_phrase_item import SpeechAnalyticsPhraseItem
from voicegain_speech.models.speech_analytics_result import SpeechAnalyticsResult
from voicegain_speech.models.stream_resp import StreamResp
from voicegain_speech.models.stream_setup import StreamSetup
from voicegain_speech.models.streaming_protocol import StreamingProtocol
from voicegain_speech.models.sync_audio_input_source import SyncAudioInputSource
from voicegain_speech.models.sync_recognition_request import SyncRecognitionRequest
from voicegain_speech.models.sync_recognition_response import SyncRecognitionResponse
from voicegain_speech.models.sync_session_established import SyncSessionEstablished
from voicegain_speech.models.sync_transcription_request import SyncTranscriptionRequest
from voicegain_speech.models.sync_transcription_response import SyncTranscriptionResponse
from voicegain_speech.models.sync_transcription_result import SyncTranscriptionResult
from voicegain_speech.models.talk_time import TalkTime
from voicegain_speech.models.training_set_bucket_type import TrainingSetBucketType
from voicegain_speech.models.training_set_doc import TrainingSetDoc
from voicegain_speech.models.training_set_doc_defaults import TrainingSetDocDefaults
from voicegain_speech.models.training_set_doc_statistics import TrainingSetDocStatistics
from voicegain_speech.models.training_set_key import TrainingSetKey
from voicegain_speech.models.training_set_modifiable import TrainingSetModifiable
from voicegain_speech.models.training_set_status import TrainingSetStatus
from voicegain_speech.models.training_set_status_modifiable import TrainingSetStatusModifiable
from voicegain_speech.models.training_set_store_type import TrainingSetStoreType
from voicegain_speech.models.transcribe_alt import TranscribeAlt
from voicegain_speech.models.transcript_position_range import TranscriptPositionRange
from voicegain_speech.models.transfer import Transfer
from voicegain_speech.models.transfer_all_of import TransferAllOf
from voicegain_speech.models.websocket import Websocket
from voicegain_speech.models.websocket_init import WebsocketInit
from voicegain_speech.models.websocket_init_reco import WebsocketInitReco
from voicegain_speech.models.websocket_modifiable import WebsocketModifiable
from voicegain_speech.models.websocket_msg import WebsocketMsg
from voicegain_speech.models.websocket_resp import WebsocketResp
from voicegain_speech.models.word_alternatives import WordAlternatives
from voicegain_speech.models.word_cloud_item import WordCloudItem
from voicegain_speech.models.word_correction import WordCorrection
from voicegain_speech.models.word_item_timed import WordItemTimed
from voicegain_speech.models.word_item_timing import WordItemTiming
from voicegain_speech.models.word_tree_ids import WordTreeIds
from voicegain_speech.models.word_tree_item import WordTreeItem
from voicegain_speech.models.words_item import WordsItem
from voicegain_speech.models.words_section import WordsSection
from voicegain_speech.models.words_websocket_item import WordsWebsocketItem
