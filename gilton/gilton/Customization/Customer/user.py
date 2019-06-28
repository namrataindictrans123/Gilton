from __future__ import unicode_literals
import frappe


def create_user(doc,method=None):
<<<<<<< HEAD

=======
   
>>>>>>> 3b28e2279f5a43fb39c29b70f41ea02dc74c597c
   new_cus = frappe.new_doc("User")
   new_cus.email=doc.email
   new_cus.username=doc.email
   full_name = doc.customer_name
   full_name = full_name.split(' ')
<<<<<<< HEAD

=======
   
>>>>>>> 3b28e2279f5a43fb39c29b70f41ea02dc74c597c
   if(len(full_name)>1):
   	new_cus.first_name = full_name[0]
   	new_cus.last_name = full_name[1]
   else:
   	new_cus.first_name = full_name[0]
   new_cus.insert()
   frappe.db.commit()
<<<<<<< HEAD
=======


>>>>>>> 3b28e2279f5a43fb39c29b70f41ea02dc74c597c
