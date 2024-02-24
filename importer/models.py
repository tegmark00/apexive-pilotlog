import datetime
import uuid
from typing import Literal, Optional

from django.utils.timezone import make_aware
from pydantic import BaseModel, Field, field_validator
from pydantic_core.core_schema import ValidationInfo


T_TABLES = Literal[
    "Aircraft",
    "aircraft",
    "AirField",
    "airfield",
    "Flight",
    "flight",
    "imagepic",
    "limitrules",
    "myquery",
    "myquerybuild",
    "pilot",
    "qualification",
    "settingconfig",
]


class BaseDTO(BaseModel):
    record_modified: datetime.datetime = Field(..., alias="Record_Modified")


class AirCraftDTO(BaseDTO):
    fin: str = Field(..., alias="Fin")
    sea: bool = Field(..., alias="Sea")
    tmg: bool = Field(..., alias="TMG")
    efis: bool = Field(..., alias="Efis")

    # aircraft
    eng_group: Optional[int] = Field(None, alias="EngGroup")
    eng_type: Optional[int] = Field(None, alias="EngType")

    fnpt: int = Field(..., alias="FNPT")
    make: str = Field(..., alias="Make")
    run2: bool = Field(..., alias="Run2")
    aircraft_class: int = Field(..., alias="Class")
    model: str = Field(..., alias="Model")
    power: int = Field(..., alias="Power")
    seats: int = Field(..., alias="Seats")
    active: bool = Field(..., alias="Active")
    kg5700: int = Field(..., alias="Kg5700")
    rating: str = Field(..., alias="Rating")
    company: str = Field(..., alias="Company")
    complex: bool = Field(..., alias="Complex")
    cond_log: int = Field(..., alias="CondLog")
    fav_list: bool = Field(..., alias="FavList")
    category: int = Field(..., alias="Category")
    high_perf: bool = Field(..., alias="HighPerf")
    sub_model: str = Field(..., alias="SubModel")
    aerobatic: bool = Field(..., alias="Aerobatic")
    ref_search: str = Field(..., alias="RefSearch")
    reference: str = Field(..., alias="Reference")
    tail_wheel: bool = Field(..., alias="Tailwheel")
    default_app: int = Field(..., alias="DefaultApp")
    default_log: int = Field(..., alias="DefaultLog")
    default_ops: int = Field(..., alias="DefaultOps")
    device_code: int = Field(..., alias="DeviceCode")
    aircraft_code: uuid.UUID = Field(..., alias="AircraftCode")
    default_launch: int = Field(..., alias="DefaultLaunch")


class AirFieldDTO(BaseDTO):
    af_cat: int = Field(..., alias="AFCat")
    af_code: uuid.UUID = Field(..., alias="AFCode")
    afiata: str = Field(..., alias="AFIATA")
    aficao: str = Field(..., alias="AFICAO")
    af_name: str = Field(..., alias="AFName")

    # airfield
    city: Optional[str] = Field(None, alias="City")
    user_edit: Optional[bool] = Field(None, alias="UserEdit")
    notes: Optional[str] = Field(None, alias="Notes")
    affaa: Optional[str] = Field(None, alias="AFFAA")

    tz_code: int = Field(..., alias="TZCode")
    latitude: int = Field(..., alias="Latitude")
    show_list: bool = Field(..., alias="ShowList")
    af_country: int = Field(..., alias="AFCountry")
    longitude: int = Field(..., alias="Longitude")
    notes_user: str = Field(..., alias="NotesUser")
    region_user: int = Field(..., alias="RegionUser")
    elevation_ft: int = Field(..., alias="ElevationFT")


class FlightDTO(BaseDTO):
    pf: bool = Field(..., alias="PF")
    pax: int = Field(..., alias="Pax")
    fuel: int = Field(..., alias="Fuel")
    de_ice: bool = Field(..., alias="DeIce")
    route: str = Field(..., alias="Route")
    to_day: int = Field(..., alias="ToDay")
    min_u1: int = Field(..., alias="minU1")
    min_u2: int = Field(..., alias="minU2")
    min_u3: int = Field(..., alias="minU3")
    min_u4: int = Field(..., alias="minU4")
    min_xc: int = Field(..., alias="minXC")
    arr_rwy: str = Field(..., alias="ArrRwy")
    dep_rwy: str = Field(..., alias="DepRwy")
    ldg_day: int = Field(..., alias="LdgDay")
    lift_sw: int = Field(..., alias="LiftSW")
    p1_code: Optional[uuid.UUID] = Field(None, alias="P1Code")
    p2_code: Optional[uuid.UUID] = Field(None, alias="P2Code")
    p3_code: Optional[uuid.UUID] = Field(None, alias="P3Code")
    p4_code: Optional[uuid.UUID] = Field(None, alias="P4Code")
    report: str = Field(..., alias="Report")
    tag_ops: str = Field(..., alias="TagOps")
    to_edit: bool = Field(..., alias="ToEdit")
    min_air: int = Field(..., alias="minAIR")
    min_ifr: int = Field(..., alias="minIFR")
    min_pic: int = Field(..., alias="minPIC")
    min_rel: int = Field(..., alias="minREL")
    min_sfr: int = Field(..., alias="minSFR")
    arr_code: uuid.UUID = Field(..., alias="ArrCode")
    date_utc: datetime.date = Field(..., alias="DateUTC")
    dep_code: uuid.UUID = Field(..., alias="DepCode")
    hobbs_in: int = Field(..., alias="HobbsIn")
    holding: int = Field(..., alias="Holding")
    pairing: str = Field(..., alias="Pairing")
    remarks: str = Field(..., alias="Remarks")
    sign_box: int = Field(..., alias="SignBox")
    to_night: int = Field(..., alias="ToNight")
    user_num: int = Field(..., alias="UserNum")
    min_dual: int = Field(..., alias="minDUAL")
    min_exam: int = Field(..., alias="minEXAM")
    crew_list: str = Field(..., alias="CrewList")
    date_base: datetime.date = Field(..., alias="DateBASE")
    fuel_used: int = Field(..., alias="FuelUsed")
    hobbs_out: int = Field(..., alias="HobbsOut")
    ldg_night: int = Field(..., alias="LdgNight")
    next_page: bool = Field(..., alias="NextPage")
    tag_delay: str = Field(..., alias="TagDelay")
    training: str = Field(..., alias="Training")
    user_bool: bool = Field(..., alias="UserBool")
    user_text: str = Field(..., alias="UserText")
    min_inst: int = Field(..., alias="minINSTR")
    min_night: int = Field(..., alias="minNIGHT")
    min_picus: int = Field(..., alias="minPICUS")
    min_total: int = Field(..., alias="minTOTAL")
    arr_offset: int = Field(..., alias="ArrOffset")
    date_local: Optional[datetime.date] = Field(None, alias="DateLocal")
    dep_offset: int = Field(..., alias="DepOffset")
    tag_launch: str = Field(..., alias="TagLaunch")
    tag_lesson: str = Field(..., alias="TagLesson")
    to_time_utc: int = Field(..., alias="ToTimeUTC")

    arr_time_utc: Optional[datetime.time] = Field(None, alias="ArrTimeUTC")
    dep_time_utc: Optional[datetime.time] = Field(None, alias="DepTimeUTC")

    base_offset: int = Field(..., alias="BaseOffset")

    # flight
    cargo: Optional[int] = Field(None, alias="Cargo")
    flight_code: uuid.UUID = Field(..., alias="FlightCode")
    ldg_time_utc: int = Field(..., alias="LdgTimeUTC")
    fuel_planned: int = Field(..., alias="FuelPlanned")
    next_summary: bool = Field(..., alias="NextSummary")
    tag_approach: str = Field(..., alias="TagApproach")
    aircraft_code: Optional[uuid.UUID] = Field(None, alias="AircraftCode")
    arr_time_sched: int = Field(..., alias="ArrTimeSCHED")
    dep_time_sched: int = Field(..., alias="DepTimeSCHED")
    flight_number: str = Field(..., alias="FlightNumber")
    flight_search: str = Field(..., alias="FlightSearch")

    @field_validator("p1_code", "p2_code", "p3_code", "p4_code")
    def validate_pilot_codes(
        cls, v: Optional[uuid.UUID], info: ValidationInfo
    ) -> Optional[uuid.UUID]:
        if v == uuid.UUID(int=0):
            return None
        return v

    @field_validator("arr_time_utc", "dep_time_utc", mode="before")
    def validate_time_utc(
        cls, v: Optional[int], info: ValidationInfo
    ) -> Optional[datetime.time]:
        if v:
            h = v // 60
            m = v % 60
            return datetime.time(h, m)
        return None


class ImagePicDTO(BaseDTO):
    file_ext: str = Field(..., alias="FileExt")
    img_code: uuid.UUID = Field(..., alias="ImgCode")
    file_name: str = Field(..., alias="FileName")
    link_code: uuid.UUID = Field(..., alias="LinkCode")
    img_upload: bool = Field(..., alias="Img_Upload")
    img_download: bool = Field(..., alias="Img_Download")


class LimitRulesDTO(BaseDTO):
    l_to: datetime.date = Field(..., alias="LTo")
    l_from: datetime.date = Field(..., alias="LFrom")
    l_type: int = Field(..., alias="LType")
    l_zone: int = Field(..., alias="LZone")
    l_minutes: int = Field(..., alias="LMinutes")
    limit_code: uuid.UUID = Field(..., alias="LimitCode")
    l_period_code: int = Field(..., alias="LPeriodCode")


class MyQueryDTO(BaseDTO):
    name: str = Field(..., alias="Name")
    mq_code: uuid.UUID = Field(..., alias="mQCode")
    quick_view: bool = Field(..., alias="QuickView")
    short_name: str = Field(..., alias="ShortName")


class MyQueryBuildDTO(BaseDTO):
    build_1: str = Field(..., alias="Build1")
    build_2: int = Field(..., alias="Build2")
    build_3: int = Field(..., alias="Build3")
    build_4: str = Field(..., alias="Build4")
    mq_code: uuid.UUID = Field(..., alias="mQCode")
    mqb_code: uuid.UUID = Field(..., alias="mQBCode")


class PilotDTO(BaseDTO):
    notes: str = Field(..., alias="Notes")
    active: bool = Field(..., alias="Active")
    company: str = Field(..., alias="Company")
    fav_list: bool = Field(..., alias="FavList")
    user_api: str = Field(..., alias="UserAPI")
    facebook: str = Field(..., alias="Facebook")
    linkedin: str = Field(..., alias="LinkedIn")
    pilot_ref: str = Field(..., alias="PilotRef")
    pilot_code: uuid.UUID = Field(..., alias="PilotCode")
    pilot_name: str = Field(..., alias="PilotName")
    pilot_email: str = Field(..., alias="PilotEMail")
    pilot_phone: str = Field(..., alias="PilotPhone")
    certificate: str = Field(..., alias="Certificate")
    phone_search: str = Field(..., alias="PhoneSearch")
    pilot_search: str = Field(..., alias="PilotSearch")
    roster_alias: Optional[str] = Field(None, alias="RosterAlias")


class QualificationDTO(BaseDTO):
    q_code: uuid.UUID = Field(..., alias="QCode")
    ref_extra: int = Field(..., alias="RefExtra")
    ref_model: str = Field(..., alias="RefModel")
    validity: int = Field(..., alias="Validity")
    date_valid: Optional[datetime.date] = Field(None, alias="DateValid")
    q_type_code: int = Field(..., alias="QTypeCode")
    date_issued: Optional[datetime.date] = Field(None, alias="DateIssued")
    minimum_qty: int = Field(..., alias="MinimumQty")
    notify_days: int = Field(..., alias="NotifyDays")
    ref_air_field: uuid.UUID = Field(..., alias="RefAirfield")
    minimum_period: int = Field(..., alias="MinimumPeriod")
    notify_comment: str = Field(..., alias="NotifyComment")

    @field_validator("date_valid", "date_issued", mode="before")
    def validate_dates(
        cls, v: Optional[datetime.date], info: ValidationInfo
    ) -> Optional[datetime.date]:
        return v or None


class SettingConfigDTO(BaseDTO):
    data: str = Field(..., alias="Data")
    name: str = Field(..., alias="Name")
    group: str = Field(..., alias="Group")
    config_code: int = Field(..., alias="ConfigCode")


class LogEntryDTO(BaseModel):
    user_id: int = Field(..., alias="user_id")
    guid: str = Field(..., alias="guid")
    table_name: T_TABLES = Field(..., alias="table")
    meta: BaseDTO = Field(..., alias="meta")
    platform: int = Field(..., alias="platform")
    modified: datetime.datetime = Field(..., alias="_modified")

    @field_validator("modified")
    def validate_modified(
        cls, v: datetime.datetime, info: ValidationInfo
    ) -> datetime.datetime:
        if v.tzinfo is None:
            return make_aware(v)
        return v

    @field_validator("table_name", mode="before")
    def validate_table_name(cls, v, info: ValidationInfo) -> T_TABLES:
        return v.lower()
