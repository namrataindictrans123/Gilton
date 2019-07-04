


def send_email_with_attachment(doctype, docname, email_address):
	frappe.msgprint("Mail sent")
	attachments = [frappe.attach_print(doctype=doctype, name=docname, print_letterhead=True)]
	frappe.sendmail(recipients = recipients, cc = recipients, sender="", subject=docname, message="", delayed=False, attachments=attachments )