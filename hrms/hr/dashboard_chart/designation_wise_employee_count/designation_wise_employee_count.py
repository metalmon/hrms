# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_chart_name():
	"""Return translatable chart name for Designation Wise Employee Count"""
	return _("Designation Wise Employee Count")


def get_chart_description():
	"""Return translatable description for Designation Wise Employee Count chart"""
	return _("Number of employees by job designation")
