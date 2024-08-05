from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _record_name = "registry_number"

    registry_number = fields.Char(string='Registry Number', required=True)
    certificate_title = fields.Binary(string='Certificate Title')
    current_mileage = fields.Float(string='Current Mileage')
    date_registry = fields.Date(string='Date of Registry')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    license_plate = fields.Char(string='License Plate')
    vin = fields.Char(string='VIN', required=True)