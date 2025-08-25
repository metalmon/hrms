# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_chart_name():
	"""Return translatable chart name for Employees by Type"""
	return _("Employees by Type")


def get_chart_description():
	"""Return translatable description for Employees by Type chart"""
	return _("Distribution of employees by employment type")
