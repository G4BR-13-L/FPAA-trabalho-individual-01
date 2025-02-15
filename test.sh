#!/bin/bash

# Função para tratar erros
handle_error() {
    echo "Erro: $1"
    exit 1
}

# Testes para o algoritmo em Python
echo "Executando testes para o algoritmo em Python..."
cd karatsuba_python || handle_error "Diretório karatsuba_python não encontrado"

# Criar e ativar o venv
python3 -m venv venv || handle_error "Falha ao criar o venv"
source venv/bin/activate || handle_error "Falha ao ativar o venv"

# Instalar dependências
pip install -r requirements.txt || handle_error "Falha ao instalar dependências"

# Executar testes com pytest
pytest || handle_error "Testes em Python falharam"

# Desativar o venv
deactivate

# Voltar ao diretório raiz
cd ..

# Testes para o algoritmo em Rust
echo "Executando testes para o algoritmo em Rust..."
cd karatsuba_rust || handle_error "Diretório karatsuba_rust não encontrado"

# Instalar dependências e executar testes com cargo
cargo test || handle_error "Testes em Rust falharam"

# Voltar ao diretório raiz
cd ..

echo "Todos os testes foram executados com sucesso!"