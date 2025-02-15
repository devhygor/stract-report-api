from flask import render_template
from services.api_client import StractAPIClient
from utils.data_processing import process_insights, summarize_by_account, summarize_by_platform
from utils.csv_generator import generate_csv

class ReportsController:
    def __init__(self):
        self.client = StractAPIClient()
        self.platforms = self.client.get_platforms()

    def validate_platform(self, platform):
        if platform not in self.platforms.keys():
            valid_platforms = ", ".join(self.platforms.keys())
            return {"error": f"Plataforma inválida! Utilize uma das plataformas válidas: {valid_platforms}"}, 400

    def collect_data(self, platforms):
        all_data = []
        for platform in platforms:
            accounts_data = self.client.get_accounts(platform)
            fields = self.client.get_fields(platform)
            for account in accounts_data:
                if isinstance(account, dict) and "id" in account and "name" in account:
                    insights = self.client.get_insights(platform, account, fields)
                    if 'insights' in insights:
                        processed_data = process_insights(insights['insights'], platform, account["name"])
                        all_data.extend(processed_data)
                    else:
                        print(f"Nenhum dado de insights encontrado para a conta: {account['name']} na plataforma: {platform}")
        return all_data

    def home(self):
        user_info = {
            "name": "Hygor Melo Rocha",
            "email": "hygor.k92@gmail.com.br",
            "linkedin": "https://www.linkedin.com/in/devhygor/"
        }
        return render_template('home.html', title="Home", user_info=user_info)

    def platform_report(self, platform):
        validation_error = self.validate_platform(platform)
        if validation_error:
            return validation_error
        data = self.collect_data([platform])
        headers = data[0].keys() if data else []
        return render_template('table.html', title=f"Relatório de {platform}", headers=headers, data=data)
        # return generate_csv(data, f"{platform}_report")

    def platform_summary(self, platform):
        validation_error = self.validate_platform(platform)
        if validation_error:
            return validation_error
        data = self.collect_data([platform])
        summary = summarize_by_account(data)
        headers = summary[0].keys() if summary else []
        return render_template('table.html', title=f"Resumo de {platform}", headers=headers, data=summary)
        # return generate_csv(summary, f"{platform}_summary")

    def general_report(self):
        data = self.collect_data(self.platforms)
        headers = data[0].keys() if data else []
        return render_template('table.html', title="Relatório Geral", headers=headers, data=data)
        # return generate_csv(data, "general_report")

    def general_summary(self):
        data = self.collect_data(self.platforms)
        summary = summarize_by_platform(data)
        headers = summary[0].keys() if summary else []
        return render_template('table.html', title="Resumo Geral", headers=headers, data=summary)
        # return generate_csv(summary, "general_summary")
