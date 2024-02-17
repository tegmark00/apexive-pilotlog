from django.db.models import Q, Exists, OuterRef

from pilotlog.models import Flight, AirField


def associate_flights_and_airfields():
    flights_to_update = Flight.objects.filter(
        Q(arr__isnull=True) &
        Exists(
            AirField.objects.filter(
                pk=OuterRef('arr_code')
            )
        )
    )

    flights_to_update.update(
        arr=OuterRef('arr_code')
    )

    flights_to_update = Flight.objects.filter(
        Q(dep__isnull=True) &
        Exists(
            AirField.objects.filter(
                pk=OuterRef('dep_code')
            )
        )
    )

    flights_to_update.update(
        dep=OuterRef('dep_code')
    )
