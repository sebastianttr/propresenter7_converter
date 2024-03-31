import action_pb2 as _action_pb2
import cue_pb2 as _cue_pb2
import graphicsData_pb2 as _graphicsData_pb2
import groups_pb2 as _groups_pb2
import labels_pb2 as _labels_pb2
import proClockSource_pb2 as _proClockSource_pb2
import url_pb2 as _url_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Preferences(_message.Message):
    __slots__ = ("general", "screens", "groups", "network", "sync", "advanced", "updates")
    class General(_message.Message):
        __slots__ = ("house_of_worship_integrations", "crash_reports", "analytics", "logo_path", "language")
        HOUSE_OF_WORSHIP_INTEGRATIONS_FIELD_NUMBER: _ClassVar[int]
        CRASH_REPORTS_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_FIELD_NUMBER: _ClassVar[int]
        LOGO_PATH_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        house_of_worship_integrations: bool
        crash_reports: bool
        analytics: bool
        logo_path: str
        language: str
        def __init__(self, house_of_worship_integrations: bool = ..., crash_reports: bool = ..., analytics: bool = ..., logo_path: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...
    class Screens(_message.Message):
        __slots__ = ("enable_at_launch", "show_performance_stats", "ignore_background_colors", "clock_source", "show_keynote_and_powerpoint", "disable_blackmagic_sync_groups", "use_directx_rendering")
        ENABLE_AT_LAUNCH_FIELD_NUMBER: _ClassVar[int]
        SHOW_PERFORMANCE_STATS_FIELD_NUMBER: _ClassVar[int]
        IGNORE_BACKGROUND_COLORS_FIELD_NUMBER: _ClassVar[int]
        CLOCK_SOURCE_FIELD_NUMBER: _ClassVar[int]
        SHOW_KEYNOTE_AND_POWERPOINT_FIELD_NUMBER: _ClassVar[int]
        DISABLE_BLACKMAGIC_SYNC_GROUPS_FIELD_NUMBER: _ClassVar[int]
        USE_DIRECTX_RENDERING_FIELD_NUMBER: _ClassVar[int]
        enable_at_launch: bool
        show_performance_stats: bool
        ignore_background_colors: bool
        clock_source: _proClockSource_pb2.ProClockSource
        show_keynote_and_powerpoint: bool
        disable_blackmagic_sync_groups: bool
        use_directx_rendering: bool
        def __init__(self, enable_at_launch: bool = ..., show_performance_stats: bool = ..., ignore_background_colors: bool = ..., clock_source: _Optional[_Union[_proClockSource_pb2.ProClockSource, _Mapping]] = ..., show_keynote_and_powerpoint: bool = ..., disable_blackmagic_sync_groups: bool = ..., use_directx_rendering: bool = ...) -> None: ...
    class Import(_message.Message):
        __slots__ = ("foreground_scaling", "foreground_is_blurred", "background_scaling", "background_is_blurred", "image", "video", "audio")
        class ScaleBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_BEHAVIOR_FIT: _ClassVar[Preferences.Import.ScaleBehavior]
            SCALE_BEHAVIOR_FILL: _ClassVar[Preferences.Import.ScaleBehavior]
            SCALE_BEHAVIOR_STRETCH: _ClassVar[Preferences.Import.ScaleBehavior]
            SCALE_BEHAVIOR_CUSTOM: _ClassVar[Preferences.Import.ScaleBehavior]
        SCALE_BEHAVIOR_FIT: Preferences.Import.ScaleBehavior
        SCALE_BEHAVIOR_FILL: Preferences.Import.ScaleBehavior
        SCALE_BEHAVIOR_STRETCH: Preferences.Import.ScaleBehavior
        SCALE_BEHAVIOR_CUSTOM: Preferences.Import.ScaleBehavior
        class Image(_message.Message):
            __slots__ = ("layer_type", "duration", "next_behavior")
            class LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                LAYER_TYPE_BACKGROUND: _ClassVar[Preferences.Import.Image.LayerType]
                LAYER_TYPE_FOREGROUND: _ClassVar[Preferences.Import.Image.LayerType]
                LAYER_TYPE_FILL: _ClassVar[Preferences.Import.Image.LayerType]
                LAYER_TYPE_INPUT: _ClassVar[Preferences.Import.Image.LayerType]
            LAYER_TYPE_BACKGROUND: Preferences.Import.Image.LayerType
            LAYER_TYPE_FOREGROUND: Preferences.Import.Image.LayerType
            LAYER_TYPE_FILL: Preferences.Import.Image.LayerType
            LAYER_TYPE_INPUT: Preferences.Import.Image.LayerType
            class CompletionTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COMPLETION_TARGET_TYPE_NONE: _ClassVar[Preferences.Import.Image.CompletionTargetType]
                COMPLETION_TARGET_TYPE_NEXT: _ClassVar[Preferences.Import.Image.CompletionTargetType]
                COMPLETION_TARGET_TYPE_RANDOM: _ClassVar[Preferences.Import.Image.CompletionTargetType]
                COMPLETION_TARGET_TYPE_CUE: _ClassVar[Preferences.Import.Image.CompletionTargetType]
                COMPLETION_TARGET_TYPE_FIRST: _ClassVar[Preferences.Import.Image.CompletionTargetType]
            COMPLETION_TARGET_TYPE_NONE: Preferences.Import.Image.CompletionTargetType
            COMPLETION_TARGET_TYPE_NEXT: Preferences.Import.Image.CompletionTargetType
            COMPLETION_TARGET_TYPE_RANDOM: Preferences.Import.Image.CompletionTargetType
            COMPLETION_TARGET_TYPE_CUE: Preferences.Import.Image.CompletionTargetType
            COMPLETION_TARGET_TYPE_FIRST: Preferences.Import.Image.CompletionTargetType
            class Duration(_message.Message):
                __slots__ = ("none", "time", "random")
                class None(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...
                class Time(_message.Message):
                    __slots__ = ("time",)
                    TIME_FIELD_NUMBER: _ClassVar[int]
                    time: float
                    def __init__(self, time: _Optional[float] = ...) -> None: ...
                class Random(_message.Message):
                    __slots__ = ("minimum_time", "maximum_time")
                    MINIMUM_TIME_FIELD_NUMBER: _ClassVar[int]
                    MAXIMUM_TIME_FIELD_NUMBER: _ClassVar[int]
                    minimum_time: float
                    maximum_time: float
                    def __init__(self, minimum_time: _Optional[float] = ..., maximum_time: _Optional[float] = ...) -> None: ...
                NONE_FIELD_NUMBER: _ClassVar[int]
                TIME_FIELD_NUMBER: _ClassVar[int]
                RANDOM_FIELD_NUMBER: _ClassVar[int]
                none: getattr(Preferences.Import.Image.Duration, 'None')
                time: Preferences.Import.Image.Duration.Time
                random: Preferences.Import.Image.Duration.Random
                def __init__(self, none: _Optional[_Union[getattr(Preferences.Import.Image.Duration, 'None'), _Mapping]] = ..., time: _Optional[_Union[Preferences.Import.Image.Duration.Time, _Mapping]] = ..., random: _Optional[_Union[Preferences.Import.Image.Duration.Random, _Mapping]] = ...) -> None: ...
            LAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            NEXT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            layer_type: Preferences.Import.Image.LayerType
            duration: Preferences.Import.Image.Duration
            next_behavior: Preferences.Import.Image.CompletionTargetType
            def __init__(self, layer_type: _Optional[_Union[Preferences.Import.Image.LayerType, str]] = ..., duration: _Optional[_Union[Preferences.Import.Image.Duration, _Mapping]] = ..., next_behavior: _Optional[_Union[Preferences.Import.Image.CompletionTargetType, str]] = ...) -> None: ...
        class Video(_message.Message):
            __slots__ = ("layer_type", "playback_behavior", "end_behavior", "next_behavior")
            class LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                LAYER_TYPE_BACKGROUND: _ClassVar[Preferences.Import.Video.LayerType]
                LAYER_TYPE_FOREGROUND: _ClassVar[Preferences.Import.Video.LayerType]
                LAYER_TYPE_FILL: _ClassVar[Preferences.Import.Video.LayerType]
                LAYER_TYPE_INPUT: _ClassVar[Preferences.Import.Video.LayerType]
            LAYER_TYPE_BACKGROUND: Preferences.Import.Video.LayerType
            LAYER_TYPE_FOREGROUND: Preferences.Import.Video.LayerType
            LAYER_TYPE_FILL: Preferences.Import.Video.LayerType
            LAYER_TYPE_INPUT: Preferences.Import.Video.LayerType
            class PlaybackBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PLAYBACK_BEHAVIOR_STOP: _ClassVar[Preferences.Import.Video.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP: _ClassVar[Preferences.Import.Video.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: _ClassVar[Preferences.Import.Video.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: _ClassVar[Preferences.Import.Video.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_STOP: Preferences.Import.Video.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP: Preferences.Import.Video.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: Preferences.Import.Video.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: Preferences.Import.Video.PlaybackBehavior
            class EndBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                END_BEHAVIOR_STOP: _ClassVar[Preferences.Import.Video.EndBehavior]
                END_BEHAVIOR_STOP_ON_BLACK: _ClassVar[Preferences.Import.Video.EndBehavior]
                END_BEHAVIOR_STOP_ON_CLEAR: _ClassVar[Preferences.Import.Video.EndBehavior]
                END_BEHAVIOR_FADE_TO_BLACK: _ClassVar[Preferences.Import.Video.EndBehavior]
                END_BEHAVIOR_FADE_TO_CLEAR: _ClassVar[Preferences.Import.Video.EndBehavior]
            END_BEHAVIOR_STOP: Preferences.Import.Video.EndBehavior
            END_BEHAVIOR_STOP_ON_BLACK: Preferences.Import.Video.EndBehavior
            END_BEHAVIOR_STOP_ON_CLEAR: Preferences.Import.Video.EndBehavior
            END_BEHAVIOR_FADE_TO_BLACK: Preferences.Import.Video.EndBehavior
            END_BEHAVIOR_FADE_TO_CLEAR: Preferences.Import.Video.EndBehavior
            class CompletionTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COMPLETION_TARGET_TYPE_NONE: _ClassVar[Preferences.Import.Video.CompletionTargetType]
                COMPLETION_TARGET_TYPE_NEXT: _ClassVar[Preferences.Import.Video.CompletionTargetType]
                COMPLETION_TARGET_TYPE_RANDOM: _ClassVar[Preferences.Import.Video.CompletionTargetType]
                COMPLETION_TARGET_TYPE_CUE: _ClassVar[Preferences.Import.Video.CompletionTargetType]
                COMPLETION_TARGET_TYPE_FIRST: _ClassVar[Preferences.Import.Video.CompletionTargetType]
            COMPLETION_TARGET_TYPE_NONE: Preferences.Import.Video.CompletionTargetType
            COMPLETION_TARGET_TYPE_NEXT: Preferences.Import.Video.CompletionTargetType
            COMPLETION_TARGET_TYPE_RANDOM: Preferences.Import.Video.CompletionTargetType
            COMPLETION_TARGET_TYPE_CUE: Preferences.Import.Video.CompletionTargetType
            COMPLETION_TARGET_TYPE_FIRST: Preferences.Import.Video.CompletionTargetType
            LAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
            PLAYBACK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            END_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            NEXT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            layer_type: Preferences.Import.Video.LayerType
            playback_behavior: Preferences.Import.Video.PlaybackBehavior
            end_behavior: Preferences.Import.Video.EndBehavior
            next_behavior: Preferences.Import.Video.CompletionTargetType
            def __init__(self, layer_type: _Optional[_Union[Preferences.Import.Video.LayerType, str]] = ..., playback_behavior: _Optional[_Union[Preferences.Import.Video.PlaybackBehavior, str]] = ..., end_behavior: _Optional[_Union[Preferences.Import.Video.EndBehavior, str]] = ..., next_behavior: _Optional[_Union[Preferences.Import.Video.CompletionTargetType, str]] = ...) -> None: ...
        class Audio(_message.Message):
            __slots__ = ("playback_behavior", "next_behavior")
            class PlaybackBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PLAYBACK_BEHAVIOR_STOP: _ClassVar[Preferences.Import.Audio.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP: _ClassVar[Preferences.Import.Audio.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: _ClassVar[Preferences.Import.Audio.PlaybackBehavior]
                PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: _ClassVar[Preferences.Import.Audio.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_STOP: Preferences.Import.Audio.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP: Preferences.Import.Audio.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_COUNT: Preferences.Import.Audio.PlaybackBehavior
            PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: Preferences.Import.Audio.PlaybackBehavior
            class CompletionTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COMPLETION_TARGET_TYPE_NONE: _ClassVar[Preferences.Import.Audio.CompletionTargetType]
                COMPLETION_TARGET_TYPE_NEXT: _ClassVar[Preferences.Import.Audio.CompletionTargetType]
                COMPLETION_TARGET_TYPE_RANDOM: _ClassVar[Preferences.Import.Audio.CompletionTargetType]
                COMPLETION_TARGET_TYPE_CUE: _ClassVar[Preferences.Import.Audio.CompletionTargetType]
                COMPLETION_TARGET_TYPE_FIRST: _ClassVar[Preferences.Import.Audio.CompletionTargetType]
            COMPLETION_TARGET_TYPE_NONE: Preferences.Import.Audio.CompletionTargetType
            COMPLETION_TARGET_TYPE_NEXT: Preferences.Import.Audio.CompletionTargetType
            COMPLETION_TARGET_TYPE_RANDOM: Preferences.Import.Audio.CompletionTargetType
            COMPLETION_TARGET_TYPE_CUE: Preferences.Import.Audio.CompletionTargetType
            COMPLETION_TARGET_TYPE_FIRST: Preferences.Import.Audio.CompletionTargetType
            PLAYBACK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            NEXT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
            playback_behavior: Preferences.Import.Audio.PlaybackBehavior
            next_behavior: Preferences.Import.Audio.CompletionTargetType
            def __init__(self, playback_behavior: _Optional[_Union[Preferences.Import.Audio.PlaybackBehavior, str]] = ..., next_behavior: _Optional[_Union[Preferences.Import.Audio.CompletionTargetType, str]] = ...) -> None: ...
        FOREGROUND_SCALING_FIELD_NUMBER: _ClassVar[int]
        FOREGROUND_IS_BLURRED_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_SCALING_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_IS_BLURRED_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        foreground_scaling: Preferences.Import.ScaleBehavior
        foreground_is_blurred: bool
        background_scaling: Preferences.Import.ScaleBehavior
        background_is_blurred: bool
        image: Preferences.Import.Image
        video: Preferences.Import.Video
        audio: Preferences.Import.Audio
        def __init__(self, foreground_scaling: _Optional[_Union[Preferences.Import.ScaleBehavior, str]] = ..., foreground_is_blurred: bool = ..., background_scaling: _Optional[_Union[Preferences.Import.ScaleBehavior, str]] = ..., background_is_blurred: bool = ..., image: _Optional[_Union[Preferences.Import.Image, _Mapping]] = ..., video: _Optional[_Union[Preferences.Import.Video, _Mapping]] = ..., audio: _Optional[_Union[Preferences.Import.Audio, _Mapping]] = ...) -> None: ...
    class Groups(_message.Message):
        __slots__ = ("groups", "labels")
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        groups: _groups_pb2.ProGroupsDocument
        labels: _labels_pb2.ProLabelsDocument
        def __init__(self, groups: _Optional[_Union[_groups_pb2.ProGroupsDocument, _Mapping]] = ..., labels: _Optional[_Union[_labels_pb2.ProLabelsDocument, _Mapping]] = ...) -> None: ...
    class Network(_message.Message):
        __slots__ = ("network", "remotes", "link")
        class Network(_message.Message):
            __slots__ = ("enable", "name", "port")
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            PORT_FIELD_NUMBER: _ClassVar[int]
            enable: bool
            name: str
            port: int
            def __init__(self, enable: bool = ..., name: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...
        class Remotes(_message.Message):
            __slots__ = ("pro_remote", "stage_app")
            class ProRemote(_message.Message):
                __slots__ = ("enable", "enable_controller", "controller_password", "enable_observer", "observer_password")
                ENABLE_FIELD_NUMBER: _ClassVar[int]
                ENABLE_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
                CONTROLLER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
                ENABLE_OBSERVER_FIELD_NUMBER: _ClassVar[int]
                OBSERVER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
                enable: bool
                enable_controller: bool
                controller_password: str
                enable_observer: bool
                observer_password: str
                def __init__(self, enable: bool = ..., enable_controller: bool = ..., controller_password: _Optional[str] = ..., enable_observer: bool = ..., observer_password: _Optional[str] = ...) -> None: ...
            class StageApp(_message.Message):
                __slots__ = ("enable", "password")
                ENABLE_FIELD_NUMBER: _ClassVar[int]
                PASSWORD_FIELD_NUMBER: _ClassVar[int]
                enable: bool
                password: str
                def __init__(self, enable: bool = ..., password: _Optional[str] = ...) -> None: ...
            PRO_REMOTE_FIELD_NUMBER: _ClassVar[int]
            STAGE_APP_FIELD_NUMBER: _ClassVar[int]
            pro_remote: Preferences.Network.Remotes.ProRemote
            stage_app: Preferences.Network.Remotes.StageApp
            def __init__(self, pro_remote: _Optional[_Union[Preferences.Network.Remotes.ProRemote, _Mapping]] = ..., stage_app: _Optional[_Union[Preferences.Network.Remotes.StageApp, _Mapping]] = ...) -> None: ...
        class Link(_message.Message):
            __slots__ = ("enable", "link_group")
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            LINK_GROUP_FIELD_NUMBER: _ClassVar[int]
            enable: bool
            link_group: str
            def __init__(self, enable: bool = ..., link_group: _Optional[str] = ...) -> None: ...
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        REMOTES_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        network: Preferences.Network.Network
        remotes: Preferences.Network.Remotes
        link: Preferences.Network.Link
        def __init__(self, network: _Optional[_Union[Preferences.Network.Network, _Mapping]] = ..., remotes: _Optional[_Union[Preferences.Network.Remotes, _Mapping]] = ..., link: _Optional[_Union[Preferences.Network.Link, _Mapping]] = ...) -> None: ...
    class Sync(_message.Message):
        __slots__ = ("repository", "include_libraries", "include_media", "include_playlists", "include_themes", "include_support_files", "direction", "replace_destination_files")
        class SyncDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SYNC_DOWN: _ClassVar[Preferences.Sync.SyncDirection]
            SYNC_UP: _ClassVar[Preferences.Sync.SyncDirection]
        SYNC_DOWN: Preferences.Sync.SyncDirection
        SYNC_UP: Preferences.Sync.SyncDirection
        REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_LIBRARIES_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_MEDIA_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_THEMES_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_SUPPORT_FILES_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        REPLACE_DESTINATION_FILES_FIELD_NUMBER: _ClassVar[int]
        repository: str
        include_libraries: bool
        include_media: bool
        include_playlists: bool
        include_themes: bool
        include_support_files: bool
        direction: Preferences.Sync.SyncDirection
        replace_destination_files: bool
        def __init__(self, repository: _Optional[str] = ..., include_libraries: bool = ..., include_media: bool = ..., include_playlists: bool = ..., include_themes: bool = ..., include_support_files: bool = ..., direction: _Optional[_Union[Preferences.Sync.SyncDirection, str]] = ..., replace_destination_files: bool = ...) -> None: ...
    class Advanced(_message.Message):
        __slots__ = ("suppress_auto_start", "presentation_audio_behavior", "announcements_audio_behavior", "ndi_discovery", "support_files_path", "manage_media_automatically", "search_paths")
        class AudioForegroundMediaBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            IGNORE_FOREGROUND_MEDIA: _ClassVar[Preferences.Advanced.AudioForegroundMediaBehavior]
            CLEAR_FOR_ALL_MEDIA: _ClassVar[Preferences.Advanced.AudioForegroundMediaBehavior]
            CLEAR_IF_AUDIO: _ClassVar[Preferences.Advanced.AudioForegroundMediaBehavior]
            PAUSE_FOR_ALL_MEDIA: _ClassVar[Preferences.Advanced.AudioForegroundMediaBehavior]
            PAUSE_IF_AUDIO: _ClassVar[Preferences.Advanced.AudioForegroundMediaBehavior]
        IGNORE_FOREGROUND_MEDIA: Preferences.Advanced.AudioForegroundMediaBehavior
        CLEAR_FOR_ALL_MEDIA: Preferences.Advanced.AudioForegroundMediaBehavior
        CLEAR_IF_AUDIO: Preferences.Advanced.AudioForegroundMediaBehavior
        PAUSE_FOR_ALL_MEDIA: Preferences.Advanced.AudioForegroundMediaBehavior
        PAUSE_IF_AUDIO: Preferences.Advanced.AudioForegroundMediaBehavior
        class NDIDiscovery(_message.Message):
            __slots__ = ("show_local_sources", "receive_groups", "additional_search_ips")
            SHOW_LOCAL_SOURCES_FIELD_NUMBER: _ClassVar[int]
            RECEIVE_GROUPS_FIELD_NUMBER: _ClassVar[int]
            ADDITIONAL_SEARCH_IPS_FIELD_NUMBER: _ClassVar[int]
            show_local_sources: bool
            receive_groups: str
            additional_search_ips: str
            def __init__(self, show_local_sources: bool = ..., receive_groups: _Optional[str] = ..., additional_search_ips: _Optional[str] = ...) -> None: ...
        class SearchPaths(_message.Message):
            __slots__ = ("automatically_relink", "paths")
            class Path(_message.Message):
                __slots__ = ("enable", "name", "path", "url_root")
                class Root(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    ROOT_UNKNOWN: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_BOOT_VOLUME: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_HOME: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_DOCUMENTS: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_DOWNLOADS: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_MUSIC: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_PICTURES: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_VIDEOS: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_DESKTOP: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_USER_APP_SUPPORT: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_SHARED: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_SHOW: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                    ROOT_CURRENT_RESOURCE: _ClassVar[Preferences.Advanced.SearchPaths.Path.Root]
                ROOT_UNKNOWN: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_BOOT_VOLUME: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_HOME: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_DOCUMENTS: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_DOWNLOADS: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_MUSIC: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_PICTURES: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_VIDEOS: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_DESKTOP: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_USER_APP_SUPPORT: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_SHARED: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_SHOW: Preferences.Advanced.SearchPaths.Path.Root
                ROOT_CURRENT_RESOURCE: Preferences.Advanced.SearchPaths.Path.Root
                ENABLE_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                PATH_FIELD_NUMBER: _ClassVar[int]
                URL_ROOT_FIELD_NUMBER: _ClassVar[int]
                enable: bool
                name: str
                path: str
                url_root: Preferences.Advanced.SearchPaths.Path.Root
                def __init__(self, enable: bool = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., url_root: _Optional[_Union[Preferences.Advanced.SearchPaths.Path.Root, str]] = ...) -> None: ...
            AUTOMATICALLY_RELINK_FIELD_NUMBER: _ClassVar[int]
            PATHS_FIELD_NUMBER: _ClassVar[int]
            automatically_relink: bool
            paths: _containers.RepeatedCompositeFieldContainer[Preferences.Advanced.SearchPaths.Path]
            def __init__(self, automatically_relink: bool = ..., paths: _Optional[_Iterable[_Union[Preferences.Advanced.SearchPaths.Path, _Mapping]]] = ...) -> None: ...
        SUPPRESS_AUTO_START_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_AUDIO_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        ANNOUNCEMENTS_AUDIO_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        NDI_DISCOVERY_FIELD_NUMBER: _ClassVar[int]
        SUPPORT_FILES_PATH_FIELD_NUMBER: _ClassVar[int]
        MANAGE_MEDIA_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
        SEARCH_PATHS_FIELD_NUMBER: _ClassVar[int]
        suppress_auto_start: bool
        presentation_audio_behavior: Preferences.Advanced.AudioForegroundMediaBehavior
        announcements_audio_behavior: Preferences.Advanced.AudioForegroundMediaBehavior
        ndi_discovery: Preferences.Advanced.NDIDiscovery
        support_files_path: str
        manage_media_automatically: bool
        search_paths: Preferences.Advanced.SearchPaths
        def __init__(self, suppress_auto_start: bool = ..., presentation_audio_behavior: _Optional[_Union[Preferences.Advanced.AudioForegroundMediaBehavior, str]] = ..., announcements_audio_behavior: _Optional[_Union[Preferences.Advanced.AudioForegroundMediaBehavior, str]] = ..., ndi_discovery: _Optional[_Union[Preferences.Advanced.NDIDiscovery, _Mapping]] = ..., support_files_path: _Optional[str] = ..., manage_media_automatically: bool = ..., search_paths: _Optional[_Union[Preferences.Advanced.SearchPaths, _Mapping]] = ...) -> None: ...
    class Updates(_message.Message):
        __slots__ = ("notify_when_available", "update_channel")
        class Channel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            production: _ClassVar[Preferences.Updates.Channel]
            beta: _ClassVar[Preferences.Updates.Channel]
        production: Preferences.Updates.Channel
        beta: Preferences.Updates.Channel
        NOTIFY_WHEN_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        notify_when_available: bool
        update_channel: Preferences.Updates.Channel
        def __init__(self, notify_when_available: bool = ..., update_channel: _Optional[_Union[Preferences.Updates.Channel, str]] = ...) -> None: ...
    GENERAL_FIELD_NUMBER: _ClassVar[int]
    SCREENS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SYNC_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    general: Preferences.General
    screens: Preferences.Screens
    groups: Preferences.Groups
    network: Preferences.Network
    sync: Preferences.Sync
    advanced: Preferences.Advanced
    updates: Preferences.Updates
    def __init__(self, general: _Optional[_Union[Preferences.General, _Mapping]] = ..., screens: _Optional[_Union[Preferences.Screens, _Mapping]] = ..., groups: _Optional[_Union[Preferences.Groups, _Mapping]] = ..., network: _Optional[_Union[Preferences.Network, _Mapping]] = ..., sync: _Optional[_Union[Preferences.Sync, _Mapping]] = ..., advanced: _Optional[_Union[Preferences.Advanced, _Mapping]] = ..., updates: _Optional[_Union[Preferences.Updates, _Mapping]] = ..., **kwargs) -> None: ...
