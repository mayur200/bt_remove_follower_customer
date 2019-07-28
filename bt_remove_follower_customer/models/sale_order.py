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

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.multi
    def _action_confirm(self):
        res =  super(SaleOrder, self)._action_confirm()
        conf_obj = self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.sale')
        if conf_obj:
            for obj in self.filtered(lambda obj: obj.partner_id in obj.message_partner_ids):
                obj.message_unsubscribe([obj.partner_id.id, obj.user_id.partner_id.id])
        return res
    
class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    @api.multi
    def invoice_validate(self):
        result = super(AccountInvoice, self).invoice_validate()
        config_obj = self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.invoice')
        if config_obj:
            for invoice in self.filtered(lambda invoice: invoice.partner_id in invoice.message_partner_ids):
                invoice.message_unsubscribe([invoice.partner_id.id, invoice.user_id.partner_id.id])
        return result

class PurchaseInvoiceFollow(models.Model):
    _inherit = "purchase.order"


    @api.multi
    def button_confirm(self):
        result = super(PurchaseInvoiceFollow, self).button_confirm()
        purchase_obj = self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.purchase')
        if purchase_obj:
            # if self.partner_id in self.message_partner_ids:
                self.message_unsubscribe([self.partner_id.id, self.create_uid.partner_id.id])
        return result

    @api.multi
    def action_view_picking(self):
        result = super(PurchaseInvoiceFollow, self).action_view_picking()
        rcv_obj = self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.purchase')
        if rcv_obj:
            self.message_unsubscribe([self.partner_id.id, self.create_uid.partner_id.id])
        return result


class StockPickingUnfollowers(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_validate(self):
        result = super(PurchaseInvoiceFollow, self).action_view_picking()
        rcv_obj = self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.purchase')
        if rcv_obj:
            self.message_unsubscribe([self.partner_id.id, self.create_uid.partner_id.id])
        return result

class StockImmediateTransferFollowe(models.TransientModel):
    _inherit = "stock.immediate.transfer"

    @api.multi
    def process(self):
        result = super(StockImmediateTransferFollowe, self).process()
        trn = self.env['ir.config_parameter'].sudo().get_param('bt_remove_follower_customer.purchase')
        if trn:
            self.pick_ids.message_unsubscribe([self.pick_ids.partner_id.id, self.pick_ids.create_uid.partner_id.id])
        return result










