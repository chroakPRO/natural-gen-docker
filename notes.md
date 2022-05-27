## Säkerhetsgransking (Christopher Ek)
---

- [## Säkerhetsgransking (Christopher Ek)](#-säkerhetsgransking-christopher-ek)
- [## **Day 01**](#-day-01)
  - [**OTG-CONFIG-01 (Broken auth)**](#otg-config-01-broken-auth)


## **Day 01**
---
---
**ACCOUNT:** Full access

**KLIENT:** Webbgränsnitt 

**OTHER:** N/A

---

### **OTG-CONFIG-01 (Broken auth)**
*Endpoint:* /api/v1/config/otg/config



***GET Requests***


`nmap -6 -T4 localhost`

---

***SQL CMD:s***

  

```sql
SELECT * FROM otg_config;

INSERT INTO otg_config (id, name, value) VALUES ('1', 'otg_config_01', 'value_01');

SELECT * FROM otg_config;

DELETE FROM otg_config WHERE id = '1';

SELECT * FROM otg_config;
```
---
---



