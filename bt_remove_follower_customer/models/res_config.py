# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018-BroadTech IT Solutions (<http://www.broadtech-innovations.com/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU LESSER General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER General Public License for more details.
#
#    You should have received a copy of the GNU LESSER General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################


from odoo import models,api, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    sale = fields.Boolean(string='Prevents adding Customer as followers while confirming sale order')
    invoice = fields.Boolean(string='Prevents adding Customer as followers while validating invoice')
    purchase = fields.Boolean(string='Prevents add Customer as followers while validating invoice')
    
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            sale=self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.sale'),
            invoice=self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.invoice'),
            purchase=self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.purchase')
        )
        return res
    
    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('bt_remove_follower_customer.sale', self.sale)
        self.env['ir.config_parameter'].sudo().set_param('bt_remove_follower_customer.invoice', self.invoice)
        self.env['ir.config_parameter'].sudo().set_param('bt_remove_follower_customer.purchase', self.purchase)



        
        
