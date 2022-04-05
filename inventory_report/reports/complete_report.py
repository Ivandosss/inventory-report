from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = SimpleReport.generate(data)
        companies = {}

        for item in data:
            if item["nome_da_empresa"] not in companies:
                companies[item["nome_da_empresa"]] = 1
            elif item["nome_da_empresa"] in companies:
                companies[item["nome_da_empresa"]] += 1

        products_report = ""
        for item in companies:
            products_report += f"- {item}: {companies[item]}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{products_report}"
        )
