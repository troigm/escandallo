# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
	'name': 'Cost calculation tool',
    'summary': """Cost calculation tool""",

    'description': "", # Dejar vacio para que coja el README.rst
	"version": "8.0.0.1.0",
    "author": "Acelerem",
    "website": "www.acelerem.com",
    "category": "Warehouse Management",
    "license": "GPL-3",

	'depends': [
		"base",
        "product",
	 ],

	'data': [
		'views/cost_view.xml',
		'views/escandallo_report.xml',
		'views/report_cost.xml',
	],
    "installable": True,
}