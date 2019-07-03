from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def sendmail(doc,method=None):
    print('this is first semd mail api \n carryon')
    pass
