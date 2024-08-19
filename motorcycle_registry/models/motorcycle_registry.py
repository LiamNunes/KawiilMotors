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

    registry_number = fields.Char(string='Registry Number', default=lambda self: self.env['ir.sequence'].next_by_code('registry.number') or 'MRN0000', copy=False, required=True, readonly=True)
    certificate_title = fields.Binary(string='Certificate Title')
    current_mileage = fields.Float(string='Current Mileage')
    date_registry = fields.Date(string='Date of Registry')
    license_plate = fields.Char(string='License Plate')
    vin = fields.Char(string='VIN')
    active = fields.Boolean(string='Active', default=True)

    owner_id = fields.Many2one(comodel_name="res.partner", string='Owner', ondelete='restrict')
    phone = fields.Char(string='Phone', related='owner_id.phone', store=True)
    email = fields.Char(string='Email', related='owner_id.email', store=True)

    make = fields.Char(string='Make', compute='_compute_mmy', store=True)
    model = fields.Char(string='Model', compute='_compute_mmy', store=True)
    year = fields.Char(string='Year', compute='_compute_mmy', store=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('registry_number'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number') or 'MRN0000'
        return super(MotorcycleRegistry, self).create(vals_list)

    @api.constrains('vin')
    def _check_vin(self):
        vin_pattern = r'^[A-Z]{2}[A-Z]{2}\d{2}[A-Z0-9]{2}\d{5}$'
        for record in self:
            if not re.match(vin_pattern, record.vin):
                raise ValidationError("Invalid VIN")

    @api.constrains('license_plate')
    def _check_license_plate(self):
        license_plate_pattern = r'^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$'
        for record in self:
            if not isinstance(record.license_plate, str) or not re.match(license_plate_pattern, record.license_plate):
                raise ValidationError("Invalid license plate")

    @api.depends('vin')
    def _compute_mmy(self):
        for record in self:
            if isinstance(record.vin, str) and record.vin:
                record.make = record.vin[:2]
                record.model = record.vin[2:4]
                record.year = record.vin[4:6]
            else:
                record.make = False
                record.model = False
                record.year = False
            
    