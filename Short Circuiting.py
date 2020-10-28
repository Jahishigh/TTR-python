# Avec or, si le premier élément est True, le code va se rendre compte que la suite ne sert à rien et sauter le reste
# pour aller vers le print direct. Ce qui évite donc au code des calcules inutile
# and fonctionne de la même manière car si le premier ne répond pas à la condition, il s'arrête tout de suite
is_friend = True
is_user = True
if is_friend or is_user:
    print('best friend for ever')