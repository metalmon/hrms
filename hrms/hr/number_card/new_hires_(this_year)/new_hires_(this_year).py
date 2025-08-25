# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe
from frappe import _


def get_label():
	"""Return translatable label for New Hires card"""
	return _("New Hires (This Year)")


def get_description():
	"""Return translatable description for New Hires card"""
	return _("Number of new employees hired this year")
