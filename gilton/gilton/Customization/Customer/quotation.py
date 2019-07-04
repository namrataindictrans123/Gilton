from __future__ import unicode_literals
import frappe



def on_submit(doc,method=None):
	frappe.msgprint("mail sent")
	attachments=[frappe.attach_print(doc.doctype,doc.name, print_letterhead=True)]
	frappe.sendmail(
		recipients=[doc.email_address],
		subject="Regarding Quotation.....",
		message='Your Quotation is attached ,please find attachment',
		attachments=attachments
		)

