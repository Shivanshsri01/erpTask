import frappe
from frappe.model.document import Document
from frappe.utils.password import encrypt, decrypt

class aadhar(Document):
    def before_save(self):
        if not self.get("__encrypted"):
            self.aadhar_card = encrypt(self.aadhar_card)

    
 