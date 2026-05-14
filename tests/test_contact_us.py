import pytest
from pages.contact_us import ContactUs


@pytest.mark.parametrize(
    "first_name,last_name,subject,message,expected",
    [
        ("John", "Doe", "Testing", "Hello world", "success"),
        ("", "Doe", "Testing", "Hello world", "first_name_error"),
        ("John", "", "Testing", "Hello world", "last_name_error"),
        ("John", "Doe", "", "Hello world", "subject_error"),
        ("John", "Doe", "Testing", "", "message_error"),
    ]
)
def test_contact_form(driver,
                      first_name,
                      last_name,
                      subject,
                      message,
                      expected):

    contact = ContactUs(driver)

    contact.load()

    contact.submit_contact_form(
        first_name,
        last_name,
        subject,
        message
    )

    if expected == "success":
        # assert success message
        pass

    else:
        errors = contact.get_validation_errors()
        assert len(errors) > 0



