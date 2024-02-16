import datetime
import uuid
from typing import Literal, Optional

from django.utils.timezone import make_aware
from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo

T_TABLES = Literal[
    "aircraft",
    "airfield",
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
    record_modified: datetime.datetime


class AirCraftDTO(BaseDTO):
    fin: str
    sea: bool
    tmg: bool
    efis: bool
    fnpt: int
    make: str
    run2: bool
    aircraft_class: int
    model: str
    power: int
    seats: int
    active: bool
    kg5700: int
    rating: str
    company: str
    complex: bool
    cond_log: int
    fav_list: bool
    category: int
    high_perf: bool
    sub_model: str
    aerobatic: bool
    ref_search: str
    reference: str
    tail_wheel: bool
    default_app: int
    default_log: int
    default_ops: int
    device_code: int
    aircraft_code: uuid.UUID
    default_launch: int


class AirFieldDTO(BaseDTO):
    af_cat: int
    af_code: uuid.UUID
    afiata: str
    aficao: str
    af_name: str
    tz_code: int
    latitude: int
    show_list: bool
    af_country: int
    longitude: int
    notes_user: str
    region_user: int
    elevation_ft: int


class FlightDTO(BaseDTO):
    pf: bool
    pax: int
    fuel: int
    de_ice: bool
    route: str
    to_day: int
    min_u1: int
    min_u2: int
    min_u3: int
    min_u4: int
    min_xc: int
    arr_rwy: str
    dep_rwy: str
    ldg_day: int
    lift_sw: int
    p1_code: uuid.UUID
    p2_code: uuid.UUID
    p3_code: uuid.UUID
    p4_code: uuid.UUID
    report: str
    tag_ops: str
    to_edit: bool
    min_air: int
    min_ifr: int
    min_pic: int
    min_rel: int
    min_sfr: int
    arr_code: uuid.UUID
    date_utc: datetime.date
    dep_code: uuid.UUID
    hobbs_in: int
    holding: int
    pairing: str
    remarks: str
    sign_box: int
    to_night: int
    user_num: int
    min_dual: int
    min_exam: int
    crew_list: str
    date_base: datetime.date
    fuel_used: int
    hobbs_out: int
    ldg_night: int
    next_page: bool
    tag_delay: str
    training: str
    user_bool: bool
    user_text: str
    min_inst: int
    min_night: int
    min_picus: int
    min_total: int
    arr_offset: int
    date_local: Optional[datetime.date]
    dep_offset: int
    tag_launch: str
    tag_lesson: str
    to_time_utc: int
    arr_time_utc: int
    base_offset: int
    dep_time_utc: Optional[int]
    flight_code: uuid.UUID
    ldg_time_utc: int
    fuel_planned: int
    next_summary: bool
    tag_approach: str
    aircraft_code: Optional[uuid.UUID]
    arr_time_sched: int
    dep_time_sched: int
    flight_number: str
    flight_search: str


class ImagePicDTO(BaseDTO):
    file_ext: str
    img_code: uuid.UUID
    file_name: str
    link_code: uuid.UUID
    img_upload: bool
    img_download: bool


class LimitRulesDTO(BaseDTO):
    l_to: datetime.date
    l_from: datetime.date
    l_type: int
    l_zone: int
    l_minutes: int
    limit_code: uuid.UUID
    l_period_code: int


class MyQueryDTO(BaseDTO):
    name: str
    mq_code: uuid.UUID
    quick_view: bool
    short_name: str


class MyQueryBuildDTO(BaseDTO):
    build_1: str
    build_2: int
    build_3: int
    build_4: str
    mq_code: uuid.UUID
    mqb_code: uuid.UUID


class PilotDTO(BaseDTO):
    notes: str
    active: bool
    company: str
    fav_list: bool
    user_api: str
    facebook: str
    linkedin: str
    pilot_ref: str
    pilot_code: uuid.UUID
    pilot_name: str
    pilot_email: str
    pilot_phone: str
    certificate: str
    phone_search: str
    pilot_search: str
    roster_alias: Optional[str]


class QualificationDTO(BaseDTO):
    q_code: uuid.UUID
    ref_extra: int
    ref_model: str
    validity: int
    date_valid: Optional[datetime.date]
    q_type_code: int
    date_issued: Optional[datetime.date]
    minimum_qty: int
    notify_days: int
    ref_air_field: uuid.UUID
    minimum_period: int
    notify_comment: str


class SettingConfigDTO(BaseDTO):
    data: str
    name: str
    group: str
    config_code: int


class LogEntryDTO(BaseModel):
    user_id: int
    guid: str
    table_name: T_TABLES
    meta: BaseDTO
    platform: int
    modified: datetime.datetime

    @field_validator("modified")
    def validate_modified(cls, v: datetime.datetime, info: ValidationInfo) -> datetime.datetime:
        if v.tzinfo is None:
            return make_aware(v)
        return v
