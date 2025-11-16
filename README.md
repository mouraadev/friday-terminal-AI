FRIDAY é uma assistente virtual feita em Python, usando o modelo GPT-OSS da Together.
Ela responde perguntas, mantém histórico de chat e suporta streaming de mensagens.

## Como rodar

1. Instale as dependências:
pip install -r requirements.txt


2. Configure sua chave da Together no arquivo .env:
TOGETHER_API_KEY=sua_chave_aqui

3. Execute o projeto:
python main.py

## Comandos Internos
- '/mode' - mudar modo de interação
- '/clear' - limpar histórico
- '/save' - salvar histórico
- 'exit' ou 'quit' - sair do programa

## Estrutura do projeto
friday/
│   .env
│   .gitignore
│   main.py
│
├── config/
│   └── prompts.py
├── core/
│   ├── ai_client.py
│   ├── chat_manager.py
│   ├── engine.py
│   └── modes.py
├── ui/
│   ├── banner.py
│   ├── gradient.py
│   └── printer.py
└── utils/



