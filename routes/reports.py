from flask import Blueprint
from controllers.reports_controller import ReportsController

reports_bp = Blueprint("reports", __name__)
reports_controller = ReportsController()

@reports_bp.route("/")
def home():
    return reports_controller.home()

@reports_bp.route("/<platform>")
def platform_report(platform):
    return reports_controller.platform_report(platform)

@reports_bp.route("/<platform>/resumo")
def platform_summary(platform):
    return reports_controller.platform_summary(platform)

@reports_bp.route("/geral")
def general_report():
    return reports_controller.general_report()

@reports_bp.route("/geral/resumo")
def general_summary():
    return reports_controller.general_summary()


if __name__ == "__main__":
    plataform_report = reports_controller.platform_report("ga4")
    print(plataform_report)