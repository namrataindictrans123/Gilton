// Copyright (c) 2016, Indictrans and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales User"] = {
	"filters": [
		{
            "fieldname":"from_date",
			"label":("From Date"),
			"fieldtype":"Date",
			 
        },
        {
			"fieldname":"to_date",
			"label":("To Date"),
			"fieldtype": "Date",
		},
	]
}
