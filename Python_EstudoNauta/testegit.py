food = ['pizza', 'feijao', 'ceva', 'xis']
print(f'Comida Principal {food}')
friends_food = food[:]
food.append('Churras')
print(f'Comida Principal atualizada {food}')
print(f'Comida dos amigos {friends_food}')
friends_food.append('agua')
print(f'Comida Principal atualizada {food}')
