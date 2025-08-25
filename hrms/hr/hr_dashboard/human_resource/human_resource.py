# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_dashboard_name():
	"""Return translatable name for Human Resource dashboard"""
	return _("Human Resource")


def get_dashboard_description():
	"""Return translatable description for Human Resource dashboard"""
	return _("Analytics dashboard for Human Resource management")
