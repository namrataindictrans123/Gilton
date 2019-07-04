# Copyright (c) 2013, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data


def get_data(filters):
	query_data = frappe.db.sql("""
		select  
			full_name,creation,email,username
		from 
			`tabUser`
		where {0}	
			""".format(validate_filters(filters)),debug=1)

	return query_data

def validate_filters(filters):
	conditions = '1 = 1' 
	if filters.get("from_date"): 
		conditions += " and creation >= '{}'".format(filters.get("from_date"))
	if filters.get("to_date"): 
		conditions += " and creation <= '{}'".format(filters.get("to_date"))

	if filters.get('username'):
		conditions += " and username = '{0}'".format(filters.get('username'))
	print("///////////////",conditions)
	return conditions

def get_columns():
	
	return [
		
		{
			"fieldname": "full_name",
			"label": _("Full Name"),
			"fieldtype": "Link",
			"options": "User",
			"width": 150
		},
		{
			"fieldname": "creation",
			"label": _("Created Date"),
			"fieldtype": "Link",
			"options": "User",
			"width": 150
		},
		{
			"fieldname": "email",
			"label": _("Email"),
			"fieldtype": "Link",
			"options": "email",
			"width": 150
		},
		{
			"fieldname": "username",
			"label": _("User name"),
			"fieldtype": "Link",
			"options": "User",
			"width": 150
		},
		
	]
