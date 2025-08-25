# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_chart_name():
	"""Return translatable chart name for Department Wise Employee Count"""
	return _("Department Wise Employee Count")


def get_chart_description():
	"""Return translatable description for Department Wise Employee Count chart"""
	return _("Number of employees by department")
