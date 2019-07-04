frappe.ui.form.on("Quotation", {
	party_name: function(frm) {    
		if(frm.doc.party_name) {
			frm.events.get_email(frm)
		}
	},

	get_email: function(frm) {
		frappe.call({
			method: "frappe.client.get_value",
			args: {
				doctype: "Customer",
				fieldname: ['email_address'],
				filters: {'name': frm.doc.party_name}
			},
			callback: function(r) {
				frm.set_value('email_address', r.message.email_address)
			}
		});
	}
});
