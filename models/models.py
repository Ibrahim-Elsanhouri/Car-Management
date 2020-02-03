# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Parking(models.Model):
    _name = 'parking.parking'
    #     _description = 'my_first_module.my_first_module'

    name = fields.Char(string='Name')

    cars = fields.One2many('car.car', 'parking_id', string="Cars")


class Car(models.Model):
    _name = 'car.car'
    #     _description = 'my_first_module.my_first_module'

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string="Horse Power")
    door_numbers = fields.Integer(string="Doors Numbers")
    driver_id = fields.Many2one('res.partner', string='Driver')
    parking_id = fields.Many2one('parking.parking', string='Parking')
    features_ids = fields.Many2many('car.feature', string="Features")
    total_speed = fields.Integer(string="Total Speed", compute="get_total_speed")
    status = fields.Selection([('new', 'New'), ('used', 'Used'), ('sold', 'Sold')], string="status", default='new')
    car_sequence = fields.Char(string="Car Sequence")

    def get_total_speed(self):
        self.total_speed = self.horse_power * 10

    def set_car_to_used(self):
        self.status = 'used'

    def set_car_to_sold(self):
        self.status = 'sold'

    @api.model
    def create(self, vals):
        vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')

        if vals['door_numbers'] == 6:
            raise ValidationError("Max Number for Car Doors is 6")




        result = super(Car, self).create(vals)
        return result
    
    def unlink(self):
        for rec in self :
            if rec.horse_power == 5:
                raise ValidationError("Horse Power Cannot be 5")
            return super(Car , self).unlink()


# @api.model
# def create(self, vals):
#  vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')
# result = super(Car, self).create(vals)
# return result


#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Task(models.Model):
    _name = 'task.task'
    #     _description = 'my_first_module.my_first_module'

    name = fields.Char(string='Name')


class Carfeature(models.Model):
    _name = 'car.feature'
    #     _description = 'my_first_module.my_first_module'

    name = fields.Char(string='Name')
    value = fields.Char(string='value')
