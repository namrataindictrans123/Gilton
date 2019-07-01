def send_email_with_attachment(doctype, docname, recipients):
     attachments = [frappe.attach_print(doctype=doctype, name=docname, print_letterhead=True)]
     if attachments and recipients:
         frappe.sendmail(recipients = recipients, cc = recipients, sender="", subject=docname, message="", delayed=False, attachments=attachments )
