frappe.ui.form.on('Customer', {
	onload: function(frm) {
		frm.set_value("country", "")
		console.log("Hello world Thank you. Indictrans")

	},

	validate: function(frm){
		frm.set_value("user_name", frm.doc.email_address)
	},
 
	
	country: function(frm){
			frappe.call({
			    method: 'gilton.gilton.Customization.Customer.user.country_dep_currency',
			    args: {
			        'doctype': 'Item',
			        'filters': {'country': frm.doc.country},
			        'fieldname': [
			            'default_currency',
			            'default_price_list',
			        ]
			    },
			    callback: function(r) {
			        if (!r.exc) {
			            // code snippet
			        }
			    }
			});

	}


});
 