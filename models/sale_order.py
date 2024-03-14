from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Agregar un campo Many2one para relacionarse con la oportunidad desde la orden de venta
    opportunity_stage_id = fields.Many2one('crm.stage', string='Etapa actual', related='opportunity_id.stage_id',
                                           store=True)
    opportunity_closed_status = fields.Selection(related='opportunity_id.closed_status', string='Estado del cierre',
                                              store=True)

