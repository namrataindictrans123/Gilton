from __future__ import unicode_literals
import frappe
from datetime import date
def submit(doc,method=None):
    New_SalesInvoice = frappe.new_doc("Sales Invoice")
    New_SalesInvoice.customer = doc.customer_name
    New_SalesInvoice.due_date = date.today()
    New_SalesInvoice.company = "Gilton"
    for row in doc.items:
        New_SalesInvoice.append("items",
        {
            "item_code":row.item_code,
            "qty":row.qty,
            "uom":row.uom,
            "rate":row.rate,
            "amount":row.amount
        })
    #New_SalesInvoice.save(ignore_permissions=True)
    New_SalesInvoice.insert()
    frappe.db.commit()

def on_submit(doc,method=None):
    print("--------------------------------------")
    customer=frappe.get_doc("Customer",doc.customer_name)
    print(customer.email_address)
    frappe.sendmail(
		recipients=[customer.email_address],
		subject="Regarding Delivery Note and Sales Invoice.....",
		message="Dear Customer ,\n 1 <br>2 Your Item is ready to delivered with delivery Note no. {{  }} and Sales Invoice No {{ }}. \n Thank you. Visit our website again."
		)
