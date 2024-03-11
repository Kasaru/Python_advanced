text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
while len(text) > 0:
    result[text[0]] = text.count(text[0])
    text = text.replace(text[0],'')
