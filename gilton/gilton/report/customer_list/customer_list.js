// Copyright (c) 2016, Indictrans and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Customer List"] = {
	"filters": [
	   {
            "fieldname":"creation",
			"label":("From Date"),
			"fieldtype":"Date",
			 
        },
        {
			"fieldname":"modified",
			"label":("To Date"),
			"fieldtype":"Date",
			  
		},
		{
            "fieldname":"customer_name",
			"label":("Full Name"),
			"fieldtype":"Data",
			"options":"Customer",
			"default":frappe.defaults.get_user_default("Customer"),
			
        } 

	]
}
