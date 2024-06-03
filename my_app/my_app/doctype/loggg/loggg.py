import frappe
from frappe.model.document import Document

class loggg(Document):
    def error(self):
        try:
            x = 1/0 
            return x
        except ZeroDivisionError as e:
            frappe.log_error(frappe.get_traceback(), 'Error')
            return None
        except Exception as e:         
            frappe.log_error(frappe.get_traceback(), 'Error')    
            return None

    