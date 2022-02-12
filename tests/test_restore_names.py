from app.restore_names import restore_names


def test_function_nothing_to_return():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    assert restore_names(users) is None


def test_is_function_set_correct_first_name():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)

    assert users[0]["first_name"] in users[0]["full_name"]
    assert users[1]["first_name"] in users[1]["full_name"]
