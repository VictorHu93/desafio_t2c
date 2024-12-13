# RPA de Rastreamento de Pedidos e Geração de Invoice

## Visão Geral
Este projeto implementa um RPA (Robotic Process Automation) para processar pedidos de vendas, rastrear itens associados e gerar invoices com base em um conjunto de regras predefinidas.

O RPA utiliza Selenium para interação com interfaces web e SQLite para armazenamento de dados de rastreamento e status dos pedidos.

## Funcionalidades Principais
- **Login**: Realiza login e pré-login em diferentes portais.
- **Processamento de Pedidos**: Processa linhas de uma tabela de pedidos, identificando status elegíveis para rastreamento.
- **Rastreamento de Itens**: Verifica o status de entrega de itens associados aos pedidos.
- **Ações Condicionais**: Gera invoices para pedidos completamente entregues ou fecha pedidos incompletos.
- **Armazenamento de Dados**: Salva informações de rastreamento e status no banco de dados SQLite.

## Estrutura do Projeto
```
├── src
│   ├── config
│   │   ├── environment
│   │   │   ├── login.py
│   │   │   ├── urls.py
│   ├── data
│   │   ├── tracking_repository.py
│   ├── locators
│   │   ├── login_locators.py
│   │   ├── sales_order_locators.py
│   │   ├── tracking_locators.py
│   ├── pages
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── sales_order_page.py
│   │   ├── tracking_page.py
│   ├── services
│   │   ├── rpa_services.py
│   ├── utils
│   │   ├── logger.py
│   │   ├── web_manager.py
├── logs
├── venv
├── main.py
├── requirements.txt
├── README.md
├── sales_orders.db
├── env
├── gitignore
```

## Configuração do Ambiente

1. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Variáveis de Ambiente**:
   Configure as variáveis de ambiente no sistema ou em um arquivo `.env` para:
   - **USER**: Usuário para login.
   - **PASSWORD**: Senha para login.
   - **PRE_USER**: Usuário para pré-login.
   - **PRE_PASSWORD**: Senha para pré-login.

3. **Banco de Dados**:
   O banco de dados SQLite é gerado automaticamente no arquivo `sales_orders.db` na raiz do projeto.

## Execução do RPA
Execute o arquivo principal:
```bash
python main.py
```

## Principais Classes

### **BasePage**
Classe base para interações com o navegador.
- **find_element(locator)**: Localiza um elemento.
- **click(locator)**: Clica em um elemento.
- **send_keys(value, locator)**: Envia texto para um campo.
- **open(url)**: Abre uma URL.

### **LoginPage**
Realiza login e pré-login nos portais.

### **SalesOrderPage**
Processa linhas da tabela de pedidos e realiza ações baseadas nos status.

### **TrackingPage**
Rastreia itens dos pedidos e valida o status de entrega.

### **TrackingRepository**
Gerencia o banco de dados SQLite para salvar rastreamentos e status dos pedidos.

### **WebManager**
Gerencia instâncias do WebDriver para automação de navegadores.

### **Logger**
Configura loggers para registrar atividades e erros do sistema.

## Logs
Os logs são gerados em arquivos separados dentro do diretório `logs`:
- **main.log**: Logs gerais da execução do RPA.
- **sales_order_page.log**: Logs relacionados ao processamento de pedidos.
- **tracking_page.log**: Logs relacionados ao rastreamento de itens.