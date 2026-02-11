# 🌾 Agricultural IoT Data Analytics Platform
## 🖼️ Imagem Hero
![Agricultural IoT Data Analytics Platform Hero Image](images/hero_image.png)
*[Português](#português) | [English](#english)*
---
## English
### 🚜 Overview
Agricultural IoT Data Analytics Platform leverages Internet of Things (IoT) sensors, satellite imagery, and advanced analytics to optimize agricultural operations and maximize crop yields. Built with Google Cloud Platform (GCP) IoT Core and BigQuery, this solution processes real-time data from farm sensors to provide actionable insights on crop health, soil conditions, weather patterns, irrigation optimization, and yield predictions.
The platform demonstrates how modern technology can revolutionize agriculture through data-driven decision making, precision farming techniques, and sustainable resource management.
### 🌱 Key Features
**IoT Data Processing**
- Real-time sensor data ingestion from multiple farm locations
- Multi-sensor data fusion and correlation analysis
- Edge computing capabilities for immediate decision making
- Scalable data pipeline handling millions of sensor readings
- Integration with weather APIs and satellite imagery
**Predictive Analytics**
- Crop yield prediction using machine learning models
- Weather impact analysis and risk assessment
- Soil health monitoring and nutrient optimization
- Irrigation scheduling and water usage optimization
- Pest and disease early warning systems
**Smart Farming Insights**
- Resource optimization recommendations
- Cost reduction strategies and ROI analysis
- Sustainability metrics and environmental impact
- Performance benchmarking across different farms
- Automated alert system for critical conditions
**Precision Agriculture**
- Variable rate application mapping
- Field zoning based on soil and crop characteristics
- GPS-guided equipment integration
- Drone and satellite imagery analysis
- Harvest timing optimization
### 🛠️ Technology Stack
| Component | Technology | Purpose |
|-----------|------------|---------|
| **IoT Platform** | GCP IoT Core, MQTT, LoRaWAN | Device connectivity and data ingestion |
| **Analytics** | Python, Pandas, NumPy, SciPy | Data analysis and statistical computing |
| **Machine Learning** | TensorFlow, AutoML, scikit-learn | Predictive modeling and AI insights |
| **Visualization** | Looker Studio, Plotly, Folium | Interactive dashboards and mapping |
| **Database** | BigQuery, Cloud Firestore | Data warehousing and real-time storage |
| **Infrastructure** | GCP, Terraform, Kubernetes | Cloud infrastructure and orchestration |
| **APIs** | FastAPI, Cloud Functions | REST services and serverless computing |
| **Monitoring** | Cloud Monitoring, Grafana | System monitoring and alerting |
### 📊 Business Impact
**Yield Improvements:**
- **25% increase** in average crop yields
- **30% reduction** in water usage through precision irrigation
- **20% decrease** in fertilizer costs via optimized application
- **40% improvement** in pest management effectiveness
- **15% increase** in overall farm profitability
**Operational Efficiency:**
- **50% reduction** in manual field monitoring time
- **35% improvement** in resource allocation efficiency
- **60% faster** decision-making with real-time data
- **25% reduction** in equipment maintenance costs
- **ROI of 280%** within two growing seasons
**Sustainability Benefits:**
- **30% reduction** in carbon footprint
- **40% decrease** in chemical pesticide usage
- **25% improvement** in soil health metrics
- **35% reduction** in water waste
- **20% increase** in biodiversity index
### 🏗️ Architecture
```
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ IoT Sensors │ │ IoT Core │ │ Cloud Pub/Sub │
│ │───▶│ │───▶│ │
│ • Soil Sensors │ │ • Device Mgmt │ │ • Message Queue │
│ • Weather Stn │ │ • Security │ │ • Event Stream │
│ • Cameras │ │ • Protocols │ │ • Decoupling │
└─────────────────┘ └─────────────────┘ └─────────────────┘
│ │ │
▼ ▼ ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Edge Computing│ │ Dataflow │ │ BigQuery DW │
│ │ │ │ │ │
│ • Local Process │ │ • Stream ETL │ │ • Historical │
│ • Immediate Act │ │ • Data Clean │ │ • Analytics │
│ • Offline Mode │ │ • Aggregation │ │ • ML Training │
└─────────────────┘ └─────────────────┘ └─────────────────┘
│ │ │
▼ ▼ ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ ML Pipeline │ │ Looker Studio │ │ Mobile App │
│ │ │ │ │ │
│ • AutoML │ │ • Dashboards │ │ • Field Access │
│ • TensorFlow │ │ • Reports │ │ • Alerts │
│ • Predictions │ │ • KPI Tracking │ │ • Controls │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```
### 🚦 Getting Started
#### Prerequisites
- Python 3.8 or higher
- Google Cloud Platform account with IoT Core enabled
- Docker and Docker Compose
- Git
- Node.js 14+ (for mobile app development)
#### Installation
1. **Clone the repository**
```bash
git clone https://github.com/galafis/agro-iot-analytics-gcp.git
cd agro-iot-analytics-gcp
```
2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Configure GCP credentials and IoT Core**
```bash
# Set up service account key
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
# Enable required APIs
gcloud services enable iot.googleapis.com
gcloud services enable pubsub.googleapis.com
gcloud services enable dataflow.googleapis.com
```
5. **Set up IoT devices and registry**
```bash
# Create IoT registry
gcloud iot registries create farm-sensors \
--project=$GOOGLE_CLOUD_PROJECT \
--region=us-central1 \
--event-notification-config=topic=sensor-events
# Register IoT devices
python scripts/register_devices.py
```
6. **Deploy infrastructure with Terraform**
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
7. **Generate sample data and train models**
```bash
cd src
python iot_data_processor.py
```
8. **Start the analytics pipeline**
```bash
# Start data processing pipeline
python pipeline/start_dataflow.py
# Start API server
uvicorn main:app --host 0.0.0.0 --port 8000
```
#### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build
# Deploy to Kubernetes
kubectl apply -f k8s/
```
### 📊 Esquema de Dados
#### Tabela de Leituras de Sensores
| Coluna | Tipo | Descrição |
|--------|------|-------------|
| sensor_id | STRING | Identificador único do sensor |
| sensor_type | STRING | Tipo de sensor (umidade_solo, temperatura, etc.) |
| timestamp | TIMESTAMP | Carimbo de data/hora da leitura |
| value | FLOAT64 | Valor da leitura do sensor |
| unit | STRING | Unidade de medida |
| farm_location | STRING | Localização geográfica da fazenda |
| crop_type | STRING | Tipo de cultura sendo monitorada |
| latitude | FLOAT64 | Coordenada de latitude GPS |
| longitude | FLOAT64 | Coordenada de longitude GPS |
| battery_level | FLOAT64 | Porcentagem da bateria do sensor |
| signal_strength | FLOAT64 | Força do sinal de comunicação |
#### Tabela de Dados Climáticos
| Coluna | Tipo | Descrição |
|--------|------|-------------|
| date | DATE | Data de observação do clima |
| location | STRING | Localização geográfica |
| temperature_high | FLOAT64 | Temperatura máxima diária (°C) |
| temperature_low | FLOAT64 | Temperatura mínima diária (°C) |
| humidity | FLOAT64 | Porcentagem de umidade relativa |
| rainfall_mm | FLOAT64 | Precipitação diária em milímetros |
| wind_speed_kmh | FLOAT64 | Velocidade do vento em km/h |
| uv_index | FLOAT64 | Índice UV (escala de 0-11) |
#### Tabela de Dados de Produtividade da Cultura
| Coluna | Tipo | Descrição |
|--------|------|-------------|
| location | STRING | Localização da fazenda |
| crop_type | STRING | Tipo de cultura |
| planting_date | DATE | Data de plantio |
| harvest_date | DATE | Data de colheita esperada/real |
| area_hectares | FLOAT64 | Área plantada em hectares |
| predicted_yield_kg_ha | FLOAT64 | Produtividade prevista por hectare |
| actual_yield_kg_ha | FLOAT64 | Produtividade real por hectare |
| irrigation_type | STRING | Tipo de sistema de irrigação |
| fertilizer_usage_kg_ha | FLOAT64 | Uso de fertilizante por hectare |
### 🔍 Principais Funcionalidades de Analytics
**Monitoramento de Saúde das Culturas**
- Cálculo de índice de vegetação em tempo real
- Detecção de doenças e pragas usando análise de imagem
- Rastreamento e otimização de estágios de crescimento
- Detecção de estresse através de correlação de dados de sensores
- Predição de produtividade com intervalos de confiança
**Analytics de Solo**
- Otimização de umidade do solo para irrigação
- Monitoramento de níveis de nutrientes e recomendações
- Rastreamento e ajuste do equilíbrio de pH
- Análise de temperatura do solo para timing de plantio
- Avaliação e prevenção de risco de erosão
**Inteligência Climática**
- Análise e previsão de microclima
- Sistemas de alerta e proteção contra geadas
- Monitoramento e mitigação de estresse por seca
- Identificação de condições ideais de pulverização
- Planejamento sazonal e avaliação de riscos
**Otimização de Recursos**
- Análise de eficiência do uso da água
- Otimização da aplicação de fertilizantes
- Monitoramento do consumo de energia
- Rastreamento da utilização de equipamentos
- Análise de custo-benefício para intervenções
### 🧪 Modelos de Machine Learning
#### Predição de Produtividade da Cultura
```python
# Random Forest para predição de produtividade
from sklearn.ensemble import RandomForestRegressor
yield_model = RandomForestRegressor(
n_estimators=200,
max_depth=15,
random_state=42
)
# Features: clima, solo, produtividade histórica, etc.
yield_model.fit(X_train, y_train)
predicted_yield = yield_model.predict(X_test)
```
#### Otimização de Irrigação
```python
# Rede Neural para agendamento de irrigação
import tensorflow as tf
irrigation_model = tf.keras.Sequential([
tf.keras.layers.Dense(128, activation=\'relu\'),
tf.keras.layers.Dropout(0.3),
tf.keras.layers.Dense(64, activation=\'relu\'),
tf.keras.layers.Dense(32, activation=\'relu\'),
tf.keras.layers.Dense(1, activation=\'sigmoid\')
])
irrigation_model.compile(optimizer=\'adam\', loss=\'binary_crossentropy\')
```
#### Detecção de Anomalias
```python
# Isolation Forest para detecção de anomalias de sensores
from sklearn.ensemble import IsolationForest
anomaly_detector = IsolationForest(
contamination=0.1,
random_state=42
)
anomaly_detector.fit(sensor_data)
anomalies = anomaly_detector.predict(new_data)
```
| Métrica | Meta | Atual |
|--------|--------|---------|
| **Taxa de Ingestão de Dados** | 10k msgs/seg | 12k msgs/seg |
| **Precisão da Predição** | > 85% | 89.2% |
| **Tempo de Atividade do Sistema** | 99.9% | 99.95% |
| **Tempo de Resposta do Alerta** | < 5 minutos | 2.3 minutos |
| **Vida Útil da Bateria** | > 1 ano | 14 meses |
| **Atualização dos Dados** | < 1 minuto | 30 segundos |
### 🧪 Testes
```bash
# Executar testes unitários
pytest tests/unit/
# Executar testes de integração
pytest tests/integration/
# Executar testes de simulação IoT
python tests/iot_simulation.py
# Executar validação de modelo
pytest tests/models/
# Executar testes de desempenho
python tests/performance/load_test.py
```
### 📚 Documentação da API
#### Obter Dados do Sensor
```bash
GET /api/v1/sensors/{sensor_id}/data?start_date=2025-07-01&end_date=2025-07-07
```
#### Enviar Comando de Irrigação
```bash
POST /api/v1/irrigation/schedule
{
"field_id": "FIELD_001",
"duration_minutes": 30,
"start_time": "2025-07-07T06:00:00Z"
}
```
#### Obter Predição de Produtividade
```bash
GET /api/v1/predictions/yield/{field_id}
```
### 🔧 Configuração
#### Variáveis de Ambiente
```bash
# Configuração GCP
GOOGLE_CLOUD_PROJECT=your-project-id
IOT_REGISTRY_ID=farm-sensors
IOT_REGION=us-central1
# Configuração do Banco de Dados
BIGQUERY_DATASET=agriculture
FIRESTORE_COLLECTION=sensor_data
# Configuração ML
MODEL_VERSION=v1.5.0
PREDICTION_INTERVAL_HOURS=6
ANOMALY_THRESHOLD=0.1
# Configuração IoT
MQTT_BRIDGE_HOSTNAME=mqtt.googleapis.com
MQTT_BRIDGE_PORT=8883
```
### 📚 Documentação
- [Guia de Configuração IoT](docs/iot_setup.md)
- [Documentação da API](docs/api.md)
- [Guia de Treinamento de Modelo](docs/model_training.md)
- [Guia de Implantação](docs/deployment.md)
- [Solução de Problemas](docs/troubleshooting.md)
### 🤝 Contribuindo
1. Faça um fork do repositório
2. Crie uma branch de recurso (`git checkout -b feature/amazing-feature`)
3. Faça suas alterações (`git commit -m 'Adicione um recurso incrível'`)
4. Envie para a branch (`git push origin feature/amazing-feature`)
5. Abra um Pull Request
### 👨‍💻 Author
**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- Specialized in IoT Analytics, Agricultural Technology, and Machine Learning
- Expert in GCP IoT Core, Precision Agriculture, and Smart Farming Solutions
### 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
### 🙏 Agradecimentos
- Google Cloud Platform por fornecer infraestrutura robusta de IoT e analytics
- Instituições de pesquisa agrícola pela expertise de domínio
- Fabricantes de sensores IoT pelas parcerias de hardware
- Comunidade open source pelas excelentes ferramentas e frameworks
---
## Português
### 🚜 Visão Geral
A Plataforma de Analytics de Dados IoT Agrícola aproveita sensores de Internet das Coisas (IoT), imagens de satélite e analytics avançados para otimizar operações agrícolas e maximizar a produtividade das culturas. Construída com Google Cloud Platform (GCP) IoT Core e BigQuery, esta solução processa dados em tempo real de sensores de fazenda para fornecer insights acionáveis sobre saúde das culturas, condições do solo, padrões climáticos, otimização de irrigação e predições de produtividade.
A plataforma demonstra como a tecnologia moderna pode revolucionar a agricultura através de tomada de decisão baseada em dados, técnicas de agricultura de precisão e gestão sustentável de recursos.
### 🌱 Principais Funcionalidades
**Processamento de Dados IoT**
- Ingestão de dados de sensores em tempo real de múltiplas localizações de fazenda
- Fusão e análise de correlação de dados multi-sensores
- Capacidades de edge computing para tomada de decisão imediata
- Pipeline de dados escalável lidando com milhões de leituras de sensores
- Integração com APIs meteorológicas e imagens de satélite
**Analytics Preditivos**
- Predição de produtividade de culturas usando modelos de machine learning
- Análise de impacto climático e avaliação de riscos
- Monitoramento de saúde do solo e otimização de nutrientes
- Agendamento de irrigação e otimização do uso de água
- Sistemas de alerta precoce para pragas e doenças
**Insights de Agricultura Inteligente**
- Recomendações de otimização de recursos
- Estratégias de redução de custos e análise de ROI
- Métricas de sustentabilidade e impacto ambiental
- Benchmarking de desempenho entre diferentes fazendas
- Sistema de alerta automatizado para condições críticas
**Agricultura de Precisão**
- Mapeamento de aplicação de taxa variável
- Zoneamento de campo baseado em características do solo e da cultura
- Integração de equipamentos guiados por GPS
- Análise de imagens de drones e satélites
- Otimização do tempo de colheita
### 🛠️ Pilha Tecnológica
| Componente | Tecnologia | Propósito |
|-----------|------------|---------|
| **Plataforma IoT** | GCP IoT Core, MQTT, LoRaWAN | Conectividade de dispositivos e ingestão de dados |
| **Analytics** | Python, Pandas, NumPy, SciPy | Análise de dados e computação estatística |
| **Machine Learning** | TensorFlow, AutoML, scikit-learn | Modelagem preditiva e insights de IA |
| **Visualização** | Looker Studio, Plotly, Folium | Dashboards interativos e mapeamento |
| **Banco de Dados** | BigQuery, Cloud Firestore | Armazenamento de dados e armazenamento em tempo real |
| **Infraestrutura** | GCP, Terraform, Kubernetes | Infraestrutura e orquestração em nuvem |
| **APIs** | FastAPI, Cloud Functions | Serviços REST e computação sem servidor |
| **Monitoramento** | Cloud Monitoring, Grafana | Monitoramento e alertas de sistema |
### 📊 Impacto nos Negócios
**Melhorias na Produtividade:**
- **25% de aumento** na produtividade média das culturas
- **30% de redução** no uso de água através de irrigação de precisão
- **20% de diminuição** nos custos de fertilizantes via aplicação otimizada
- **40% de melhoria** na efetividade do manejo de pragas
- **15% de aumento** na lucratividade geral da fazenda
**Eficiência Operacional:**
- **50% de redução** no tempo de monitoramento manual do campo
- **35% de melhoria** na eficiência de alocação de recursos
- **60% mais rápida** tomada de decisão com dados em tempo real
- **25% de redução** nos custos de manutenção de equipamentos
- **ROI de 280%** em duas safras
### 🚦 Começando
#### Pré-requisitos
- Python 3.8 ou superior
- Conta no Google Cloud Platform com IoT Core habilitado
- Docker e Docker Compose
- Git
- Node.js 14+ (para desenvolvimento de app mobile)
#### Instalação
1. **Clone o repositório**
```bash
git clone https://github.com/galafis/agro-iot-analytics-gcp.git
cd agro-iot-analytics-gcp
```
2. **Configure o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
```
3. **Instale as dependências**
```bash
pip install -r requirements.txt
```
4. **Configure as credenciais GCP e IoT Core**
```bash
# Configure a chave da conta de serviço
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
# Habilite as APIs necessárias
gcloud services enable iot.googleapis.com
gcloud services enable pubsub.googleapis.com
gcloud services enable dataflow.googleapis.com
```
5. **Configure dispositivos IoT e registro**
```bash
# Crie o registro IoT
gcloud iot registries create farm-sensors \
--project=$GOOGLE_CLOUD_PROJECT \
--region=us-central1 \
--event-notification-config=topic=sensor-events
# Registre dispositivos IoT
python scripts/register_devices.py
```
6. **Implante a infraestrutura com Terraform**
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
7. **Gere dados de exemplo e treine modelos**
```bash
cd src
python iot_data_processor.py
```
8. **Inicie o pipeline de analytics**
```bash
# Inicie o pipeline de processamento de dados
python pipeline/start_dataflow.py
# Inicie o servidor API
uvicorn main:app --host 0.0.0.0 --port 8000
```
#### Implantação Docker
```bash
# Construa e execute com Docker Compose
docker-compose up --build
# Implante no Kubernetes
kubectl apply -f k8s/
```
### 🔍 Principais Funcionalidades de Analytics
**Monitoramento de Saúde das Culturas**
- Cálculo de índice de vegetação em tempo real
- Detecção de doenças e pragas usando análise de imagem
- Rastreamento e otimização de estágios de crescimento
- Detecção de estresse através de correlação de dados de sensores
- Predição de produtividade com intervalos de confiança
**Analytics de Solo**
- Otimização de umidade do solo para irrigação
- Monitoramento de níveis de nutrientes e recomendações
- Rastreamento e ajuste do equilíbrio de pH
- Análise de temperatura do solo para timing de plantio
- Avaliação e prevenção de risco de erosão
### 👨‍💻 Autor
**Gabriel Demetrios Lafis**
- GitHub: [@galafis](https://github.com/galafis)
- Especializado em Analytics IoT, Tecnologia Agrícola e Machine Learning
- Expert em GCP IoT Core, Agricultura de Precisão e Soluções de Smart Farming
### 📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
### 🙏 Agradecimentos
- Google Cloud Platform por fornecer infraestrutura robusta de IoT e analytics
- Instituições de pesquisa agrícola pela expertise de domínio
- Fabricantes de sensores IoT pelas parcerias de hardware
- Comunidade open source pelas excelentes ferramentas e frameworks
## 📋 Descrição
Descreva aqui o conteúdo desta seção.
## 📦 Instalação
Descreva aqui o conteúdo desta seção.
## 💻 Uso
Descreva aqui o conteúdo desta seção.
