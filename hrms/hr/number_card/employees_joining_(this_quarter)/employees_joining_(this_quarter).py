# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_label():
	"""Return translatable label for Employees Joining card"""
	return _("Employees Joining (This Quarter)")


def get_description():
	"""Return translatable description for Employees Joining card"""
	return _("Number of employees joining the company this quarter")
