szavak = input("Kérem, adjon meg a szavakat tartalmazó listát, vesszővel elválasztva: ").split(",")
nagybetus_szavak = list(map(str.upper, szavak))
print("Eredeti lista:", szavak)
print("Generált lista (csupa nagybetűvel):", nagybetus_szavak)