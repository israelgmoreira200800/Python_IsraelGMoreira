from flask import Flask

app = Flask(__name__) 

@app.route('/')


def index():
    return '''
        <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo | Israel Gomes Moreira</title>
    <style>
        :root {
            --primary: #0056b3;
            --secondary: #333;
            --bg: #f4f7f6;
            --text: #444;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        header {
            text-align: center;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 20px;
            margin-bottom: 25px;
        }
        header h1 {
            color: var(--secondary);
            font-size: 2.2rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        header p {
            color: var(--primary);
            font-weight: 600;
            margin-top: 5px;
        }
        .contact-info {
            margin-top: 15px;
            font-size: 0.9rem;
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }
        .contact-info span {
            display: flex;
            align-items: center;
        }
        section {
            margin-bottom: 30px;
        }
        h2 {
            color: var(--primary);
            font-size: 1.4rem;
            border-bottom: 1px solid #ddd;
            padding-bottom: 5px;
            margin-bottom: 15px;
            text-transform: uppercase;
        }
        .edu-item, .exp-item {
            margin-bottom: 15px;
        }
        .item-title {
            font-weight: bold;
            color: var(--secondary);
        }
        .item-sub {
            font-style: italic;
            color: #666;
            font-size: 0.95rem;
        }
        ul {
            list-style-position: inside;
            margin-left: 10px;
        }
        li {
            margin-bottom: 5px;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 10px;
        }
        .skill-tag {
            background: #e9ecef;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 0.9rem;
            text-align: center;
            font-weight: 500;
        }
        @media (max-width: 600px) {
            .container { padding: 20px; }
            header h1 { font-size: 1.8rem; }
            .contact-info { flex-direction: column; gap: 5px; align-items: center; }
        }
    </style>
</head>
<body>

<div class="container">

    <header>
        <h1>Israel Gomes Moreira</h1>
        <p>Estudante de TI | Desenvolvimento de Software</p>
        <div class="contact-info">
            <span>📍 Belo Horizonte, MG</span>
            <span>📧 seu.email@email.com</span>
            <span>📞 (31) 99999-9999</span>
            <span>🔗 linkedin.com</span>
        </div>
    </header>

    <section>
        <h2>Objetivo Profissional</h2>
        <p>Busco minha primeira oportunidade no mercado de tecnologia como Estagiário ou Assistente de TI. Objetivo aplicar os conhecimentos teóricos e práticos adquiridos em minha formação acadêmica, contribuindo para o sucesso da equipe e desenvolvendo minhas habilidades técnicas.</p>
    </section>

    <section>
        <h2>Formação Acadêmica</h2>
        <div class="edu-item">
            <p class="item-title">Colégio COTEMIG</p>
            <p class="item-sub">Curso Técnico em Informática / TI Básica</p>
            <p class="item-sub">Conclusão Prevista: 2027</p>
        </div>
    </section>

    <section>
        <h2>Principais Competências</h2>
        <div class="skills-grid">
            <div class="skill-tag">Lógica de Programação</div>
            <div class="skill-tag">HTML5 & CSS3</div>
            <div class="skill-tag">Suporte Técnico</div>
            <div class="skill-tag">Sistemas Operacionais</div>
            <div class="skill-tag">Pacote Office</div>
            <div class="skill-tag">Trabalho em Equipe</div>
        </div>
    </section>

    <section>
        <h2>Projetos e Atividades</h2>
        <ul>
            <li>Desenvolvimento de projetos acadêmicos utilizando versionamento com Git e GitHub.</li>
            <li>Resolução de problemas de lógica computacional estruturada.</li>
            <li>Configuração de ambientes locais de desenvolvimento e redes básicas.</li>
        </ul>
    </section>

    <section>
        <h2>Idiomas</h2>
        <p><strong>Português:</strong> Nativo</p>
        <p><strong>Inglês:</strong> Instrumental / Técnico</p>
    </section>

</div>

</body>
</html>

'''


if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
