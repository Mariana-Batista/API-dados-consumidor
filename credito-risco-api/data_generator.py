from faker import Faker
import random

fake = Faker('pt_BR')

def generate_credit_data():
    data = {
        "dados_demograficos": {
            "id": fake.uuid4(),  # ID único para cada cliente
            "nome": fake.name(),  # Nome gerado aleatoriamente
            "idade": random.randint(18, 80),
            "genero": random.choice(["Masculino", "Feminino"]),
            "estado_civil": random.choice(["Solteiro", "Divorciado", "Casado", "Uniao Estavel"]),
            "numero_de_dependentes": random.randint(0, 5)
        },
        "historico_financeiro": {
            "renda_mensal": round(random.uniform(1000, 10000), 2),
            "historico_de_credito": random.choice(["Bom", "Razoavel", "Ruim"]),
            "patrimonio_liquido": round(random.uniform(5000, 1000000), 2),
            "limite_de_credito": round(random.uniform(500, 20000), 2),
            "tipo_de_conta": random.choice(["Cartao de credito", "Emprestimo Pessoal", "Hipoteca"]),
        },
        "comportamento_financeiro": {
            "historico_de_pagamento": random.choice(["Sem atrasos nos pagamentos", "Atrasos nos pagamentos", "Inadimplencias"]),
            "utilizacao_do_credito": round(random.uniform(0.1, 1.0), 2),  # Percentual usado
            "saldo_em_aberto": round(random.uniform(0, 20000), 2),
        },
        "dados_relacionados_ao_emprestimo": {
            "montante_do_emprestimo": round(random.uniform(1000, 50000), 2),
            "taxa_de_juros": round(random.uniform(0.01, 0.15), 2),
            "prazo_do_emprestimo": random.randint(12, 360),
            "finalidade_do_emprestimo": random.choice(["Carro", "Educacao", "Melhoria da Casa", "Negocio"]),
            "garantias_oferecidas": random.choice(["Casa", "Carro", "Nenhum"]),
        },
        "score_credito": {
            "credito_score": random.randint(300, 1000)  # Score de 300 a 1000
        },
        "dados_geograficos": {
            "localizacao_residencial": fake.address(),
        },
        "historico_de_emprego": {
            "status_do_emprego": random.choice(["Empregado", "Autonomo", "Desempregado"]),
            "tempo_no_trabalho_atual_em_anos": random.randint(0, 30),
            "industria": random.choice(["Tecnologia", "Financas", "Saude", "Varejo", "Outros"]),
        },
        "outros_dados_relevantes": {
            "nivel_educacao": random.choice(["Ensino Medio Incompleto", "Ensino Medio Completo", "Superior Incompleto", "Superior Completo", "Mestrado", "PhD"]),
            "comportamento_de_compra": random.choice(["Conservador", "Moderado", "Agressivo"]),
        }
    }
    
    return data
