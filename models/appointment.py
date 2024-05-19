# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Appointment(models.Model):
    _name = 'hospital.patient_appointment'
    _description = 'Patient Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'  # Used For Giving a name For Record

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], default="draft", string="State", tracking=True, required=True)

    ref = fields.Char(string="Reference", default="New", readonly=True, tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", tracking=True)
    doctor_id = fields.Many2one('res.users', string="Doctor", tracking=True)
    gender = fields.Selection(string="Gender", tracking=True, related="patient_id.gender", readonly=True)
    appointment_date = fields.Datetime(string="Appointment Date", tracking=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string="Priority", tracking=True)

    prescription = fields.Html(string="Prescription", tracking=True)

    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id',
                                        string="Pharmacy")

    @api.model
    def create(self, vals_list):
        res = super(Appointment, self).create(vals_list)

        if res.ref == "New":
            res.ref = self.env['ir.sequence'].next_by_code("appointment_sequence")

        return res

    def action_make_it_normal(self):
        for rec in self:
            if rec.priority != '0':
                rec.priority = '0'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': "Changed To Normal Successfully",
                    'img_url': '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': "Appointment Done Successfully",
                    'img_url': '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }

    def action_cancel(self):
        for rec in self:
            rec.state = 'canceled'


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = "Appointment Pharmacy Lines"

    appointment_id = fields.Many2one('hospital.patient_appointment', string="Appointment")
    product_id = fields.Many2one('product.product', string="Medicine", required=True)
    price_unit = fields.Float(string="Price", related="product_id.list_price")
    qty = fields.Float(string="Quantity")
