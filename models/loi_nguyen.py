from odoo import models, fields, api


class LoiNguyen(models.Model):
    _name = 'loi_nguyen'
    _description = 'loi_nguyen'

    name = fields.Char()

    loi_nguyen_ids = fields.Many2many("loi_nguyen", "loi_nguyen_ids", "col1", "col2", string="loi_nguyen_ids")
    bi_loi_nguyen_ids = fields.Many2many("loi_nguyen", "loi_nguyen_ids", "col2", "col1", string="loi_nguyen_ids")

    
    @api.model
    def create(self, vals):
        vals["bi_loi_nguyen_ids"] = vals["loi_nguyen_ids"]
        record = super(LoiNguyen, self).create(vals)
        return record

    def write(self, vals):
        vals["bi_loi_nguyen_ids"] = vals["loi_nguyen_ids"]
        return super(LoiNguyen, self).write(vals)
    

class Tag(models.Model):
    _name = 'loi.nguyen.tag'
    name = fields.Char()
    


