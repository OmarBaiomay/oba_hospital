# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Appointment(models.Model):
    _name = 'hospital.patient_appointment'
    _description = 'Patient Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref' # Used For Giving a name For Record

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], default="draft", string="State", tracking=True, required=True)

    ref = fields.Char(string="Reference", default="New", readonly=True, tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient",  tracking=True)
    doctor_id = fields.Many2one('res.users', string="Doctor",  tracking=True)
    gender = fields.Selection(string="Gender", tracking=True, related="patient_id.gender", readonly=True)
    appointment_date = fields.Datetime(string="Appointment Date", tracking=True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
        ], string="Priority", tracking=True)

    prescription = fields.Html(string="Prescription", tracking=True)

    @api.model
    def create(self, vals_list):
        res = super(Appointment, self).create(vals_list)

        if res.ref == "New":
            res.ref = self.env['ir.sequence'].next_by_code("appointment_sequence")

        return res

    @api.onchange('state')
    def celebrate_done(self):
        if self.state == 'done':
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': "Appointment Done Successfully",
                    'img_url': '/web/static/img/smile.svg',
                    'type': 'rainbow_man',
                }
            }


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
