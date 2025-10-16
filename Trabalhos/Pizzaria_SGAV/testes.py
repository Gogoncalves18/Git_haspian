from datetime import datetime

dados = ('bl1', 'bl1', '19:31:16', '19:31:16', '19:47:31', '19:54:23', '00:20:00', 7.3, 7.3, 'Jonathan Diego Souza ', '', '', 'Rua Doutor Alexandre Gutierrez, Água Verde, Curitiba', '359', 'Curitiba', -25.45043, -49.28418, -25.4576404, -49.2783563, 'none', '', '1.47', 4)
ent = 1
for i in dados:
    if i == 'bl1':
        try:
            num = int(i)
        except ValueError:
            num = 5000 + ent
            ent += 1        
            print(num)
        except Exception as e:
            print(e)
