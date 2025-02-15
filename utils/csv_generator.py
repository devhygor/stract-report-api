import csv
from io import StringIO
from flask import Response

def generate_csv(data, filename):
    csv_data = StringIO()
    if data:
        writer = csv.DictWriter(csv_data, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    response = Response(csv_data.getvalue(), content_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}.csv"
    return response
