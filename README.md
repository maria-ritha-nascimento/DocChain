# **DocChain**

**DocChain** é uma aplicação backend para criação, deploy e interação com contratos inteligentes (smart contracts) na blockchain Ethereum, utilizando uma arquitetura simples e fácil de integrar. Ele permite que os usuários deployem contratos inteligentes diretamente na blockchain local (usando Ganache) e façam chamadas de leitura a contratos implantados.

O **DocChain** oferece uma solução robusta para automação de processos e validações em blockchain, aplicável em vários contextos como autenticação, registros financeiros, ou qualquer outro processo que exija confiança e rastreabilidade.

---

## **Características**

- **Deploy de contratos inteligentes**: Permite o deploy de contratos inteligentes na blockchain Ethereum.
- **Leitura de contratos**: Realiza chamadas de leitura a funções públicas de contratos inteligentes já implantados.
- **Blockchain Ethereum**: Utiliza a blockchain Ethereum local, utilizando o Ganache para testes.
- **Interface Simples**: API RESTful para interação com contratos inteligentes.

---

## **Tecnologias Utilizadas**

- **Flask**: Framework web em Python para criar a API backend.
- **Web3.py**: Biblioteca para interagir com a blockchain Ethereum.
- **Solcx**: Biblioteca para compilar contratos inteligentes escritos em Solidity.
- **Ganache**: Ambiente local de blockchain Ethereum para testes.

---

## **Pré-requisitos**

Antes de executar o projeto, é necessário que você tenha instalado:

1. **Python 3.x** – [Download](https://www.python.org/downloads/)
2. **Ganache** – [Baixe o Ganache](https://www.trufflesuite.com/ganache) e execute-o para criar uma rede Ethereum local.
3. **Dependências do projeto** – Usaremos um ambiente virtual Python para isolar as dependências do projeto.

---

## **Como Executar o Projeto**

### 1. Clonando o Repositório

Primeiro, clone o repositório no seu computador:

```bash
git clone https://github.com/maria-ritha-nascimento/DocChain.git
cd DocChain/backend
```

### 2. Criando um Ambiente Virtual

Crie um ambiente virtual para instalar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows**:

    ```bash
    .\venv\Scripts\activate
    ```

- **Linux/macOS**:

    ```bash
    source venv/bin/activate
    ```

### 3. Instalando as Dependências

Instale todas as dependências do projeto executando:

```bash
pip install -r requirements.txt
```

### 4. Iniciando o Ganache

Execute o Ganache em sua máquina local para simular a blockchain Ethereum. Ao iniciar, o Ganache exibirá um conjunto de contas e informações de rede.

### 5. Configuração do `.env`

Crie um arquivo `.env` na pasta `backend` e configure a URL do Ganache:

```bash
GANACHE_URL=http://127.0.0.1:7545
```

### 6. Executando o Servidor Flask

Agora, você pode iniciar o servidor Flask executando:

```bash
python app.py
```

O servidor será iniciado e estará disponível em [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Endpoints da API**

### **POST /deploy**

Faz o deploy de um contrato inteligente na blockchain Ethereum local.

**Exemplo de requisição**:
```bash
POST http://127.0.0.1:5000/deploy
```

**Resposta esperada**:
```json
{
  "status": "success",
  "contractAddress": "0x1234...abcd",
  "txHash": "0xabc...1234"
}
```

### **POST /call**

Chama uma função de leitura de um contrato inteligente.

**Exemplo de requisição**:
```bash
POST http://127.0.0.1:5000/call
{
  "contractAddress": "0x1234...abcd",
  "functionName": "getValue",
  "abi": [ ... ]  // ABI do contrato
}
```

**Resposta esperada**:
```json
{
  "status": "success",
  "result": "42"
}
```

---

## **Testando o Projeto**

1. **Deploy de contrato**: Envie uma requisição POST para o endpoint `/deploy` para implantar um contrato inteligente na rede Ethereum local (Ganache).
   
2. **Leitura de contrato**: Envie uma requisição POST para o endpoint `/call` com os dados do contrato implantado para realizar uma chamada de leitura.

---

## **Considerações Finais**

O **DocChain** foi desenvolvido para ser uma solução simples e eficaz para interação com contratos inteligentes em uma blockchain Ethereum local. A utilização de **Ganache** como rede local proporciona um ambiente seguro e controlado para testes e experimentações.

---

## **Contribuindo**

Se você deseja contribuir com o projeto, por favor, siga os seguintes passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua nova feature (`git checkout -b feature/nome-da-feature`).
3. Realize suas modificações e faça um commit (`git commit -m 'Adicionando nova feature'`).
4. Envie suas modificações para o seu repositório fork (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request no repositório original.

---

## **Licença**

Este projeto está licenciado sob a **MIT License** – consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---
