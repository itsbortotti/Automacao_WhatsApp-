
# WhatsApp Automation Script

Este projeto contém um script em Python que utiliza Selenium para automatizar o envio de mensagens de texto e arquivos via WhatsApp Web. Ele é útil para agendar o envio de mensagens de forma repetitiva ou em horários específicos, usando a interface do WhatsApp Web.

## Funcionalidades

- Envio automatizado de mensagens de texto para contatos ou grupos específicos.
- Envio automatizado de arquivos para contatos ou grupos.
- Agendamento de envios em intervalos de tempo determinados.

## Pré-requisitos

Antes de iniciar o projeto, certifique-se de ter o seguinte instalado em sua máquina:

- **Python 3.x**: Você pode verificar se o Python está instalado executando `python3 --version`.
- **pip**: O gerenciador de pacotes do Python. Geralmente, ele vem instalado junto com o Python.
- **Google Chrome**: Navegador utilizado pelo Selenium.
- **ChromeDriver**: Necessário para o Selenium controlar o navegador Chrome.

## Instalação

Siga as etapas abaixo para configurar o ambiente do projeto em uma nova máquina:

### 1. Clone o repositório

Clone o repositório do GitHub para sua máquina local:

```bash
git clone https://github.com/itsbortotti/WhatsApp_Automation_Script.git
cd WhatsApp_Automation_Script
```

### 2. Crie um ambiente virtual

Crie e ative um ambiente virtual para isolar as dependências do projeto:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 3. Instale as dependências do projeto

Com o ambiente virtual ativo, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 4. Baixe e configure o ChromeDriver

O Selenium precisa do ChromeDriver para controlar o navegador Chrome. Faça o download do ChromeDriver [aqui](https://sites.google.com/chromium.org/driver/downloads) e coloque o executável em um diretório de sua escolha. No script, atualize o caminho para o ChromeDriver:

```python
service = Service('/caminho/para/seu/chromedriver')
```

### 5. Execute o Script

Agora, você está pronto para executar o script. Use o seguinte comando para iniciar:

```bash
python whatsapp_scheduler.py
```

## Uso

O script é configurado para enviar mensagens de texto ou arquivos para um contato ou grupo específico em intervalos de tempo determinados.

### Envio de Mensagem de Texto

Para enviar uma mensagem de texto, o script pode ser configurado da seguinte maneira:

```python
schedule.every(5).seconds.do(enviar_mensagem, tipo="texto", contato="NOME_DO_CONTATO", conteudo="Olá, esta é uma mensagem automática.")
```

### Envio de Arquivo

Para enviar um arquivo, o script pode ser configurado da seguinte maneira:

```python
schedule.every(5).seconds.do(enviar_mensagem, tipo="arquivo", contato="NOME_DO_CONTATO", conteudo="/caminho/para/seu/arquivo.pdf")
```

### Agendamento

Você pode configurar o agendamento usando a biblioteca `schedule`. No exemplo acima, a função `enviar_mensagem` será chamada a cada 5 segundos.

## Considerações

- **Sessão do WhatsApp Web**: O script salva os cookies da sessão para que você não precise escanear o QR code toda vez que o script for executado. Certifique-se de que o `whatsapp_session.pkl` seja salvo e carregado corretamente.
- **Automação Cautelosa**: Use a automação com responsabilidade para evitar possíveis violações dos termos de uso do WhatsApp.

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT) - veja o arquivo LICENSE para mais detalhes.
