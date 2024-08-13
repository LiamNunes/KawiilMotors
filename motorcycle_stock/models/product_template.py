from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    detailed_type = fields.Selection(selection_add=[('motorcycle','Motorcycle')],ondelete={'motorcycle':'set service'})

    horsepower = fields.Float(string='Horsepower')
    top_speed = fields.Float(string='Top Speed')
    torque = fields.Float(string='Torque')
    battery_capacity = fields.Selection(
        [('xs', 'Small'), ('m', 'Medium'), ('l', 'Long'), ('xl', 'Extra Large')],
        string='Battery Capacity'
    )
    charge_time = fields.Float(string='Charge Time')
    range = fields.Float(string='Range')
    weight = fields.Float(string='Weight')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')
    year = fields.Char(string='Year')
    
    @api.model
    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle']='product'
        return type_mapping