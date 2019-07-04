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
	return columns, data

def get_data(filters):
	query_data = frappe.db.sql("""
		select  
			title,name,creation 
		from 
			`tabQuotation`
		where {0}	
			""".format(validate_filters(filters)),debug=1)

	return query_data	

def validate_filters(filters):
	conditions = '1 = 1' 
	if filters.get("from_date"): 
		conditions += " and creation >= '{}'".format(filters.get("from_date"))
	if filters.get("to_date"): 
		conditions += " and creation <= '{}'".format(filters.get("to_date"))

	if filters.get('customer_name'):
		conditions += " and customer_name = '{0}'".format(filters.get('customer_name'))
	print("///////////////",conditions)
	return conditions	

def get_columns():
	
	return [
		{
			"fieldname": "title",
			"label": _("Customer Name"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 110
		},
		{
			"fieldname": "name",
			"label": _("Qutation No"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
		{
			"fieldname": "creation",
			"label": _("Created Date"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
		{
			"fieldname": "",
			"label": _("Sales Order No"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
		{
			"fieldname": "",
			"label": _("Sales Invoice No"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
		{
			"fieldname": "",
			"label": _("Delivery Note"),
			"fieldtype": "Link",
			"options": "Qutation",
			"width": 150
		},
	]
