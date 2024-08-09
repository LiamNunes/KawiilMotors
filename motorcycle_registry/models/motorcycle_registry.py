from odoo import fields, models, api
import re
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _record_name = "registry_number"
    _sql_constraints = [
        ('vin_unique', 'unique(vin)', 'The VIN must be unique.'),
        ('license_plate_unique', 'unique(license_plate)', 'The License Plate must be unique.')
    ]
    

    registry_number = fields.Char(string='Registry Number',default="MRN0000",copy=False, required=True,readonly=True)
    certificate_title = fields.Binary(string='Certificate Title')
    current_mileage = fields.Float(string='Current Mileage')
    date_registry = fields.Date(string='Date of Registry')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    license_plate = fields.Char(string='License Plate', required=True)
    vin = fields.Char(string='VIN', required=True)
    active = fields.Boolean(string='Active', default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number',('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin(self):
        vin_pattern = r'^[A-Z]{2}[A-Z]{2}\d{2}[A-Z0-9]{2}\d{5}$'
        for record in self:
            if not re.match(vin_pattern, record.vin):
                raise ValidationError("invalid vin")

    @api.constrains('license_plate')
    def _check_license_plate(self):
        license_plate_pattern = r'^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$'
        for record in self:
            if not re.match(license_plate_pattern, record.license_plate):
                raise ValidationError("invalid license")