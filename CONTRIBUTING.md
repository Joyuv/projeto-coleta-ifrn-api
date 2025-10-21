# Guia de Contribuição

Obrigado por se interessar em contribuir com este projeto!  
Este é um projeto de pesquisa desenvolvido em **Python** com **Flask**, e buscamos manter o código simples, limpo e bem documentado.

---

## 🧭 Como contribuir

1. Faça um **fork** deste repositório.  
2. Crie uma **branch** para sua modificação:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Faça as alterações desejadas.  
4. Garanta que o código segue as boas práticas e que o projeto roda corretamente.  
5. Envie um **Pull Request** com uma descrição clara do que foi alterado.

---

## ⚙️ Configuração do ambiente local

1. **Clone** o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um **ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure variáveis de ambiente** (se necessário):
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. **Execute o servidor Flask**:
   ```bash
   flask run
   ```

6. Acesse o projeto em:  
   👉 [http://localhost:5000](http://localhost:5000)

---

## 🧩 Diretrizes de código

- Escreva código limpo e legível.  
- Prefira nomes de variáveis e funções descritivos.  
- Comente partes complexas do código.  
- Mantenha a consistência de estilo (indentação, espaçamento, etc.).  
- Sempre teste suas alterações antes de enviar.

---

## 📝 Padrão de commits

Adote mensagens de commit claras e consistentes. Recomenda-se o padrão abaixo:

```
tipo: breve descrição da mudança
```

Tipos comuns:
- `feat:` nova funcionalidade  
- `fix:` correção de bug  
- `docs:` alteração na documentação  
- `refactor:` melhoria de código sem mudar comportamento  
- `test:` adição ou modificação de testes  
- `chore:` tarefas menores ou manutenção

Exemplo:
```
feat: adiciona endpoint de autenticação com Flask
```

---

## 🌱 Padrão de branches

Use nomes de branch descritivos, seguindo o formato:

```
tipo/nome-da-feature
```

Exemplos:
```
feat/api-login
fix/erro-dependencias
docs/atualiza-readme
```

---

## 🤝 Código de conduta

- Respeite os demais contribuidores.  
- Mantenha um ambiente colaborativo e cordial.  
- Discussões são bem-vindas, desde que mantenham o foco técnico e construtivo.

---

## 🧾 Licença

Ao contribuir, você concorda que suas alterações podem ser incluídas sob a mesma licença do projeto.  
Verifique o arquivo `LICENSE` para mais detalhes.

---

💡 *Dica:* Antes de enviar seu Pull Request, rode o projeto localmente e teste todas as rotas e funções alteradas.
