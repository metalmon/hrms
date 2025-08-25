# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_chart_name():
	"""Return translatable chart name for Gender Diversity Ratio"""
	return _("Gender Diversity Ratio")


def get_chart_description():
	"""Return translatable description for Gender Diversity Ratio chart"""
	return _("Distribution of employees by gender")
