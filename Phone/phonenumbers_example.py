import phonenumbers

class PhoneUtils:

    def add_plus_if_not_exists(phone_number: str) -> str:
        if not phone_number.startswith('+'):
            phone_number = '+' + phone_number
        return phone_number

    def extract_country_calling_code_and_national_number(phone_number: str) -> tuple:
        phone_number = PhoneUtils.add_plus_if_not_exists(phone_number)
        phonenumber = phonenumbers.parse(number=phone_number)
        return str(phonenumber.country_code), str(phonenumber.national_number)

    def extract_country_calling_code(phone_number: str) -> str:
        return PhoneUtils.extract_country_calling_code_and_national_number(phone_number)[0]

    def is_valid_phone_number(phone_number: str) -> bool:
        if not phone_number:
            return

        try:
            phone_number = PhoneUtils.add_plus_if_not_exists(phone_number)
            is_valid = phonenumbers.is_valid_number(phonenumbers.parse(phone_number))
            if not is_valid:
                print(f"Invalid Phone Number: {phone_number}.")
            return is_valid
        except Exception as ex:
            print(f"Invalid Phone Number: {phone_number}. Error: {str(ex)}")
            return False

    def format_e164_phone_number(phone_number: str) -> str:
        phone_number = PhoneUtils.add_plus_if_not_exists(phone_number)
        phonenumber = phonenumbers.parse(number=phone_number)
        phone_number_e164 = phonenumbers.format_number(phonenumber, phonenumbers.PhoneNumberFormat.E164)
        return phone_number_e164

    def validate_doctype_phone_number(doctype_name: str, country_phone_code: str, phone_number: str):
        if not (country_phone_code and phone_number):
            return

        if not PhoneUtils.is_valid_phone_number(country_phone_code + phone_number):
            print(f"Invalid {doctype_name} Phone Number: {country_phone_code + phone_number}")

    def get_country_calling_code_by_region_code(region_code: str):
        if not region_code:
            return
        region_code = region_code.upper()
        return phonenumbers.phonenumberutil.country_code_for_region(region_code)
    

number = PhoneUtils.format_e164_phone_number("521559 fdf 2252692")
print(f"Number: {number}")