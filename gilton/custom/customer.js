frappe.ui.form.on('Customer', {
	onload: function(frm) {

		console.log("Hello world Thank you. Indictrans")

	},

	validate: function(frm){
		frm.set_value("user_name", frm.doc.email)
	}

});
