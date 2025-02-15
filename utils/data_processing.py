from collections import defaultdict

def process_insights(insights_data, platform_name, account_name):
    for item in insights_data:
        item["Platform"] = platform_name
        item["Account Name"] = account_name
    return insights_data

def summarize_by(data, group_by):
    summary = defaultdict(lambda: defaultdict(float))
    for item in data:
        group_value = item[group_by]
        for key, value in item.items():
            if key not in ["Account Name", "Platform"]:
                try:
                    summary[group_value][key] += float(value)
                except ValueError:
                    summary[group_value][key] = ""  # Deixa vazio se não for numérico
    summary_list = []
    for group_value, metrics in summary.items():
        row = {group_by: group_value}
        row.update(metrics)
        summary_list.append(row)
    return summary_list

def summarize_by_account(data):
    return summarize_by(data, "Account Name")

def summarize_by_platform(data):
    return summarize_by(data, "Platform")
