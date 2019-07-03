frappe.ui.form.on('Customer', {
	onload: function(frm) {

		console.log("Hello world Thank you. Indictrans")

	},

	validate: function(frm){
		frm.set_value("user_name", frm.doc.email_address)
	},

	country: function(frm){
		if (frm.doc.country == "United Kingdom")
		{
			frm.set_value("default_currency", "GBP")
			frm.set_value("default_price_list", "Standard UK")
		}

		if (frm.doc.country == "United States")
		{
			frm.set_value("default_currency", "USD")
			frm.set_value("default_price_list", "Standard US")
		}

		if (frm.doc.country == "United Arab Emirates")
		{
			frm.set_value("default_currency", "ADE")
			frm.set_value("default_price_list", "Standard UAE")
		}

	}

});
