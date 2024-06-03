// Copyright (c) 2024, Shivansh Srivastava and contributors
// For license information, please see license.txt

// frappe.ui.form.on("listcache", {
// 	refresh(frm) {

// 	},
// });
frappe.call({
    method: "my_app.my_app.doctype.listcache.listcache.set_cached_items",
    callback: function(response) {
        console.log(response.message);
    }
});

frappe.call({
    method: 'my_app.my_app.doctype.listcache.listcache.get_cached_items',
    callback: function(response) {
        console.log(response.message);
    }
});

