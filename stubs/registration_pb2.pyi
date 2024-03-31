from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("register", "unregister", "change_seat_type", "get_free_bibles", "get_purchased_bibles", "activate_bible", "deactivate_bible", "download_bible", "registration_data", "product_information", "get_upgrades_available", "get_downgrade_available", "download_new_version", "refresh", "activate_link", "update_token", "old_token_data")
    REGISTER_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    GET_FREE_BIBLES_FIELD_NUMBER: _ClassVar[int]
    GET_PURCHASED_BIBLES_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_BIBLE_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_BIBLE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BIBLE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DATA_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    GET_UPGRADES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    GET_DOWNGRADE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_NEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_LINK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OLD_TOKEN_DATA_FIELD_NUMBER: _ClassVar[int]
    register: Register
    unregister: Unregister
    change_seat_type: ChangeSeatType
    get_free_bibles: GetFreeBibles
    get_purchased_bibles: GetPurchasedBibles
    activate_bible: ActivateBible
    deactivate_bible: DeactivateBible
    download_bible: DownloadBible
    registration_data: RegistrationData
    product_information: ProductInformation
    get_upgrades_available: GetAvailableVersion
    get_downgrade_available: GetAvailableVersion
    download_new_version: DownloadNewVersion
    refresh: Refresh
    activate_link: ActivateLink
    update_token: UpdateToken
    old_token_data: OldTokenData
    def __init__(self, register: _Optional[_Union[Register, _Mapping]] = ..., unregister: _Optional[_Union[Unregister, _Mapping]] = ..., change_seat_type: _Optional[_Union[ChangeSeatType, _Mapping]] = ..., get_free_bibles: _Optional[_Union[GetFreeBibles, _Mapping]] = ..., get_purchased_bibles: _Optional[_Union[GetPurchasedBibles, _Mapping]] = ..., activate_bible: _Optional[_Union[ActivateBible, _Mapping]] = ..., deactivate_bible: _Optional[_Union[DeactivateBible, _Mapping]] = ..., download_bible: _Optional[_Union[DownloadBible, _Mapping]] = ..., registration_data: _Optional[_Union[RegistrationData, _Mapping]] = ..., product_information: _Optional[_Union[ProductInformation, _Mapping]] = ..., get_upgrades_available: _Optional[_Union[GetAvailableVersion, _Mapping]] = ..., get_downgrade_available: _Optional[_Union[GetAvailableVersion, _Mapping]] = ..., download_new_version: _Optional[_Union[DownloadNewVersion, _Mapping]] = ..., refresh: _Optional[_Union[Refresh, _Mapping]] = ..., activate_link: _Optional[_Union[ActivateLink, _Mapping]] = ..., update_token: _Optional[_Union[UpdateToken, _Mapping]] = ..., old_token_data: _Optional[_Union[OldTokenData, _Mapping]] = ...) -> None: ...

class Callback(_message.Message):
    __slots__ = ("set_watermark", "deactivation_complete", "free_bibles", "purchased_bibles", "bible_activation_complete", "bible_deactivation_complete", "bible_download_progress", "hard_exit", "read_registration_data", "write_registration_data", "get_product_information", "log", "upgrades_available", "downgrade_available", "download_progress", "alerts", "show_expiration_dialog", "read_old_token", "token", "verification_complete")
    SET_WATERMARK_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    FREE_BIBLES_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_BIBLES_FIELD_NUMBER: _ClassVar[int]
    BIBLE_ACTIVATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    BIBLE_DEACTIVATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    BIBLE_DOWNLOAD_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    HARD_EXIT_FIELD_NUMBER: _ClassVar[int]
    READ_REGISTRATION_DATA_FIELD_NUMBER: _ClassVar[int]
    WRITE_REGISTRATION_DATA_FIELD_NUMBER: _ClassVar[int]
    GET_PRODUCT_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    UPGRADES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DOWNGRADE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    SHOW_EXPIRATION_DIALOG_FIELD_NUMBER: _ClassVar[int]
    READ_OLD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    set_watermark: SetWatermark
    deactivation_complete: DeactivationComplete
    free_bibles: FreeBibles
    purchased_bibles: PurchasedBibles
    bible_activation_complete: BibleActivationComplete
    bible_deactivation_complete: BibleDeactivationComplete
    bible_download_progress: BibleDownloadProgress
    hard_exit: HardExit
    read_registration_data: ReadRegistrationData
    write_registration_data: WriteRegistrationData
    get_product_information: GetProductInformation
    log: Log
    upgrades_available: UpgradesAvailable
    downgrade_available: DowngradeAvailable
    download_progress: DownloadProgress
    alerts: Alerts
    show_expiration_dialog: ShowExpirationDialog
    read_old_token: ReadOldToken
    token: Token
    verification_complete: VerificationComplete
    def __init__(self, set_watermark: _Optional[_Union[SetWatermark, _Mapping]] = ..., deactivation_complete: _Optional[_Union[DeactivationComplete, _Mapping]] = ..., free_bibles: _Optional[_Union[FreeBibles, _Mapping]] = ..., purchased_bibles: _Optional[_Union[PurchasedBibles, _Mapping]] = ..., bible_activation_complete: _Optional[_Union[BibleActivationComplete, _Mapping]] = ..., bible_deactivation_complete: _Optional[_Union[BibleDeactivationComplete, _Mapping]] = ..., bible_download_progress: _Optional[_Union[BibleDownloadProgress, _Mapping]] = ..., hard_exit: _Optional[_Union[HardExit, _Mapping]] = ..., read_registration_data: _Optional[_Union[ReadRegistrationData, _Mapping]] = ..., write_registration_data: _Optional[_Union[WriteRegistrationData, _Mapping]] = ..., get_product_information: _Optional[_Union[GetProductInformation, _Mapping]] = ..., log: _Optional[_Union[Log, _Mapping]] = ..., upgrades_available: _Optional[_Union[UpgradesAvailable, _Mapping]] = ..., downgrade_available: _Optional[_Union[DowngradeAvailable, _Mapping]] = ..., download_progress: _Optional[_Union[DownloadProgress, _Mapping]] = ..., alerts: _Optional[_Union[Alerts, _Mapping]] = ..., show_expiration_dialog: _Optional[_Union[ShowExpirationDialog, _Mapping]] = ..., read_old_token: _Optional[_Union[ReadOldToken, _Mapping]] = ..., token: _Optional[_Union[Token, _Mapping]] = ..., verification_complete: _Optional[_Union[VerificationComplete, _Mapping]] = ...) -> None: ...

class Register(_message.Message):
    __slots__ = ("user_name", "registration_key", "display_name", "seat_type", "channel")
    class SeatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Inactive: _ClassVar[Register.SeatType]
        Basic: _ClassVar[Register.SeatType]
        Advanced: _ClassVar[Register.SeatType]
    Inactive: Register.SeatType
    Basic: Register.SeatType
    Advanced: Register.SeatType
    class UpdateChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Beta: _ClassVar[Register.UpdateChannel]
        Production: _ClassVar[Register.UpdateChannel]
    Beta: Register.UpdateChannel
    Production: Register.UpdateChannel
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    registration_key: str
    display_name: str
    seat_type: Register.SeatType
    channel: Register.UpdateChannel
    def __init__(self, user_name: _Optional[str] = ..., registration_key: _Optional[str] = ..., display_name: _Optional[str] = ..., seat_type: _Optional[_Union[Register.SeatType, str]] = ..., channel: _Optional[_Union[Register.UpdateChannel, str]] = ...) -> None: ...

class ActivateLink(_message.Message):
    __slots__ = ("identifier",)
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    def __init__(self, identifier: _Optional[str] = ...) -> None: ...

class Unregister(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChangeSeatType(_message.Message):
    __slots__ = ("seat_type", "channel")
    class SeatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Inactive: _ClassVar[ChangeSeatType.SeatType]
        Basic: _ClassVar[ChangeSeatType.SeatType]
        Advanced: _ClassVar[ChangeSeatType.SeatType]
    Inactive: ChangeSeatType.SeatType
    Basic: ChangeSeatType.SeatType
    Advanced: ChangeSeatType.SeatType
    class UpdateChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Beta: _ClassVar[ChangeSeatType.UpdateChannel]
        Production: _ClassVar[ChangeSeatType.UpdateChannel]
    Beta: ChangeSeatType.UpdateChannel
    Production: ChangeSeatType.UpdateChannel
    SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    seat_type: ChangeSeatType.SeatType
    channel: ChangeSeatType.UpdateChannel
    def __init__(self, seat_type: _Optional[_Union[ChangeSeatType.SeatType, str]] = ..., channel: _Optional[_Union[ChangeSeatType.UpdateChannel, str]] = ...) -> None: ...

class GetFreeBibles(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPurchasedBibles(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ActivateBible(_message.Message):
    __slots__ = ("bible_id",)
    BIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    bible_id: str
    def __init__(self, bible_id: _Optional[str] = ...) -> None: ...

class DeactivateBible(_message.Message):
    __slots__ = ("bible_id",)
    BIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    bible_id: str
    def __init__(self, bible_id: _Optional[str] = ...) -> None: ...

class DownloadBible(_message.Message):
    __slots__ = ("bible_id", "filename")
    BIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    bible_id: str
    filename: str
    def __init__(self, bible_id: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class RegistrationData(_message.Message):
    __slots__ = ("data", "channel")
    class UpdateChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Beta: _ClassVar[RegistrationData.UpdateChannel]
        Production: _ClassVar[RegistrationData.UpdateChannel]
    Beta: RegistrationData.UpdateChannel
    Production: RegistrationData.UpdateChannel
    DATA_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    channel: RegistrationData.UpdateChannel
    def __init__(self, data: _Optional[bytes] = ..., channel: _Optional[_Union[RegistrationData.UpdateChannel, str]] = ...) -> None: ...

class ProductInformation(_message.Message):
    __slots__ = ("product_name", "major_version", "minor_version", "patch_version", "build_number", "build_date")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    BUILD_DATE_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    major_version: str
    minor_version: str
    patch_version: str
    build_number: str
    build_date: int
    def __init__(self, product_name: _Optional[str] = ..., major_version: _Optional[str] = ..., minor_version: _Optional[str] = ..., patch_version: _Optional[str] = ..., build_number: _Optional[str] = ..., build_date: _Optional[int] = ...) -> None: ...

class GetAvailableVersion(_message.Message):
    __slots__ = ("include_notes", "channel", "format")
    INCLUDE_NOTES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    include_notes: bool
    channel: str
    format: str
    def __init__(self, include_notes: bool = ..., channel: _Optional[str] = ..., format: _Optional[str] = ...) -> None: ...

class DownloadNewVersion(_message.Message):
    __slots__ = ("url", "filename")
    URL_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    url: str
    filename: str
    def __init__(self, url: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class Refresh(_message.Message):
    __slots__ = ("channel",)
    class UpdateChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Beta: _ClassVar[Refresh.UpdateChannel]
        Production: _ClassVar[Refresh.UpdateChannel]
    Beta: Refresh.UpdateChannel
    Production: Refresh.UpdateChannel
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: Refresh.UpdateChannel
    def __init__(self, channel: _Optional[_Union[Refresh.UpdateChannel, str]] = ...) -> None: ...

class UpdateToken(_message.Message):
    __slots__ = ("token_metadata",)
    TOKEN_METADATA_FIELD_NUMBER: _ClassVar[int]
    token_metadata: TokenMetadata
    def __init__(self, token_metadata: _Optional[_Union[TokenMetadata, _Mapping]] = ...) -> None: ...

class OldTokenData(_message.Message):
    __slots__ = ("status", "token")
    class ReadTokenStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ReadTokenSuccess: _ClassVar[OldTokenData.ReadTokenStatus]
        TokenNotPresent: _ClassVar[OldTokenData.ReadTokenStatus]
    ReadTokenSuccess: OldTokenData.ReadTokenStatus
    TokenNotPresent: OldTokenData.ReadTokenStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    status: OldTokenData.ReadTokenStatus
    token: TokenMetadata
    def __init__(self, status: _Optional[_Union[OldTokenData.ReadTokenStatus, str]] = ..., token: _Optional[_Union[TokenMetadata, _Mapping]] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ("token_metadata",)
    TOKEN_METADATA_FIELD_NUMBER: _ClassVar[int]
    token_metadata: TokenMetadata
    def __init__(self, token_metadata: _Optional[_Union[TokenMetadata, _Mapping]] = ...) -> None: ...

class SetWatermark(_message.Message):
    __slots__ = ("is_registered", "active_seat")
    IS_REGISTERED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SEAT_FIELD_NUMBER: _ClassVar[int]
    is_registered: bool
    active_seat: bool
    def __init__(self, is_registered: bool = ..., active_seat: bool = ...) -> None: ...

class ActivationComplete(_message.Message):
    __slots__ = ("result", "registration_info", "available_seats", "total_seats")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[ActivationComplete.Status]
        ExpiredLicense: _ClassVar[ActivationComplete.Status]
        DeactivatedLicense: _ClassVar[ActivationComplete.Status]
        DisabledLicense: _ClassVar[ActivationComplete.Status]
        NoSeats: _ClassVar[ActivationComplete.Status]
        NoCopies: _ClassVar[ActivationComplete.Status]
        MissingLicense: _ClassVar[ActivationComplete.Status]
        TimeDiscrepancy: _ClassVar[ActivationComplete.Status]
        BibleMissing: _ClassVar[ActivationComplete.Status]
        BibleNotPurchased: _ClassVar[ActivationComplete.Status]
        BibleActivationMissing: _ClassVar[ActivationComplete.Status]
        BibleDeactivated: _ClassVar[ActivationComplete.Status]
        NetworkError: _ClassVar[ActivationComplete.Status]
        IOError: _ClassVar[ActivationComplete.Status]
        NotInitialized: _ClassVar[ActivationComplete.Status]
        UnknownError: _ClassVar[ActivationComplete.Status]
    Success: ActivationComplete.Status
    ExpiredLicense: ActivationComplete.Status
    DeactivatedLicense: ActivationComplete.Status
    DisabledLicense: ActivationComplete.Status
    NoSeats: ActivationComplete.Status
    NoCopies: ActivationComplete.Status
    MissingLicense: ActivationComplete.Status
    TimeDiscrepancy: ActivationComplete.Status
    BibleMissing: ActivationComplete.Status
    BibleNotPurchased: ActivationComplete.Status
    BibleActivationMissing: ActivationComplete.Status
    BibleDeactivated: ActivationComplete.Status
    NetworkError: ActivationComplete.Status
    IOError: ActivationComplete.Status
    NotInitialized: ActivationComplete.Status
    UnknownError: ActivationComplete.Status
    RESULT_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SEATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SEATS_FIELD_NUMBER: _ClassVar[int]
    result: ActivationComplete.Status
    registration_info: RegistrationInfo
    available_seats: Seats
    total_seats: Seats
    def __init__(self, result: _Optional[_Union[ActivationComplete.Status, str]] = ..., registration_info: _Optional[_Union[RegistrationInfo, _Mapping]] = ..., available_seats: _Optional[_Union[Seats, _Mapping]] = ..., total_seats: _Optional[_Union[Seats, _Mapping]] = ...) -> None: ...

class DeactivationComplete(_message.Message):
    __slots__ = ("result",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[DeactivationComplete.Status]
        ExpiredLicense: _ClassVar[DeactivationComplete.Status]
        DeactivatedLicense: _ClassVar[DeactivationComplete.Status]
        DisabledLicense: _ClassVar[DeactivationComplete.Status]
        NoSeats: _ClassVar[DeactivationComplete.Status]
        NoCopies: _ClassVar[DeactivationComplete.Status]
        MissingLicense: _ClassVar[DeactivationComplete.Status]
        TimeDiscrepancy: _ClassVar[DeactivationComplete.Status]
        BibleMissing: _ClassVar[DeactivationComplete.Status]
        BibleNotPurchased: _ClassVar[DeactivationComplete.Status]
        BibleActivationMissing: _ClassVar[DeactivationComplete.Status]
        BibleDeactivated: _ClassVar[DeactivationComplete.Status]
        NetworkError: _ClassVar[DeactivationComplete.Status]
        IOError: _ClassVar[DeactivationComplete.Status]
        NotInitialized: _ClassVar[DeactivationComplete.Status]
        UnknownError: _ClassVar[DeactivationComplete.Status]
    Success: DeactivationComplete.Status
    ExpiredLicense: DeactivationComplete.Status
    DeactivatedLicense: DeactivationComplete.Status
    DisabledLicense: DeactivationComplete.Status
    NoSeats: DeactivationComplete.Status
    NoCopies: DeactivationComplete.Status
    MissingLicense: DeactivationComplete.Status
    TimeDiscrepancy: DeactivationComplete.Status
    BibleMissing: DeactivationComplete.Status
    BibleNotPurchased: DeactivationComplete.Status
    BibleActivationMissing: DeactivationComplete.Status
    BibleDeactivated: DeactivationComplete.Status
    NetworkError: DeactivationComplete.Status
    IOError: DeactivationComplete.Status
    NotInitialized: DeactivationComplete.Status
    UnknownError: DeactivationComplete.Status
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: DeactivationComplete.Status
    def __init__(self, result: _Optional[_Union[DeactivationComplete.Status, str]] = ...) -> None: ...

class ChangeSeatTypeComplete(_message.Message):
    __slots__ = ("result", "available_seats", "total_seats", "seat_type")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[ChangeSeatTypeComplete.Status]
        ExpiredLicense: _ClassVar[ChangeSeatTypeComplete.Status]
        DeactivatedLicense: _ClassVar[ChangeSeatTypeComplete.Status]
        DisabledLicense: _ClassVar[ChangeSeatTypeComplete.Status]
        NoSeats: _ClassVar[ChangeSeatTypeComplete.Status]
        NoCopies: _ClassVar[ChangeSeatTypeComplete.Status]
        MissingLicense: _ClassVar[ChangeSeatTypeComplete.Status]
        TimeDiscrepancy: _ClassVar[ChangeSeatTypeComplete.Status]
        BibleMissing: _ClassVar[ChangeSeatTypeComplete.Status]
        BibleNotPurchased: _ClassVar[ChangeSeatTypeComplete.Status]
        BibleActivationMissing: _ClassVar[ChangeSeatTypeComplete.Status]
        BibleDeactivated: _ClassVar[ChangeSeatTypeComplete.Status]
        NetworkError: _ClassVar[ChangeSeatTypeComplete.Status]
        IOError: _ClassVar[ChangeSeatTypeComplete.Status]
        NotInitialized: _ClassVar[ChangeSeatTypeComplete.Status]
        UnknownError: _ClassVar[ChangeSeatTypeComplete.Status]
    Success: ChangeSeatTypeComplete.Status
    ExpiredLicense: ChangeSeatTypeComplete.Status
    DeactivatedLicense: ChangeSeatTypeComplete.Status
    DisabledLicense: ChangeSeatTypeComplete.Status
    NoSeats: ChangeSeatTypeComplete.Status
    NoCopies: ChangeSeatTypeComplete.Status
    MissingLicense: ChangeSeatTypeComplete.Status
    TimeDiscrepancy: ChangeSeatTypeComplete.Status
    BibleMissing: ChangeSeatTypeComplete.Status
    BibleNotPurchased: ChangeSeatTypeComplete.Status
    BibleActivationMissing: ChangeSeatTypeComplete.Status
    BibleDeactivated: ChangeSeatTypeComplete.Status
    NetworkError: ChangeSeatTypeComplete.Status
    IOError: ChangeSeatTypeComplete.Status
    NotInitialized: ChangeSeatTypeComplete.Status
    UnknownError: ChangeSeatTypeComplete.Status
    class SeatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Inactive: _ClassVar[ChangeSeatTypeComplete.SeatType]
        Basic: _ClassVar[ChangeSeatTypeComplete.SeatType]
        Advanced: _ClassVar[ChangeSeatTypeComplete.SeatType]
    Inactive: ChangeSeatTypeComplete.SeatType
    Basic: ChangeSeatTypeComplete.SeatType
    Advanced: ChangeSeatTypeComplete.SeatType
    RESULT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SEATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SEATS_FIELD_NUMBER: _ClassVar[int]
    SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    result: ChangeSeatTypeComplete.Status
    available_seats: Seats
    total_seats: Seats
    seat_type: ChangeSeatTypeComplete.SeatType
    def __init__(self, result: _Optional[_Union[ChangeSeatTypeComplete.Status, str]] = ..., available_seats: _Optional[_Union[Seats, _Mapping]] = ..., total_seats: _Optional[_Union[Seats, _Mapping]] = ..., seat_type: _Optional[_Union[ChangeSeatTypeComplete.SeatType, str]] = ...) -> None: ...

class FreeBibles(_message.Message):
    __slots__ = ("status", "bibles")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[FreeBibles.Status]
        ExpiredLicense: _ClassVar[FreeBibles.Status]
        DeactivatedLicense: _ClassVar[FreeBibles.Status]
        DisabledLicense: _ClassVar[FreeBibles.Status]
        NoSeats: _ClassVar[FreeBibles.Status]
        NoCopies: _ClassVar[FreeBibles.Status]
        MissingLicense: _ClassVar[FreeBibles.Status]
        TimeDiscrepancy: _ClassVar[FreeBibles.Status]
        BibleMissing: _ClassVar[FreeBibles.Status]
        BibleNotPurchased: _ClassVar[FreeBibles.Status]
        BibleActivationMissing: _ClassVar[FreeBibles.Status]
        BibleDeactivated: _ClassVar[FreeBibles.Status]
        NetworkError: _ClassVar[FreeBibles.Status]
        IOError: _ClassVar[FreeBibles.Status]
        NotInitialized: _ClassVar[FreeBibles.Status]
        UnknownError: _ClassVar[FreeBibles.Status]
    Success: FreeBibles.Status
    ExpiredLicense: FreeBibles.Status
    DeactivatedLicense: FreeBibles.Status
    DisabledLicense: FreeBibles.Status
    NoSeats: FreeBibles.Status
    NoCopies: FreeBibles.Status
    MissingLicense: FreeBibles.Status
    TimeDiscrepancy: FreeBibles.Status
    BibleMissing: FreeBibles.Status
    BibleNotPurchased: FreeBibles.Status
    BibleActivationMissing: FreeBibles.Status
    BibleDeactivated: FreeBibles.Status
    NetworkError: FreeBibles.Status
    IOError: FreeBibles.Status
    NotInitialized: FreeBibles.Status
    UnknownError: FreeBibles.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BIBLES_FIELD_NUMBER: _ClassVar[int]
    status: FreeBibles.Status
    bibles: _containers.RepeatedCompositeFieldContainer[Bible]
    def __init__(self, status: _Optional[_Union[FreeBibles.Status, str]] = ..., bibles: _Optional[_Iterable[_Union[Bible, _Mapping]]] = ...) -> None: ...

class PurchasedBibles(_message.Message):
    __slots__ = ("status", "bibles")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[PurchasedBibles.Status]
        ExpiredLicense: _ClassVar[PurchasedBibles.Status]
        DeactivatedLicense: _ClassVar[PurchasedBibles.Status]
        DisabledLicense: _ClassVar[PurchasedBibles.Status]
        NoSeats: _ClassVar[PurchasedBibles.Status]
        NoCopies: _ClassVar[PurchasedBibles.Status]
        MissingLicense: _ClassVar[PurchasedBibles.Status]
        TimeDiscrepancy: _ClassVar[PurchasedBibles.Status]
        BibleMissing: _ClassVar[PurchasedBibles.Status]
        BibleNotPurchased: _ClassVar[PurchasedBibles.Status]
        BibleActivationMissing: _ClassVar[PurchasedBibles.Status]
        BibleDeactivated: _ClassVar[PurchasedBibles.Status]
        NetworkError: _ClassVar[PurchasedBibles.Status]
        IOError: _ClassVar[PurchasedBibles.Status]
        NotInitialized: _ClassVar[PurchasedBibles.Status]
        UnknownError: _ClassVar[PurchasedBibles.Status]
    Success: PurchasedBibles.Status
    ExpiredLicense: PurchasedBibles.Status
    DeactivatedLicense: PurchasedBibles.Status
    DisabledLicense: PurchasedBibles.Status
    NoSeats: PurchasedBibles.Status
    NoCopies: PurchasedBibles.Status
    MissingLicense: PurchasedBibles.Status
    TimeDiscrepancy: PurchasedBibles.Status
    BibleMissing: PurchasedBibles.Status
    BibleNotPurchased: PurchasedBibles.Status
    BibleActivationMissing: PurchasedBibles.Status
    BibleDeactivated: PurchasedBibles.Status
    NetworkError: PurchasedBibles.Status
    IOError: PurchasedBibles.Status
    NotInitialized: PurchasedBibles.Status
    UnknownError: PurchasedBibles.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BIBLES_FIELD_NUMBER: _ClassVar[int]
    status: PurchasedBibles.Status
    bibles: _containers.RepeatedCompositeFieldContainer[PurchasedBible]
    def __init__(self, status: _Optional[_Union[PurchasedBibles.Status, str]] = ..., bibles: _Optional[_Iterable[_Union[PurchasedBible, _Mapping]]] = ...) -> None: ...

class BibleActivationComplete(_message.Message):
    __slots__ = ("status", "bible_id", "download_link", "bibles")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[BibleActivationComplete.Status]
        ExpiredLicense: _ClassVar[BibleActivationComplete.Status]
        DeactivatedLicense: _ClassVar[BibleActivationComplete.Status]
        DisabledLicense: _ClassVar[BibleActivationComplete.Status]
        NoSeats: _ClassVar[BibleActivationComplete.Status]
        NoCopies: _ClassVar[BibleActivationComplete.Status]
        MissingLicense: _ClassVar[BibleActivationComplete.Status]
        TimeDiscrepancy: _ClassVar[BibleActivationComplete.Status]
        BibleMissing: _ClassVar[BibleActivationComplete.Status]
        BibleNotPurchased: _ClassVar[BibleActivationComplete.Status]
        BibleActivationMissing: _ClassVar[BibleActivationComplete.Status]
        BibleDeactivated: _ClassVar[BibleActivationComplete.Status]
        NetworkError: _ClassVar[BibleActivationComplete.Status]
        IOError: _ClassVar[BibleActivationComplete.Status]
        NotInitialized: _ClassVar[BibleActivationComplete.Status]
        UnknownError: _ClassVar[BibleActivationComplete.Status]
    Success: BibleActivationComplete.Status
    ExpiredLicense: BibleActivationComplete.Status
    DeactivatedLicense: BibleActivationComplete.Status
    DisabledLicense: BibleActivationComplete.Status
    NoSeats: BibleActivationComplete.Status
    NoCopies: BibleActivationComplete.Status
    MissingLicense: BibleActivationComplete.Status
    TimeDiscrepancy: BibleActivationComplete.Status
    BibleMissing: BibleActivationComplete.Status
    BibleNotPurchased: BibleActivationComplete.Status
    BibleActivationMissing: BibleActivationComplete.Status
    BibleDeactivated: BibleActivationComplete.Status
    NetworkError: BibleActivationComplete.Status
    IOError: BibleActivationComplete.Status
    NotInitialized: BibleActivationComplete.Status
    UnknownError: BibleActivationComplete.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    BIBLES_FIELD_NUMBER: _ClassVar[int]
    status: BibleActivationComplete.Status
    bible_id: str
    download_link: str
    bibles: _containers.RepeatedCompositeFieldContainer[PurchasedBible]
    def __init__(self, status: _Optional[_Union[BibleActivationComplete.Status, str]] = ..., bible_id: _Optional[str] = ..., download_link: _Optional[str] = ..., bibles: _Optional[_Iterable[_Union[PurchasedBible, _Mapping]]] = ...) -> None: ...

class BibleDeactivationComplete(_message.Message):
    __slots__ = ("status", "bible_id", "bibles")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[BibleDeactivationComplete.Status]
        ExpiredLicense: _ClassVar[BibleDeactivationComplete.Status]
        DeactivatedLicense: _ClassVar[BibleDeactivationComplete.Status]
        DisabledLicense: _ClassVar[BibleDeactivationComplete.Status]
        NoSeats: _ClassVar[BibleDeactivationComplete.Status]
        NoCopies: _ClassVar[BibleDeactivationComplete.Status]
        MissingLicense: _ClassVar[BibleDeactivationComplete.Status]
        TimeDiscrepancy: _ClassVar[BibleDeactivationComplete.Status]
        BibleMissing: _ClassVar[BibleDeactivationComplete.Status]
        BibleNotPurchased: _ClassVar[BibleDeactivationComplete.Status]
        BibleActivationMissing: _ClassVar[BibleDeactivationComplete.Status]
        BibleDeactivated: _ClassVar[BibleDeactivationComplete.Status]
        NetworkError: _ClassVar[BibleDeactivationComplete.Status]
        IOError: _ClassVar[BibleDeactivationComplete.Status]
        NotInitialized: _ClassVar[BibleDeactivationComplete.Status]
        UnknownError: _ClassVar[BibleDeactivationComplete.Status]
    Success: BibleDeactivationComplete.Status
    ExpiredLicense: BibleDeactivationComplete.Status
    DeactivatedLicense: BibleDeactivationComplete.Status
    DisabledLicense: BibleDeactivationComplete.Status
    NoSeats: BibleDeactivationComplete.Status
    NoCopies: BibleDeactivationComplete.Status
    MissingLicense: BibleDeactivationComplete.Status
    TimeDiscrepancy: BibleDeactivationComplete.Status
    BibleMissing: BibleDeactivationComplete.Status
    BibleNotPurchased: BibleDeactivationComplete.Status
    BibleActivationMissing: BibleDeactivationComplete.Status
    BibleDeactivated: BibleDeactivationComplete.Status
    NetworkError: BibleDeactivationComplete.Status
    IOError: BibleDeactivationComplete.Status
    NotInitialized: BibleDeactivationComplete.Status
    UnknownError: BibleDeactivationComplete.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    BIBLES_FIELD_NUMBER: _ClassVar[int]
    status: BibleDeactivationComplete.Status
    bible_id: str
    bibles: _containers.RepeatedCompositeFieldContainer[PurchasedBible]
    def __init__(self, status: _Optional[_Union[BibleDeactivationComplete.Status, str]] = ..., bible_id: _Optional[str] = ..., bibles: _Optional[_Iterable[_Union[PurchasedBible, _Mapping]]] = ...) -> None: ...

class BibleDownloadProgress(_message.Message):
    __slots__ = ("status", "complete", "progress", "bible_id", "file_name", "download_link")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[BibleDownloadProgress.Status]
        ExpiredLicense: _ClassVar[BibleDownloadProgress.Status]
        DeactivatedLicense: _ClassVar[BibleDownloadProgress.Status]
        DisabledLicense: _ClassVar[BibleDownloadProgress.Status]
        NoSeats: _ClassVar[BibleDownloadProgress.Status]
        NoCopies: _ClassVar[BibleDownloadProgress.Status]
        MissingLicense: _ClassVar[BibleDownloadProgress.Status]
        TimeDiscrepancy: _ClassVar[BibleDownloadProgress.Status]
        BibleMissing: _ClassVar[BibleDownloadProgress.Status]
        BibleNotPurchased: _ClassVar[BibleDownloadProgress.Status]
        BibleActivationMissing: _ClassVar[BibleDownloadProgress.Status]
        BibleDeactivated: _ClassVar[BibleDownloadProgress.Status]
        NetworkError: _ClassVar[BibleDownloadProgress.Status]
        IOError: _ClassVar[BibleDownloadProgress.Status]
        NotInitialized: _ClassVar[BibleDownloadProgress.Status]
        UnknownError: _ClassVar[BibleDownloadProgress.Status]
    Success: BibleDownloadProgress.Status
    ExpiredLicense: BibleDownloadProgress.Status
    DeactivatedLicense: BibleDownloadProgress.Status
    DisabledLicense: BibleDownloadProgress.Status
    NoSeats: BibleDownloadProgress.Status
    NoCopies: BibleDownloadProgress.Status
    MissingLicense: BibleDownloadProgress.Status
    TimeDiscrepancy: BibleDownloadProgress.Status
    BibleMissing: BibleDownloadProgress.Status
    BibleNotPurchased: BibleDownloadProgress.Status
    BibleActivationMissing: BibleDownloadProgress.Status
    BibleDeactivated: BibleDownloadProgress.Status
    NetworkError: BibleDownloadProgress.Status
    IOError: BibleDownloadProgress.Status
    NotInitialized: BibleDownloadProgress.Status
    UnknownError: BibleDownloadProgress.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    BIBLE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    status: BibleDownloadProgress.Status
    complete: bool
    progress: float
    bible_id: str
    file_name: str
    download_link: str
    def __init__(self, status: _Optional[_Union[BibleDownloadProgress.Status, str]] = ..., complete: bool = ..., progress: _Optional[float] = ..., bible_id: _Optional[str] = ..., file_name: _Optional[str] = ..., download_link: _Optional[str] = ...) -> None: ...

class HardExit(_message.Message):
    __slots__ = ("reason",)
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HostsFile: _ClassVar[HardExit.Reason]
        SystemTime: _ClassVar[HardExit.Reason]
    HostsFile: HardExit.Reason
    SystemTime: HardExit.Reason
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: HardExit.Reason
    def __init__(self, reason: _Optional[_Union[HardExit.Reason, str]] = ...) -> None: ...

class ReadRegistrationData(_message.Message):
    __slots__ = ("fingerprint", "identifier")
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    fingerprint: str
    identifier: str
    def __init__(self, fingerprint: _Optional[str] = ..., identifier: _Optional[str] = ...) -> None: ...

class ReadOldToken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WriteRegistrationData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class GetProductInformation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Log(_message.Message):
    __slots__ = ("level", "message")
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Debug: _ClassVar[Log.Level]
        Info: _ClassVar[Log.Level]
        Warning: _ClassVar[Log.Level]
        Error: _ClassVar[Log.Level]
    Debug: Log.Level
    Info: Log.Level
    Warning: Log.Level
    Error: Log.Level
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    level: Log.Level
    message: str
    def __init__(self, level: _Optional[_Union[Log.Level, str]] = ..., message: _Optional[str] = ...) -> None: ...

class UpgradesAvailable(_message.Message):
    __slots__ = ("status", "is_non_production_active", "active_channel", "release_notes", "upgrades")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[UpgradesAvailable.Status]
        ExpiredLicense: _ClassVar[UpgradesAvailable.Status]
        DeactivatedLicense: _ClassVar[UpgradesAvailable.Status]
        DisabledLicense: _ClassVar[UpgradesAvailable.Status]
        NoSeats: _ClassVar[UpgradesAvailable.Status]
        NoCopies: _ClassVar[UpgradesAvailable.Status]
        MissingLicense: _ClassVar[UpgradesAvailable.Status]
        TimeDiscrepancy: _ClassVar[UpgradesAvailable.Status]
        BibleMissing: _ClassVar[UpgradesAvailable.Status]
        BibleNotPurchased: _ClassVar[UpgradesAvailable.Status]
        BibleActivationMissing: _ClassVar[UpgradesAvailable.Status]
        BibleDeactivated: _ClassVar[UpgradesAvailable.Status]
        NetworkError: _ClassVar[UpgradesAvailable.Status]
        IOError: _ClassVar[UpgradesAvailable.Status]
        NotInitialized: _ClassVar[UpgradesAvailable.Status]
        UnknownError: _ClassVar[UpgradesAvailable.Status]
    Success: UpgradesAvailable.Status
    ExpiredLicense: UpgradesAvailable.Status
    DeactivatedLicense: UpgradesAvailable.Status
    DisabledLicense: UpgradesAvailable.Status
    NoSeats: UpgradesAvailable.Status
    NoCopies: UpgradesAvailable.Status
    MissingLicense: UpgradesAvailable.Status
    TimeDiscrepancy: UpgradesAvailable.Status
    BibleMissing: UpgradesAvailable.Status
    BibleNotPurchased: UpgradesAvailable.Status
    BibleActivationMissing: UpgradesAvailable.Status
    BibleDeactivated: UpgradesAvailable.Status
    NetworkError: UpgradesAvailable.Status
    IOError: UpgradesAvailable.Status
    NotInitialized: UpgradesAvailable.Status
    UnknownError: UpgradesAvailable.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_NON_PRODUCTION_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NOTES_FIELD_NUMBER: _ClassVar[int]
    UPGRADES_FIELD_NUMBER: _ClassVar[int]
    status: UpgradesAvailable.Status
    is_non_production_active: bool
    active_channel: str
    release_notes: str
    upgrades: _containers.RepeatedCompositeFieldContainer[BuildInformation]
    def __init__(self, status: _Optional[_Union[UpgradesAvailable.Status, str]] = ..., is_non_production_active: bool = ..., active_channel: _Optional[str] = ..., release_notes: _Optional[str] = ..., upgrades: _Optional[_Iterable[_Union[BuildInformation, _Mapping]]] = ...) -> None: ...

class DowngradeAvailable(_message.Message):
    __slots__ = ("status", "downgrade", "release_notes")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[DowngradeAvailable.Status]
        ExpiredLicense: _ClassVar[DowngradeAvailable.Status]
        DeactivatedLicense: _ClassVar[DowngradeAvailable.Status]
        DisabledLicense: _ClassVar[DowngradeAvailable.Status]
        NoSeats: _ClassVar[DowngradeAvailable.Status]
        NoCopies: _ClassVar[DowngradeAvailable.Status]
        MissingLicense: _ClassVar[DowngradeAvailable.Status]
        TimeDiscrepancy: _ClassVar[DowngradeAvailable.Status]
        BibleMissing: _ClassVar[DowngradeAvailable.Status]
        BibleNotPurchased: _ClassVar[DowngradeAvailable.Status]
        BibleActivationMissing: _ClassVar[DowngradeAvailable.Status]
        BibleDeactivated: _ClassVar[DowngradeAvailable.Status]
        NetworkError: _ClassVar[DowngradeAvailable.Status]
        IOError: _ClassVar[DowngradeAvailable.Status]
        NotInitialized: _ClassVar[DowngradeAvailable.Status]
        UnknownError: _ClassVar[DowngradeAvailable.Status]
    Success: DowngradeAvailable.Status
    ExpiredLicense: DowngradeAvailable.Status
    DeactivatedLicense: DowngradeAvailable.Status
    DisabledLicense: DowngradeAvailable.Status
    NoSeats: DowngradeAvailable.Status
    NoCopies: DowngradeAvailable.Status
    MissingLicense: DowngradeAvailable.Status
    TimeDiscrepancy: DowngradeAvailable.Status
    BibleMissing: DowngradeAvailable.Status
    BibleNotPurchased: DowngradeAvailable.Status
    BibleActivationMissing: DowngradeAvailable.Status
    BibleDeactivated: DowngradeAvailable.Status
    NetworkError: DowngradeAvailable.Status
    IOError: DowngradeAvailable.Status
    NotInitialized: DowngradeAvailable.Status
    UnknownError: DowngradeAvailable.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DOWNGRADE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NOTES_FIELD_NUMBER: _ClassVar[int]
    status: DowngradeAvailable.Status
    downgrade: BuildInformation
    release_notes: str
    def __init__(self, status: _Optional[_Union[DowngradeAvailable.Status, str]] = ..., downgrade: _Optional[_Union[BuildInformation, _Mapping]] = ..., release_notes: _Optional[str] = ...) -> None: ...

class DownloadProgress(_message.Message):
    __slots__ = ("status", "complete", "progress")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[DownloadProgress.Status]
        ExpiredLicense: _ClassVar[DownloadProgress.Status]
        DeactivatedLicense: _ClassVar[DownloadProgress.Status]
        DisabledLicense: _ClassVar[DownloadProgress.Status]
        NoSeats: _ClassVar[DownloadProgress.Status]
        NoCopies: _ClassVar[DownloadProgress.Status]
        MissingLicense: _ClassVar[DownloadProgress.Status]
        TimeDiscrepancy: _ClassVar[DownloadProgress.Status]
        BibleMissing: _ClassVar[DownloadProgress.Status]
        BibleNotPurchased: _ClassVar[DownloadProgress.Status]
        BibleActivationMissing: _ClassVar[DownloadProgress.Status]
        BibleDeactivated: _ClassVar[DownloadProgress.Status]
        NetworkError: _ClassVar[DownloadProgress.Status]
        IOError: _ClassVar[DownloadProgress.Status]
        NotInitialized: _ClassVar[DownloadProgress.Status]
        UnknownError: _ClassVar[DownloadProgress.Status]
    Success: DownloadProgress.Status
    ExpiredLicense: DownloadProgress.Status
    DeactivatedLicense: DownloadProgress.Status
    DisabledLicense: DownloadProgress.Status
    NoSeats: DownloadProgress.Status
    NoCopies: DownloadProgress.Status
    MissingLicense: DownloadProgress.Status
    TimeDiscrepancy: DownloadProgress.Status
    BibleMissing: DownloadProgress.Status
    BibleNotPurchased: DownloadProgress.Status
    BibleActivationMissing: DownloadProgress.Status
    BibleDeactivated: DownloadProgress.Status
    NetworkError: DownloadProgress.Status
    IOError: DownloadProgress.Status
    NotInitialized: DownloadProgress.Status
    UnknownError: DownloadProgress.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    status: DownloadProgress.Status
    complete: bool
    progress: float
    def __init__(self, status: _Optional[_Union[DownloadProgress.Status, str]] = ..., complete: bool = ..., progress: _Optional[float] = ...) -> None: ...

class Alerts(_message.Message):
    __slots__ = ("alerts",)
    ALERTS_FIELD_NUMBER: _ClassVar[int]
    alerts: _containers.RepeatedCompositeFieldContainer[Alert]
    def __init__(self, alerts: _Optional[_Iterable[_Union[Alert, _Mapping]]] = ...) -> None: ...

class ShowExpirationDialog(_message.Message):
    __slots__ = ("days",)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int
    def __init__(self, days: _Optional[int] = ...) -> None: ...

class LicenseInfo(_message.Message):
    __slots__ = ("registration_info", "available_seats", "total_seats", "legacy")
    REGISTRATION_INFO_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SEATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SEATS_FIELD_NUMBER: _ClassVar[int]
    LEGACY_FIELD_NUMBER: _ClassVar[int]
    registration_info: RegistrationInfo
    available_seats: Seats
    total_seats: Seats
    legacy: bool
    def __init__(self, registration_info: _Optional[_Union[RegistrationInfo, _Mapping]] = ..., available_seats: _Optional[_Union[Seats, _Mapping]] = ..., total_seats: _Optional[_Union[Seats, _Mapping]] = ..., legacy: bool = ...) -> None: ...

class VerificationComplete(_message.Message):
    __slots__ = ("result", "license", "bibles", "token", "subscription_info", "alert", "banner")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Success: _ClassVar[VerificationComplete.Status]
        ExpiredLicense: _ClassVar[VerificationComplete.Status]
        DeactivatedLicense: _ClassVar[VerificationComplete.Status]
        DisabledLicense: _ClassVar[VerificationComplete.Status]
        NoSeats: _ClassVar[VerificationComplete.Status]
        NoCopies: _ClassVar[VerificationComplete.Status]
        MissingLicense: _ClassVar[VerificationComplete.Status]
        TimeDiscrepancy: _ClassVar[VerificationComplete.Status]
        BibleMissing: _ClassVar[VerificationComplete.Status]
        BibleNotPurchased: _ClassVar[VerificationComplete.Status]
        BibleActivationMissing: _ClassVar[VerificationComplete.Status]
        BibleDeactivated: _ClassVar[VerificationComplete.Status]
        NetworkError: _ClassVar[VerificationComplete.Status]
        IOError: _ClassVar[VerificationComplete.Status]
        NotInitialized: _ClassVar[VerificationComplete.Status]
        UnknownError: _ClassVar[VerificationComplete.Status]
    Success: VerificationComplete.Status
    ExpiredLicense: VerificationComplete.Status
    DeactivatedLicense: VerificationComplete.Status
    DisabledLicense: VerificationComplete.Status
    NoSeats: VerificationComplete.Status
    NoCopies: VerificationComplete.Status
    MissingLicense: VerificationComplete.Status
    TimeDiscrepancy: VerificationComplete.Status
    BibleMissing: VerificationComplete.Status
    BibleNotPurchased: VerificationComplete.Status
    BibleActivationMissing: VerificationComplete.Status
    BibleDeactivated: VerificationComplete.Status
    NetworkError: VerificationComplete.Status
    IOError: VerificationComplete.Status
    NotInitialized: VerificationComplete.Status
    UnknownError: VerificationComplete.Status
    class PopupAlertMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NoPopupAlert: _ClassVar[VerificationComplete.PopupAlertMessage]
        Activation: _ClassVar[VerificationComplete.PopupAlertMessage]
        ActivationNoSeat: _ClassVar[VerificationComplete.PopupAlertMessage]
        NotSignedIn: _ClassVar[VerificationComplete.PopupAlertMessage]
        SignedInNoSubscription: _ClassVar[VerificationComplete.PopupAlertMessage]
    NoPopupAlert: VerificationComplete.PopupAlertMessage
    Activation: VerificationComplete.PopupAlertMessage
    ActivationNoSeat: VerificationComplete.PopupAlertMessage
    NotSignedIn: VerificationComplete.PopupAlertMessage
    SignedInNoSubscription: VerificationComplete.PopupAlertMessage
    class BannerMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NoBanner: _ClassVar[VerificationComplete.BannerMessage]
        ActivateProPresenter: _ClassVar[VerificationComplete.BannerMessage]
    NoBanner: VerificationComplete.BannerMessage
    ActivateProPresenter: VerificationComplete.BannerMessage
    RESULT_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    BIBLES_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    BANNER_FIELD_NUMBER: _ClassVar[int]
    result: VerificationComplete.Status
    license: LicenseInfo
    bibles: Bibles
    token: TokenMetadata
    subscription_info: SubscriptionInfo
    alert: VerificationComplete.PopupAlertMessage
    banner: VerificationComplete.BannerMessage
    def __init__(self, result: _Optional[_Union[VerificationComplete.Status, str]] = ..., license: _Optional[_Union[LicenseInfo, _Mapping]] = ..., bibles: _Optional[_Union[Bibles, _Mapping]] = ..., token: _Optional[_Union[TokenMetadata, _Mapping]] = ..., subscription_info: _Optional[_Union[SubscriptionInfo, _Mapping]] = ..., alert: _Optional[_Union[VerificationComplete.PopupAlertMessage, str]] = ..., banner: _Optional[_Union[VerificationComplete.BannerMessage, str]] = ...) -> None: ...

class Seats(_message.Message):
    __slots__ = ("basic", "advanced")
    BASIC_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    basic: int
    advanced: int
    def __init__(self, basic: _Optional[int] = ..., advanced: _Optional[int] = ...) -> None: ...

class SupplementalInformation(_message.Message):
    __slots__ = ("download_link",)
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    download_link: str
    def __init__(self, download_link: _Optional[str] = ...) -> None: ...

class Bible(_message.Message):
    __slots__ = ("id", "name", "language", "publisher", "copyright", "display_abbreviation", "internal_abbreviation", "version", "info")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    COPYRIGHT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ABBREVIATION_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_ABBREVIATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    language: str
    publisher: str
    copyright: str
    display_abbreviation: str
    internal_abbreviation: str
    version: str
    info: SupplementalInformation
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., language: _Optional[str] = ..., publisher: _Optional[str] = ..., copyright: _Optional[str] = ..., display_abbreviation: _Optional[str] = ..., internal_abbreviation: _Optional[str] = ..., version: _Optional[str] = ..., info: _Optional[_Union[SupplementalInformation, _Mapping]] = ...) -> None: ...

class PurchasedBible(_message.Message):
    __slots__ = ("metadata", "licensing_info")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LICENSING_INFO_FIELD_NUMBER: _ClassVar[int]
    metadata: Bible
    licensing_info: LicensingInfo
    def __init__(self, metadata: _Optional[_Union[Bible, _Mapping]] = ..., licensing_info: _Optional[_Union[LicensingInfo, _Mapping]] = ...) -> None: ...

class LicensingInfo(_message.Message):
    __slots__ = ("available_copies", "total_copies", "is_active_locally", "other_active_copies")
    AVAILABLE_COPIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COPIES_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_LOCALLY_FIELD_NUMBER: _ClassVar[int]
    OTHER_ACTIVE_COPIES_FIELD_NUMBER: _ClassVar[int]
    available_copies: int
    total_copies: int
    is_active_locally: bool
    other_active_copies: _containers.RepeatedCompositeFieldContainer[ActiveCopy]
    def __init__(self, available_copies: _Optional[int] = ..., total_copies: _Optional[int] = ..., is_active_locally: bool = ..., other_active_copies: _Optional[_Iterable[_Union[ActiveCopy, _Mapping]]] = ...) -> None: ...

class ActiveCopy(_message.Message):
    __slots__ = ("display_name", "hostname")
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    hostname: str
    def __init__(self, display_name: _Optional[str] = ..., hostname: _Optional[str] = ...) -> None: ...

class RegistrationInfo(_message.Message):
    __slots__ = ("user_name", "display_key", "display_name", "expiration_date", "activation_key", "license_type", "registration_date", "seat_type", "latest_available_build_number", "latest_available_version", "has_worship_house_media_subscription", "maintenance_expiration_date", "non_extended_maintenance_expiration_date", "is_auto_renewal_active")
    class LicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Trial: _ClassVar[RegistrationInfo.LicenseType]
        Rental: _ClassVar[RegistrationInfo.LicenseType]
        Standard: _ClassVar[RegistrationInfo.LicenseType]
        Campus: _ClassVar[RegistrationInfo.LicenseType]
    Trial: RegistrationInfo.LicenseType
    Rental: RegistrationInfo.LicenseType
    Standard: RegistrationInfo.LicenseType
    Campus: RegistrationInfo.LicenseType
    class SeatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Inactive: _ClassVar[RegistrationInfo.SeatType]
        Basic: _ClassVar[RegistrationInfo.SeatType]
        Advanced: _ClassVar[RegistrationInfo.SeatType]
    Inactive: RegistrationInfo.SeatType
    Basic: RegistrationInfo.SeatType
    Advanced: RegistrationInfo.SeatType
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_KEY_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_KEY_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    SEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LATEST_AVAILABLE_BUILD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LATEST_AVAILABLE_VERSION_FIELD_NUMBER: _ClassVar[int]
    HAS_WORSHIP_HOUSE_MEDIA_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    NON_EXTENDED_MAINTENANCE_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_RENEWAL_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    display_key: str
    display_name: str
    expiration_date: int
    activation_key: str
    license_type: RegistrationInfo.LicenseType
    registration_date: int
    seat_type: RegistrationInfo.SeatType
    latest_available_build_number: int
    latest_available_version: str
    has_worship_house_media_subscription: bool
    maintenance_expiration_date: int
    non_extended_maintenance_expiration_date: int
    is_auto_renewal_active: bool
    def __init__(self, user_name: _Optional[str] = ..., display_key: _Optional[str] = ..., display_name: _Optional[str] = ..., expiration_date: _Optional[int] = ..., activation_key: _Optional[str] = ..., license_type: _Optional[_Union[RegistrationInfo.LicenseType, str]] = ..., registration_date: _Optional[int] = ..., seat_type: _Optional[_Union[RegistrationInfo.SeatType, str]] = ..., latest_available_build_number: _Optional[int] = ..., latest_available_version: _Optional[str] = ..., has_worship_house_media_subscription: bool = ..., maintenance_expiration_date: _Optional[int] = ..., non_extended_maintenance_expiration_date: _Optional[int] = ..., is_auto_renewal_active: bool = ...) -> None: ...

class BuildInformation(_message.Message):
    __slots__ = ("build_number", "version", "min_os_version", "release_date", "registration_date", "download_size", "download_url", "channel", "is_beta", "is_available")
    BUILD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MIN_OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    IS_BETA_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    build_number: int
    version: str
    min_os_version: str
    release_date: int
    registration_date: int
    download_size: int
    download_url: str
    channel: str
    is_beta: bool
    is_available: bool
    def __init__(self, build_number: _Optional[int] = ..., version: _Optional[str] = ..., min_os_version: _Optional[str] = ..., release_date: _Optional[int] = ..., registration_date: _Optional[int] = ..., download_size: _Optional[int] = ..., download_url: _Optional[str] = ..., channel: _Optional[str] = ..., is_beta: bool = ..., is_available: bool = ...) -> None: ...

class Alert(_message.Message):
    __slots__ = ("alert_type", "title", "content_type", "content")
    class AlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Info: _ClassVar[Alert.AlertType]
        Feature: _ClassVar[Alert.AlertType]
        Warning: _ClassVar[Alert.AlertType]
    Info: Alert.AlertType
    Feature: Alert.AlertType
    Warning: Alert.AlertType
    class AlertContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ContentType: _ClassVar[Alert.AlertContentType]
        Text: _ClassVar[Alert.AlertContentType]
        InternalLink: _ClassVar[Alert.AlertContentType]
        ExternalLink: _ClassVar[Alert.AlertContentType]
    ContentType: Alert.AlertContentType
    Text: Alert.AlertContentType
    InternalLink: Alert.AlertContentType
    ExternalLink: Alert.AlertContentType
    ALERT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    alert_type: Alert.AlertType
    title: str
    content_type: Alert.AlertContentType
    content: str
    def __init__(self, alert_type: _Optional[_Union[Alert.AlertType, str]] = ..., title: _Optional[str] = ..., content_type: _Optional[_Union[Alert.AlertContentType, str]] = ..., content: _Optional[str] = ...) -> None: ...

class TokenMetadata(_message.Message):
    __slots__ = ("access_token", "refresh_token", "expires_at")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    expires_at: int
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., expires_at: _Optional[int] = ...) -> None: ...

class SubscriptionInfo(_message.Message):
    __slots__ = ("organization_name", "procontent_license_type", "procontent_license_expiration")
    class ProContentLicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Free: _ClassVar[SubscriptionInfo.ProContentLicenseType]
        Premium: _ClassVar[SubscriptionInfo.ProContentLicenseType]
    Free: SubscriptionInfo.ProContentLicenseType
    Premium: SubscriptionInfo.ProContentLicenseType
    ORGANIZATION_NAME_FIELD_NUMBER: _ClassVar[int]
    PROCONTENT_LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROCONTENT_LICENSE_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    organization_name: str
    procontent_license_type: SubscriptionInfo.ProContentLicenseType
    procontent_license_expiration: int
    def __init__(self, organization_name: _Optional[str] = ..., procontent_license_type: _Optional[_Union[SubscriptionInfo.ProContentLicenseType, str]] = ..., procontent_license_expiration: _Optional[int] = ...) -> None: ...

class DownloadLink(_message.Message):
    __slots__ = ("id", "url")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class Bibles(_message.Message):
    __slots__ = ("free_bibles", "purchased_bibles")
    FREE_BIBLES_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_BIBLES_FIELD_NUMBER: _ClassVar[int]
    free_bibles: _containers.RepeatedCompositeFieldContainer[Bible]
    purchased_bibles: _containers.RepeatedCompositeFieldContainer[PurchasedBible]
    def __init__(self, free_bibles: _Optional[_Iterable[_Union[Bible, _Mapping]]] = ..., purchased_bibles: _Optional[_Iterable[_Union[PurchasedBible, _Mapping]]] = ...) -> None: ...

class FeatureFlags(_message.Message):
    __slots__ = ("use_staging", "use_subscription")
    USE_STAGING_FIELD_NUMBER: _ClassVar[int]
    USE_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    use_staging: bool
    use_subscription: bool
    def __init__(self, use_staging: bool = ..., use_subscription: bool = ...) -> None: ...
