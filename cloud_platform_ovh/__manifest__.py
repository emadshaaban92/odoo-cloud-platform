# Copyright 2017-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    "name": "Cloud Platform OVH",
    "summary": "Addons required for the Camptocamp Cloud Platform on OVH",
    "version": "12.0.2.0.1",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Extra Tools",
    "depends": [
        "cloud_platform",
        "attachment_swift",
        "monitoring_statsd",
    ],
    "excludes": [
        "cloud_platform_exoscale",
    ],
    "website": "https://github.com/camptocamp/odoo-cloud-platform",
    "data": [],
    "installable": True,
}
