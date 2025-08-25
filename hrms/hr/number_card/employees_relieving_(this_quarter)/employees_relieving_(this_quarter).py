# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_label():
	"""Return translatable label for Employees Relieving card"""
	return _("Employees Relieving (This Quarter)")


def get_description():
	"""Return translatable description for Employees Relieving card"""
	return _("Number of employees leaving the company this quarter")
