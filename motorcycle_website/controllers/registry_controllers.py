from odoo import http


class MotorcycleWebsite(http.Controller):
    @http.route('/compare', auth='public', website=True, sitemap=True)
    def compare(self, **kw):
        motorcycles = http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')])
        return http.request.render('motorcycle_website.compare_template',{
            'motorcycles': motorcycles,
        })
