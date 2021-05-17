# -*- coding: utf-8 -*-
##############################################################################
#
#    Global Resource Systems S.A.R.L.
#
#    Copyright (C) 2021-TODAY Global Resource Systems(<https://www.grs.com>)
#    Author: Global Resource Systems(<https://www.grs.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{ 'sequence': 500,

'name': 'Customer channel',
'version': '1.0',
'category': 'Sales Management',
    'description': """
Allows you to add a channel per client.
==============================================================

You can have a more than one customer in one channel, you can also filter the customers by channel.
""",
'author': 'GRS - Hamza Larmoud',
'website': '',
'summary': '',
'depends': ['sale'],
'data': [ 'views/partner_view.xml',
          'views/sales_menu.xml',
          ],
'license': 'LGPL-3',
'images': ['static/img/banner.png'],
'installable': True,
'application': False,
'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
