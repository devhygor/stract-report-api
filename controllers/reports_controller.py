from services.api_client import StractAPIClient
from utils.data_processing import process_insights, summarize_by_account, summarize_by_platform
from utils.csv_generator import generate_csv

class ReportsController:
    def __init__(self):
        self.client = StractAPIClient()
        self.platforms = self.client.get_platforms()

    def validate_platform(self, platform):
        # Verifica se a plataforma está nas chaves do dicionário das plataformas validas
        if platform not in self.platforms.keys():
            # Mostra as chaves válidas na mensagem de erro
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
        return {
            "name": "Hygor Melo Rocha",
            "email": "hygor.k92@gmail.com.br",
            "linkedin": "https://www.linkedin.com/in/devhygor/"
        }

    def platform_report(self, platform):
        validation_error = self.validate_platform(platform)
        if validation_error:
            return validation_error
        data = self.collect_data([platform])
        return generate_csv(data, f"{platform}_report")

    def platform_summary(self, platform):
        validation_error = self.validate_platform(platform)
        if validation_error:
            return validation_error
        data = self.collect_data([platform])
        summary = summarize_by_account(data)
        return generate_csv(summary, f"{platform}_summary")

    def general_report(self):
        data = self.collect_data(self.platforms)
        return generate_csv(data, "general_report")

    def general_summary(self):
        data = self.collect_data(self.platforms)
        summary = summarize_by_platform(data)
        return generate_csv(summary, "general_summary")
