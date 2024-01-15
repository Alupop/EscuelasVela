# -*- coding: utf-8 -*-

from odoo import models, fields

class Escuela(models.Model):
    _name = 'escuelas_vela.escuela'
    _description = 'Escuela de Vela'

    name = fields.Char(string='Denominación', required=True)
    logotipo = fields.Binary(string='Logotipo')
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')

class Curso(models.Model):
    _name = 'escuelas_vela.curso'
    _description = 'Curso de Vela'

    title = fields.Char(string='Título', required=True)
    duracion_dias = fields.Integer(string='Duración en días')
    duracion_horas = fields.Integer(string='Duración en horas')
    precio = fields.Float(string='Precio')

    escuela_id = fields.Many2one('escuelas_vela.escuela', string='Escuela')

class Monitor(models.Model):
    _name = 'escuelas_vela.monitor'
    _description = 'Monitor de Vela'

    name = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    direccion = fields.Char(string='Dirección')
    codigo_identificacion = fields.Char(string='Código de identificación', required=True, unique=True)

    escuela_ids = fields.Many2many('escuelas_vela.escuela', string='Escuelas colaboradoras')

class Alumno(models.Model):
    _name = 'escuelas_vela.alumno'
    _description = 'Alumno de Vela'

    name = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    direccion = fields.Char(string='Dirección')
    numero_matricula = fields.Char(string='Número de matrícula', required=True)
    
    escuela_id = fields.Many2one('escuelas_vela.escuela', string='Escuela')