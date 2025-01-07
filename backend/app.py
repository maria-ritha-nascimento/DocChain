from flask import Flask, request, jsonify
from web3 import Web3
import os
from dotenv import load_dotenv
from solcx import compile_source, install_solc, get_installable_solc_versions

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do Flask
app = Flask(__name__)

# Configuração do Web3
ganache_url = os.getenv("GANACHE_URL", "HTTP://127.0.0.1:7545")
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    raise Exception("Erro ao conectar ao Ganache.")

# Conta padrão (do Ganache)
default_account = web3.eth.accounts[0]
web3.eth.default_account = default_account

@app.route('/deploy', methods=['POST'])
def deploy_contract():
    """
    Faz o deploy de um contrato inteligente na blockchain local.
    """
    try:
        # Caminho absoluto do arquivo .sol
        contract_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'contracts', 'SimpleContract.sol'))
        
        # Verificar se o arquivo existe antes de tentar abri-lo
        print("Caminho absoluto:", contract_path)
        print("Arquivo existe:", os.path.exists(contract_path))
        
        # Verificar e instalar o compilador Solidity (solc)
        available_versions = get_installable_solc_versions()
        print("Versões disponíveis do solc:", available_versions)
        
        # Definir a versão que queremos instalar
        required_version = '0.8.19'  # Ou qualquer versão desejada
        if required_version not in available_versions:
            print(f"Instalando a versão {required_version} do solc...")
            install_solc(required_version)  # Instalar versão desejada

        # Carregar contrato .sol
        contract_source_code = open(contract_path, 'r').read()
        
        # Compilar contrato
        compiled_sol = compile_source(contract_source_code)
        contract_interface = compiled_sol['<stdin>:SimpleContract']

        # Deploy do contrato
        SimpleContract = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
        tx_hash = SimpleContract.constructor().transact()
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        return jsonify({
            "status": "success",
            "contractAddress": tx_receipt.contractAddress,
            "txHash": tx_hash.hex()
        }), 200

    except Exception as e:
        print(f"Erro ao realizar o deploy: {str(e)}")  # Exibir o erro detalhado no console
        return jsonify({"status": "error", "message": f"Erro ao realizar o deploy: {str(e)}"}), 500

@app.route('/call', methods=['POST'])
def call_contract():
    """
    Chama uma função de leitura de um contrato.
    """
    try:
        data = request.json
        contract_address = data['contractAddress']
        function_name = data['functionName']
        abi = data['abi']

        # Conectar ao contrato
        contract = web3.eth.contract(address=contract_address, abi=abi)
        result = getattr(contract.functions, function_name)().call()

        return jsonify({"status": "success", "result": result}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
