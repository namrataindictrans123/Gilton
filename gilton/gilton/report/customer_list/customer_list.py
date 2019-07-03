# Copyright (c) 2013, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	# print("execute function")
	columns, data = get_columns(), get_data(filters)
	print("------------------------------------------")
	print(data)
	print("------------------------------------------")
	# validate_filters(filters)
	return columns, data

def get_data(filters):
	query_data = frappe.db.sql("""
		select  
			customer_name,email_address 
		from 
			`tabCustomer`
		where {0}	
			""".format(validate_filters(filters)),debug=1)

	return query_data

def validate_filters(filters):
	# if filters.creation > filters.modified:
	# 	frappe.throw((" 'creation' cannot not be greater than 'modified' "))
	cond = '1 = 1' 
	if filters.get('customer_name'):
		cond += " and customer_name = '{0}'".format(filters.get('customer_name'))
	return cond	

def get_columns():
	
	return [
		{
			"fieldname": "cust",
			"label": _("Cust Name"),
			"fieldtype": "Link",
			"options": "Customer",
			"width": 110
		},
		{
			"fieldname": "email_address",
			"label": _("Email Id"),
			"fieldtype": "Link",
			"options": "Customer",
			"width": 150
		},
		
	]
