# Copyright (c) 2021, Kevin Rojas and contributors
# For license information, please see license.txt

# import frappe
import logging
from frappe.model.document import Document

_logger = logging.getLogger(__name__)

class LibraryMember(Document):
	
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
		print(f'\n\nInspeccionando el registro {self.as_dict()}\n\n')

	