# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_label():
	"""Return translatable label for Employee Exits card"""
	return _("Employee Exits (This Year)")


def get_description():
	"""Return translatable description for Employee Exits card"""
	return _("Number of employees who left the company this year")
