
```packet: Ether / IP / TCP 172.16.1.206:56381 > 93.184.215.14:http S
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 4c:eb:bd:25:fb:d3
  - Dst MAC: 48:2f:6b:c8:db:8a

[Network Layer: IP]
  - Src IP: 172.16.1.206
  - Dst IP: 93.184.215.14
  - TTL:    64

[Transport Layer: TCP]
  - Src Port: 56381
  - Dst Port: 80
  - Flags:    S

============================================================

packet: Ether / IP / TCP 93.184.215.14:http > 172.16.1.206:56381 SA
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 48:2f:6b:c8:db:8a
  - Dst MAC: 4c:eb:bd:25:fb:d3

[Network Layer: IP]
  - Src IP: 93.184.215.14
  - Dst IP: 172.16.1.206
  - TTL:    52

[Transport Layer: TCP]
  - Src Port: 80
  - Dst Port: 56381
  - Flags:    SA

============================================================

packet: Ether / IP / TCP 172.16.1.206:56381 > 93.184.215.14:http A
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 4c:eb:bd:25:fb:d3
  - Dst MAC: 48:2f:6b:c8:db:8a

[Network Layer: IP]
  - Src IP: 172.16.1.206
  - Dst IP: 93.184.215.14
  - TTL:    64

[Transport Layer: TCP]
  - Src Port: 56381
  - Dst Port: 80
  - Flags:    A

============================================================

packet: Ether / IP / TCP 172.16.1.206:56381 > 93.184.215.14:http PA / Raw
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 4c:eb:bd:25:fb:d3
  - Dst MAC: 48:2f:6b:c8:db:8a

[Network Layer: IP]
  - Src IP: 172.16.1.206
  - Dst IP: 93.184.215.14
  - TTL:    64

[Transport Layer: TCP]
  - Src Port: 56381
  - Dst Port: 80
  - Flags:    PA

[Application Layer: HTTP (Raw Data)]
GET / HTTP/1.1
Host: example.com
User-Agent: python-requests/2.31.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive


============================================================

packet: Ether / IP / TCP 93.184.215.14:http > 172.16.1.206:56381 A
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 48:2f:6b:c8:db:8a
  - Dst MAC: 4c:eb:bd:25:fb:d3

[Network Layer: IP]
  - Src IP: 93.184.215.14
  - Dst IP: 172.16.1.206
  - TTL:    52

[Transport Layer: TCP]
  - Src Port: 80
  - Dst Port: 56381
  - Flags:    A

============================================================

packet: Ether / IP / TCP 93.184.215.14:http > 172.16.1.206:56381 PA / Raw
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 48:2f:6b:09:73:32
  - Dst MAC: 4c:eb:bd:25:fb:d3

[Network Layer: IP]
  - Src IP: 93.184.215.14
  - Dst IP: 172.16.1.206
  - TTL:    52

[Transport Layer: TCP]
  - Src Port: 80
  - Dst Port: 56381
  - Flags:    PA

[Application Layer: HTTP (Raw Data)]
HTTP/1.1 200 OK
Content-Encoding: gzip
Age: 128350
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Sat, 21 Dec 2024 07:03:58 GMT
Etag: "3147526947+gzip"
Expires: Sat, 28 Dec 2024 07:03:58 GMT
Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
Server: ECAcc (sac/255B)
Vary: Accept-Encoding
X-Cache: HIT
Content-Length: 648

]}TMs WlK2#$'i␦-iiiiPt߻B#7]xﱐ)fc\3_om>ť:[>:_Ei1q޷
a#(Yy:@<%nZcdF
_{Y"
^򆹒7=A9#2Cs3b0Lyyӂ1v     9av-O
\a,9|r0w¦̡S.a'tpKx;hE
/Qy9E&+2˅\-s5fC.転o?ǡ%Մ
_IbB1śbpL`i,Km4NA)É[jt~QUDc$d
τ[fI$<1v!]O3*nHvHt|m:4tR1S-Z%#G!U
Ax4{A
(|o
============================================================

packet: Ether / IP / TCP 172.16.1.206:56381 > 93.184.215.14:http FA
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 4c:eb:bd:25:fb:d3
  - Dst MAC: 48:2f:6b:c8:db:8a

[Network Layer: IP]
  - Src IP: 172.16.1.206
  - Dst IP: 93.184.215.14
  - TTL:    64

[Transport Layer: TCP]
  - Src Port: 56381
  - Dst Port: 80
  - Flags:    FA

============================================================

packet: Ether / IP / TCP 93.184.215.14:http > 172.16.1.206:56381 FA
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 48:2f:6b:c8:db:8a
  - Dst MAC: 4c:eb:bd:25:fb:d3

[Network Layer: IP]
  - Src IP: 93.184.215.14
  - Dst IP: 172.16.1.206
  - TTL:    52

[Transport Layer: TCP]
  - Src Port: 80
  - Dst Port: 56381
  - Flags:    FA

============================================================

packet: Ether / IP / TCP 172.16.1.206:56381 > 93.184.215.14:http A
============================================================
[Data Link Layer: Ethernet]
  - Src MAC: 4c:eb:bd:25:fb:d3
  - Dst MAC: 48:2f:6b:c8:db:8a

[Network Layer: IP]
  - Src IP: 172.16.1.206
  - Dst IP: 93.184.215.14
  - TTL:    64

[Transport Layer: TCP]
  - Src Port: 56381
  - Dst Port: 80
  - Flags:    A

============================================================

```