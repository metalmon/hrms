# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_chart_name():
	"""Return translatable chart name for Employees by Branch"""
	return _("Employees by Branch")


def get_chart_description():
	"""Return translatable description for Employees by Branch chart"""
	return _("Distribution of employees by branch location")
