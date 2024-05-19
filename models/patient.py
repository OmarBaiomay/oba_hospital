# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    active = fields.Boolean(string="Active", default=True, tracking=True)
    ref = fields.Char(string="Reference", default="New", readonly=True, tracking=True)
    name = fields.Char(string="Name", required=True,tracking=True)
    age = fields.Integer(string="Age", required=True,tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender", required=True,tracking=True)
    image = fields.Image(string="Image", tracking=True)

    @api.model
    def create(self, vals_list):
        res = super(Patient, self).create(vals_list)

        if res.ref == "New":
            res.ref = self.env['ir.sequence'].next_by_code("patient_sequence")

        return res











