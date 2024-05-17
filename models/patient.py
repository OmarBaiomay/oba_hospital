# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(string="Reference", default="New", readonly=True)
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender")

    @api.model
    def create(self, vals_list):
        res = super(Patient, self).create(vals_list)

        if res.ref == "New":
            res.ref = self.env['ir.sequence'].next_by_code("patient_sequence")

        return res











