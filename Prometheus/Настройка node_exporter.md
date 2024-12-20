```bash 
> wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz
> tar xvfz node_exporter-1.8.2.linux-amd64.tar.gz
> mv node_exporter /usr/bun
> useradd -rs /bin/false node_exporter
> chown node_exporter:node_exporter /usr/bin/node_exporter
> sudo vim /etc/systemd/system/node_exporter.service
```

```bash
[Unit]
Description=Prometheus node exporter
After=network.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
Restart=on-failure
ExecStart=/usr/bin/node_exporter

[Install]
WantedBy=multi-user.target
```

```bash
> systemctl daemon-reload
> systemctl start prometheus.service
> systemctl status prometheus.service
> systemctl enable prometheus.service
> 

```