# Copyright 2023 ForgeFlow, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Website Search in Header",
    "category": "Website",
    "version": "17.0.1.1.0",
    "author": "ForgeFlow, Ooops, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/website",
    "license": "LGPL-3",
    "depends": [
        # "web",
        "website",
    ],
    "data": [
        "views/templates.xml",
    ],
    "assets": {
        "website_search_header.assets_frontend": [
            "website_search_header/static/src/js/website.js",
            # "website_search_header/static/src/scss/website_search_header.scss",
        ],
    },
    "installable": True,
}