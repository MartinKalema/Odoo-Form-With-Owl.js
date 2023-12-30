# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class NiraDataEntry(models.Model):
    _name = 'nira.data.entry'
    # Chatter window
    _inherit = ['mail.thread']
    _description = 'store ID application data'

    application_reference = fields.Char(string='Application ID')
    name = fields.Char(string='Applicant Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True, required=True)
    applicant_photo = fields.Image(string='Photo', required=True, tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True, required=True)
    reference_letter = fields.Image(string='LC Reference Letter', required=True, tracking=True)
    nationality = fields.Char(string='Nationality', required=True, tracking=True)
    county = fields.Char(string='County', required=True, tracking=True)
    parish = fields.Char(string='Parish/Ward', required=True)
    village = fields.Char(string='Village', required=True, tracking=True)
    state = fields.Selection([
        ('application', 'Application'),
        ('review', 'Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='application', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        string='Gender', tracking=True, required=True)
    citizenship_type = fields.Selection([
        ('birth', 'Birth'),
        ('naturalization', 'Naturalization'),
        ('registration', 'Registration')],
        string='Citizenship Type', tracking=True, required=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                record.age = today.year - record.date_of_birth.year
            else:
                record.age = 0

    @staticmethod
    def set_to_review(self):
        for record in self:
            record.state = 'review'

    @staticmethod
    def set_to_approved(self):
        for record in self:
            record.state = 'approved'

    @staticmethod
    def set_to_rejected(self):
        for record in self:
            record.state = 'rejected'


# from odoo import models, fields, api


# class nira_data_entry(models.Model):
#     _name = 'nira_data_entry.nira_data_entry'
#     _description = 'nira_data_entry.nira_data_entry'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

