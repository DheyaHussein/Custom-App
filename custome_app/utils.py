import frappe
from num2words import num2words

@frappe.whitelist()
def convert_number_to_words(number, lang="en"):
    try:
        number = int(number)
        if lang == "ar":
            return num2words(number, lang="ar")
        return num2words(number, lang="en")
    except Exception as e:
        return str(e)
