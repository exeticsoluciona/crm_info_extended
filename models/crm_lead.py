# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime,timedelta,time


class CrmLead(models.Model):
    _inherit = "crm.lead"

    closed_status = fields.Selection([
        ('pending_closure', 'Pendiente de cierre'),
        ('closed_lost', 'Cerrado - Perdido'),
        ('closed_won', 'Cerrado - Ganado'),
    ], string='Estado de Cierre', compute='_compute_closed_status', store=True)

    @api.depends('won_status')
    def _compute_closed_status(self):
        for lead in self:
            if lead.won_status == 'won':
                lead.closed_status = 'closed_won'
            elif lead.won_status == 'lost':
                lead.closed_status = 'closed_lost'
            else:
                lead.closed_status = 'pending_closure'


    # def _handle_won_lost(self, vals):
    #     # Llama al método original para obtener los valores que devuelve
    #     result = super(CrmLead, self)._handle_won_lost(vals)
    #     if self.won_status == 'won':
    #         self.closed_status = 'closed_lost'
    #     elif self.won_status == 'lost':
    #         self.closed_status = 'closed_won'
    #     return result

    
