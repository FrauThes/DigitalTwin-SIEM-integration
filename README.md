# DigitalTwin-SIEM-integration

TODO

## Installation

TODO

```bash
pip install todo
```
### Docker
Docker Compose is the most convenient way to setup the project:
1. Install Docker Compose as explained here: https://docs.docker.com/compose/install/
2. Download and unzip or clone the project:
    ```bash
    git clone https://github.com/FrauThes/DigitalTwin-SIEM-integration.git
    ```
3. Run the init script:
    ```bash
    cd /deployments/docker && \
    sudo sh init.sh
    ```
4. Enter the IP address or Hostname of the server when requested. For example:
    ```
    Enter the Hostname or IP Address where your elasticsearch will be deployed:192.168.2.120
    ```
5. The script is trying to import the Dsiem dashboard to Kibana. This may take a few minutes. Until Kibana is up and running, error messages are shown. This is normal. Example error message:
    ```
    curl: (22) The requested URL returned error: 503 Service Unavailable
    cannot connect to localhost:5601, will retry in 5 sec ..
    ```
6. The project is ready. You can now open Kibana in your browser:
    ```
    http://192.168.2.120:5601/
    ```
    replace **192.168.2.120** with the IP you have set previously.

The Project is up and running. If you want to start it a second time you simply have to navigate to deployments/docker and run `docker-compose up`.
## Usage

TODO
