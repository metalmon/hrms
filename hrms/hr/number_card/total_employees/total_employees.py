# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_label():
	"""Return translatable label for Total Employees card"""
	return _("Total Employees")


def get_description():
	"""Return translatable description for Total Employees card"""
	return _("Total number of active employees in the company")
