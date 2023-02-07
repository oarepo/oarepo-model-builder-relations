from invenio_access.permissions import system_identity


def test_relation_defaults(app, db, search_clear):
    from referred.proxies import current_service as referred_service
    from referrer.proxies import current_service as referrer_service

    referred_record = referred_service.create(
        system_identity,
        {
            "metadata": {
                "title": "Referred Record",
                "description": "First referred record",
                "hint": "Just a random string",
                "price": 1,
            }
        },
    )

    referrer_record = referrer_service.create(
        system_identity, {"metadata": {"ref": {"id": referred_record.id}}}
    )
    assert referrer_record.data["metadata"]["ref"]["id"] == referred_record.id
    assert (
        referrer_record.data["metadata"]["ref"]["metadata"]["title"]
        == referred_record.data["metadata"]["title"]
    )
