frappe.ui.form.on('Customer', {
	onload: function(frm) {

		console.log("Hello world Thank you. Indictrans")

	},

	

	validate: function(frm){
		frm.set_value("user_name", frm.doc.email)
	},

	country: function(frm){
		if (frm.doc.country == "United Kingdom")
		{
			frappe.msgprint("validated")
			frm.set_value("default_currency", "GBP")
			frm.set_value("default_price_list", "Standard UK")
		}

		if (frm.doc.country == "United States")
		{
			frappe.msgprint("validated for US")
			frm.set_value("default_currency", "USD")
			frm.set_value("default_price_list", "Standard US")
		}

		if (frm.doc.country == "United Arab Emirates")
		{
			frappe.msgprint("validated for UAE")
			frm.set_value("default_currency", "ADE")
			frm.set_value("default_price_list", "Standard UAE")
		}

	}

});
