frappe.ui.form.on('Customer', {
	onload: function(frm) {

		console.log("Hello world Thank you. Indictrans")

	},

<<<<<<< HEAD

=======
	
>>>>>>> 3b28e2279f5a43fb39c29b70f41ea02dc74c597c

	validate: function(frm){
		frm.set_value("user_name", frm.doc.email)
	}

});
