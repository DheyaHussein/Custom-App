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

# def validate_material_issue(doc, method):
#     """
#     Prevents issuing certain items unless the same quantity exists in 'Damaged Items Warehouse'.
#     This applies only to items where 'Requires Damaged Receipt' is checked.
#     """

#     damaged_warehouse = "Damaged Items Warehouse - اا"  # Change this to your actual warehouse name

#     for item in doc.items:
#         # Check if the item requires a damaged receipt before issue
#         requires_damaged = frappe.db.get_value("Item", item.item_code, "requires_damaged_receipt")

#         if doc.stock_entry_type == "Material Issue" and requires_damaged:
#             required_qty = item.qty

#             # Check available quantity in Damaged Warehouse
#             damaged_qty = frappe.db.get_value(
#                 "Bin",
#                 {"item_code": item.item_code, "warehouse": damaged_warehouse},
#                 "actual_qty"
#             ) or 0

#             # If required quantity is not available, prevent the Material Issue
#             if required_qty > damaged_qty:
#                 msg = _(f"""
#                 <b>Cannot issue item <b>{item.item_code}</b></b> because only <b>{damaged_qty}</b> exists in the <b>{damaged_warehouse}</b>.
#                 <br><br>
#                 <b>Solution:</b> You must first receive <b>{required_qty - damaged_qty}</b> as 'Damaged Material' before issuing.
#                 <br><br>
#                 <a href='/app/stock-entry/new' target='_blank'>
#                     <button class='btn btn-primary'>Create Stock Entry for Damaged Items</button>
#                 </a>
#                 """)

#                 frappe.throw(msg)