from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        manufacturing_date = []

        expired_dates = []
        companies = []
        for product in inventory:
            manufacturing_date.append(product['data_de_fabricacao'])
            dateNow = str(datetime.now().today())
            if product['data_de_validade'] > dateNow:
                expired_dates.append(product['data_de_validade'])

            companies.append(product['nome_da_empresa'])

        common = Counter(companies).most_common()[0][0]
        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date)}\n"
            f"Data de validade mais próxima: {min(expired_dates)}\n"
            f"Empresa com maior quantidade de produtos estocados: {common}\n"
        )
