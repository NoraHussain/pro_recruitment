app_name = "pro_recruitment"
app_title = "Pro Recruitment"
app_publisher = "prosite"
app_description = "Prosite added value for recruitment"
app_email = "prosite@p.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pro_recruitment/css/pro_recruitment.css"
# app_include_js = "/assets/pro_recruitment/js/pro_recruitment.js"

# include js, css files in header of web template
# web_include_css = "/assets/pro_recruitment/css/pro_recruitment.css"
# web_include_js = "/assets/pro_recruitment/js/pro_recruitment.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pro_recruitment/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Job Applicant" : "overrides/job_applicant.js", "Job Opening" : "overrides/job_opening.js" }
doctype_list_js = {"Job Applicant" : "overrides/job_applicant.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "pro_recruitment/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "pro_recruitment.utils.jinja_methods",
#	"filters": "pro_recruitment.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pro_recruitment.install.before_install"
after_install = "pro_recruitment.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pro_recruitment.uninstall.before_uninstall"
# after_uninstall = "pro_recruitment.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "pro_recruitment.utils.before_app_install"
# after_app_install = "pro_recruitment.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "pro_recruitment.utils.before_app_uninstall"
# after_app_uninstall = "pro_recruitment.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pro_recruitment.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Job Opening": "pro_recruitment.overrides.job_opening.CustomJobOpening"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"pro_recruitment.tasks.all"
#	],
#	"daily": [
#		"pro_recruitment.tasks.daily"
#	],
#	"hourly": [
#		"pro_recruitment.tasks.hourly"
#	],
#	"weekly": [
#		"pro_recruitment.tasks.weekly"
#	],
#	"monthly": [
#		"pro_recruitment.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "pro_recruitment.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "pro_recruitment.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "pro_recruitment.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pro_recruitment.utils.before_request"]
# after_request = ["pro_recruitment.utils.after_request"]

# Job Events
# ----------
# before_job = ["pro_recruitment.utils.before_job"]
# after_job = ["pro_recruitment.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"pro_recruitment.auth.validate"
# ]
