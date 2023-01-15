# Copyright (c) 2021, Kevin Rojas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryMembership(Document):

    # check before submitting this document
    def before_submit(self):
        exists = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                # check for submitted documents
                "docstatus": 1,
                # check if the membership's end date is later than this membership's start date
                "to_date": (">", self.from_date),
            },
        )
        if exists:
            frappe.throw("There is an active membership for this member!")