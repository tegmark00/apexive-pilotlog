import dataclasses


@dataclasses.dataclass
class Type:
    name: str
    comment: str = ""


text = Type("Text")
boolean = Type("Boolean")
date = Type("Date")
datetime_ = Type("DateTime")
yyyy = Type("YYYY")
hhmm = Type("hhmm")
number = Type("Number")
decimal = Type("Decimal")
packed_detail_approach = Type("Packed Detail", "#;type;runway;airport;comments")
packed_detail_person = Type("Packed Detail", "name;role;email")
