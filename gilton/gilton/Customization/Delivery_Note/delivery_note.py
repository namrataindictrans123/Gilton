from __future__ import unicode_literals
import frappe
from datetime import date
def submit(doc,method=None):
    print("After submit in delivery Note Submission")
    frappe.msgprint("Hiii You are on right track")
    print(doc.items)
    print(doc.customer_name)
    New_SalesInvoice = frappe.new_doc("Sales Invoice")
    for item in doc.items:
        print(item.item_code)
        print(item.qty)
        print(item.uom)
        print(item.rate)
        print(item.amount)
        New_SalesInvoice.append()

    New_SalesInvoice.customer = doc.customer_name
    New_SalesInvoice.due_date = date.today()
    New_SalesInvoice.append()
