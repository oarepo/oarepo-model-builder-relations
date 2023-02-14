from invenio_access.permissions import system_identity
from referred.proxies import current_service as referred_service
from referrer.proxies import current_service as referrer_service
import pytest


@pytest.fixture
def referred_record(app, db, search_clear):
    return referred_service.create(
        system_identity,
        {
            "metadata": {
                "title": "Referred Record",
                "description": "First referred record",
                "hint": "Just a random string",
                "price": 1,
            },
            "test": "cf",
        },
    )


@pytest.fixture
def referred_records(app, db, search_clear):
    return [
        referred_service.create(
            system_identity,
            {
                "metadata": {
                    "title": f"Referred Record # {idx}",
                    "description": f"Referred record # {idx} description",
                    "hint": f"Just a random string",
                    "price": idx,
                },
                "test": f"cf # {idx}",
            },
        )
        for idx in range(1, 11)
    ]


def test_internal_relation(app, db, search_clear):
    referrer_record = referrer_service.create(
        system_identity,
        {"metadata": {"obj": {"id": "1", "test": "blah"}, "internal-ref": {"id": "1"}}},
    )
    assert (
        referrer_record.data["metadata"]["internal-ref"]["id"]
        == referrer_record.data["metadata"]["obj"]["id"]
    )
    assert (
        referrer_record.data["metadata"]["internal-ref"]["test"]
        == referrer_record.data["metadata"]["obj"]["test"]
    )
