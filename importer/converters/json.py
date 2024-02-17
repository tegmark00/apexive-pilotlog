from datetime import datetime

from importer import models
from importer.converters.base import Converter


class JsonAircraftConverter(Converter):

    def convert(self, data: dict) -> models.AirCraftDTO:
        return models.AirCraftDTO(
            fin=data["Fin"],
            sea=data["Sea"],
            tmg=data["TMG"],
            efis=data["Efis"],

            # aircraft
            eng_group=data.get("EngGroup"),
            eng_type=data.get("EngType"),

            fnpt=data["FNPT"],
            make=data["Make"],
            run2=data["Run2"],
            aircraft_class=data["Class"],
            model=data["Model"],
            power=data["Power"],
            seats=data["Seats"],
            active=data["Active"],
            kg5700=data["Kg5700"],
            rating=data["Rating"],
            company=data["Company"],
            complex=data["Complex"],
            cond_log=data["CondLog"],
            fav_list=data["FavList"],
            category=data["Category"],
            high_perf=data["HighPerf"],
            sub_model=data["SubModel"],
            aerobatic=data["Aerobatic"],
            ref_search=data["RefSearch"],
            reference=data["Reference"],
            tail_wheel=data["Tailwheel"],
            default_app=data["DefaultApp"],
            default_log=data["DefaultLog"],
            default_ops=data["DefaultOps"],
            device_code=data["DeviceCode"],
            aircraft_code=data["AircraftCode"],
            default_launch=data["DefaultLaunch"],
            record_modified=data["Record_Modified"]
        )


class JsonAirFieldConverter(Converter):
    def convert(self, data: dict) -> models.AirFieldDTO:
        return models.AirFieldDTO(
            af_cat=data["AFCat"],
            af_code=data["AFCode"],
            afiata=data["AFIATA"],
            aficao=data["AFICAO"],
            af_name=data["AFName"],

            # airfield
            affaa=data.get("AFFAA"),
            user_edit=data.get("UserEdit"),
            city=data.get("City"),
            notes=data.get("Notes"),

            tz_code=data["TZCode"],
            latitude=data["Latitude"],
            show_list=data["ShowList"],
            af_country=data["AFCountry"],
            longitude=data["Longitude"],
            notes_user=data["NotesUser"],
            region_user=data["RegionUser"],
            elevation_ft=data["ElevationFT"],
            record_modified=data["Record_Modified"]
        )


class JsonFlightConverter(Converter):
    def convert(self, data: dict) -> models.FlightDTO:
        return models.FlightDTO(
            pf=data["PF"],
            pax=data["Pax"],
            fuel=data["Fuel"],
            de_ice=data["DeIce"],
            route=data["Route"],
            to_day=data["ToDay"],
            min_u1=data["minU1"],
            min_u2=data["minU2"],
            min_u3=data["minU3"],
            min_u4=data["minU4"],
            min_xc=data["minXC"],
            arr_rwy=data["ArrRwy"],
            dep_rwy=data["DepRwy"],
            ldg_day=data["LdgDay"],
            lift_sw=data["LiftSW"],
            p1_code=data["P1Code"],
            p2_code=data["P2Code"],
            p3_code=data["P3Code"],
            p4_code=data["P4Code"],
            report=data["Report"],
            tag_ops=data["TagOps"],
            to_edit=data["ToEdit"],
            min_air=data["minAIR"],
            min_cop=data["minCOP"],
            min_ifr=data["minIFR"],
            min_imt=data["minIMT"],
            min_pic=data["minPIC"],
            min_rel=data["minREL"],
            min_sfr=data["minSFR"],
            arr_code=data["ArrCode"],
            date_utc=data["DateUTC"],
            dep_code=data["DepCode"],
            hobbs_in=data["HobbsIn"],
            holding=data["Holding"],
            pairing=data["Pairing"],
            remarks=data["Remarks"],
            sign_box=data["SignBox"],
            to_night=data["ToNight"],
            user_num=data["UserNum"],
            min_dual=data["minDUAL"],
            min_exam=data["minEXAM"],
            crew_list=data["CrewList"],
            date_base=data["DateBASE"],
            fuel_used=data["FuelUsed"],
            hobbs_out=data["HobbsOut"],
            ldg_night=data["LdgNight"],
            next_page=data["NextPage"],
            tag_delay=data["TagDelay"],
            training=data["Training"],
            user_bool=data["UserBool"],
            user_text=data["UserText"],
            min_inst=data["minINSTR"],
            min_night=data["minNIGHT"],
            min_picus=data["minPICUS"],
            min_total=data["minTOTAL"],
            arr_offset=data["ArrOffset"],
            date_local=data.get("DateLocal"),
            dep_offset=data["DepOffset"],
            tag_launch=data["TagLaunch"],
            tag_lesson=data["TagLesson"],
            to_time_utc=data["ToTimeUTC"],
            arr_time_utc=data["ArrTimeUTC"],
            base_offset=data["BaseOffset"],

            # flight
            cargo=data.get("Cargo"),

            dep_time_utc=data["DepTimeUTC"],
            flight_code=data["FlightCode"],
            ldg_time_utc=data["LdgTimeUTC"],
            fuel_planned=data["FuelPlanned"],
            next_summary=data["NextSummary"],
            tag_approach=data["TagApproach"],
            aircraft_code=data.get("AircraftCode"),
            arr_time_sched=data["ArrTimeSCHED"],
            dep_time_sched=data["DepTimeSCHED"],
            flight_number=data["FlightNumber"],
            flight_search=data["FlightSearch"],
            record_modified=data["Record_Modified"]
        )


class JsonImagePicConverter(Converter):
    def convert(self, data: dict) -> models.ImagePicDTO:
        return models.ImagePicDTO(
            file_ext=data["FileExt"],
            img_code=data["ImgCode"],
            file_name=data["FileName"],
            link_code=data["LinkCode"],
            img_upload=data["Img_Upload"],
            img_download=data["Img_Download"],
            record_modified=data["Record_Modified"],
        )


class JsonLimitRulesConverter(Converter):
    def convert(self, data: dict) -> models.LimitRulesDTO:
        return models.LimitRulesDTO(
            l_to=data["LTo"],
            l_from=data["LFrom"],
            l_type=data["LType"],
            l_zone=data["LZone"],
            l_minutes=data["LMinutes"],
            limit_code=data["LimitCode"],
            l_period_code=data["LPeriodCode"],
            record_modified=data["Record_Modified"],
        )


class JsonMyQueryConverter(Converter):
    def convert(self, data: dict) -> models.MyQueryDTO:
        return models.MyQueryDTO(
            name=data["Name"],
            mq_code=data["mQCode"],
            quick_view=data["QuickView"],
            short_name=data["ShortName"],
            record_modified=data["Record_Modified"],
        )


class JsonMyQueryBuildConverter(Converter):
    def convert(self, data: dict) -> models.MyQueryBuildDTO:
        return models.MyQueryBuildDTO(
            build_1=data["Build1"],
            build_2=data["Build2"],
            build_3=data["Build3"],
            build_4=data["Build4"],
            mq_code=data["mQCode"],
            mqb_code=data["mQBCode"],
            record_modified=data["Record_Modified"],
        )


class JsonPilotConverter(Converter):
    def convert(self, data: dict) -> models.PilotDTO:
        return models.PilotDTO(
            notes=data["Notes"],
            active=data["Active"],
            company=data["Company"],
            fav_list=data["FavList"],
            user_api=data["UserAPI"],
            facebook=data["Facebook"],
            linkedin=data["LinkedIn"],
            pilot_ref=data["PilotRef"],
            pilot_code=data["PilotCode"],
            pilot_name=data["PilotName"],
            pilot_email=data["PilotEMail"],
            pilot_phone=data["PilotPhone"],
            certificate=data["Certificate"],
            phone_search=data["PhoneSearch"],
            pilot_search=data["PilotSearch"],
            roster_alias=data.get("RosterAlias"),
            record_modified=data["Record_Modified"],
        )


class JsonQualificationConverter(Converter):
    def convert(self, data: dict) -> models.QualificationDTO:
        return models.QualificationDTO(
            q_code=data["QCode"],
            ref_extra=data["RefExtra"],
            ref_model=data["RefModel"],
            validity=data["Validity"],
            date_valid=data["DateValid"] or None,
            q_type_code=data["QTypeCode"],
            date_issued=data["DateIssued"] or None,
            minimum_qty=data["MinimumQty"],
            notify_days=data["NotifyDays"],
            ref_air_field=data["RefAirfield"],
            minimum_period=data["MinimumPeriod"],
            notify_comment=data["NotifyComment"],
            record_modified=data["Record_Modified"],
        )


class JsonSettingConfigConverter(Converter):
    def convert(self, data: dict) -> models.SettingConfigDTO:
        return models.SettingConfigDTO(
            data=data["Data"],
            name=data["Name"],
            group=data["Group"],
            config_code=data["ConfigCode"],
            record_modified=data["Record_Modified"],
        )


class JsonLogEntryConverter(Converter):
    model_adapters = {
        "aircraft": JsonAircraftConverter,
        "airfield": JsonAirFieldConverter,
        "flight": JsonFlightConverter,
        "imagepic": JsonImagePicConverter,
        "limitrules": JsonLimitRulesConverter,
        "myquery": JsonMyQueryConverter,
        "myquerybuild": JsonMyQueryBuildConverter,
        "pilot": JsonPilotConverter,
        "qualification": JsonQualificationConverter,
        "settingconfig": JsonSettingConfigConverter,
    }

    def convert(self, data: dict) -> models.LogEntryDTO:
        table_name = data["table"].lower()
        model_adapter = self.model_adapters[table_name]()
        meta = model_adapter.convert(data["meta"])

        return models.LogEntryDTO(
            user_id=data["user_id"],
            guid=data["guid"],
            table_name=table_name,
            meta=meta,
            platform=data["platform"],
            modified=datetime.utcfromtimestamp(data["_modified"]),
        )
