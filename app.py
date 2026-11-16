from flask import Flask, render_template

app = Flask(__name__)

# Edite estas informações para personalizar o portfólio.
profile = {
    "name": "Eduarda Lino",
    "role": "Tecnologia, sistemas e dados",
    "headline": "Transformo curiosidade em soluções digitais.",
    "intro": (
        "Sou formada em Análise e Desenvolvimento de Sistemas e tenho interesse em "
        "análise de sistemas, banco de dados, desenvolvimento e infraestrutura de TI. "
        "Gosto de aprender na prática, entender problemas e construir soluções organizadas."
    ),
    "email": "eduardalinno15@gmail.com",  
    "linkedin": "https://www.linkedin.com/in/eduarda-lino-186743185/", 
    "github": "https://github.com/eduarda-ai",  
}

skills = [
    "HTML e CSS",
    "Python",
    "MySQL",
    "Power BI e Excel",
    "Suporte e infraestrutura",
    "Redes, DNS e VPN",
    
]

projects = [
    {
        "number": "01",
        "category": "Banco de dados",
        "name": "CRUD de funcionários",
        "description": "Projeto de prática com operações de cadastro, consulta, atualização e exclusão utilizando banco de dados MySQL.",
        "tags": ["MySQL", "SQL", "CRUD"],
        "link": "#contato",
        "link_label": "Adicionar repositório",
    },
    {
        "number": "02",
        "category": "Desenvolvimento desktop",
        "name": "CalculaChurras",
        "description": "Aplicação desktop desenvolvida com C# e WPF como exercício de lógica, construção de interface e organização de funcionalidades.",
        "tags": ["C#", ".NET", "WPF"],
        "link": "#contato",
        "link_label": "Adicionar demonstração",
    },
    {
        "number": "03",
        "category": "Automação de processos",
        "name": "Melhorias Contínuas",
        "description": "Aplicação criada no Power Apps para apoiar o registro e o acompanhamento de ideias de melhoria de processos.",
        "tags": ["Power Apps", "Processos", "Low-code"],
        "link": "#contato",
        "link_label": "Adicionar demonstração",
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=profile,
        skills=skills,
        projects=projects,
    )

if __name__ == "__main__":
    app.run(debug=True)
