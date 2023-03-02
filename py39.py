szavak = input("Kérem, adjon meg a szavakat tartalmazó listát, vesszővel elválasztva: ").split(",")
nagybetus_szavak = list(map(lambda s: s.upper() if len(s) > 3 else s, szavak))
print("Eredeti lista:", szavak)
print("Generált lista (csupa nagybetűvel):", nagybetus_szavak)